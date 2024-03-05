from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from moviepy.editor import ImageClip, AudioFileClip
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        audio_file = request.files['audio']
        image_file = request.files['image']
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp4')

        # Save uploaded files
        audio_path = os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(audio_file.filename))
        image_path = os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(image_file.filename))
        audio_file.save(audio_path)
        image_file.save(image_path)

        # Merge audio and image files
        image_clip = ImageClip(image_path).set_duration(10)
        audio_clip = AudioFileClip(audio_path)
        final_clip = image_clip.set_audio(audio_clip)
        final_clip.write_videofile(
            output_path, codec='libx264', audio_codec='aac', fps=24)

        # Delete temporary files
        os.remove(audio_path)
        os.remove(image_path)

        return jsonify({'success': True, 'video_url': output_path})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
