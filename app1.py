from flask import send_from_directory
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from moviepy.editor import ImageClip, AudioFileClip
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Check if the 'uploads' directory exists and create it if it doesn't
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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
        merge_image_and_audio(image_path, audio_path, output_path)

        # Delete temporary files
        os.remove(audio_path)
        os.remove(image_path)

        return jsonify({'success': True, 'video_url': output_path})
    except Exception as e:
        return jsonify({'error': str(e)})


def merge_image_and_audio(image_path, audio_path, output_path):
    try:
        # Load image and audio clips
        audio_clip = AudioFileClip(audio_path)  # Use the saved audio path
        image_clip = ImageClip(image_path).set_duration(
            audio_clip.duration)  # Set the duration to match the audio clip
        final_clip = image_clip.set_audio(audio_clip)

        # Write the video file to output path
        final_clip.write_videofile(
            output_path, codec='libx264', audio_codec='aac', fps=24)

        print("Video successfully generated:", output_path)
    except Exception as e:
        print("Error:", e)


if __name__ == '__main__':
    app.run(debug=True)
