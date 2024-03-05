import SidebarLink from "@/components/Docs/SidebarLink";
import { Metadata } from "next";
import { useState } from 'react';
// import Replicate from "replicate";
export const metadata: Metadata = {
  title: "GenMedia",
  description: "This is Docs page for Solid Pro",
  // other metadata
};


// const replicate = new Replicate({
//   auth: process.env.REPLICATE_API_TOKEN,
// });

// const output = await replicate.run(
//   "pollinations/music-gen:9b8643c06debace10b9026f94dcb117f61dc1fee66558a09cde4cfbf51bcced6",
//   {
//     input: {
//       text: "A dynamic blend of hip-hop and orchestral elements, with sweeping strings and brass, evoking the vibrant energy of the city.",
//       duration: 12
//     }
//   }
// );
// console.log(output);

// async function generateMusic() {
//   const output = await replicate.run(
//       "pollinations/music-gen:9b8643c06debace10b9026f94dcb117f61dc1fee66558a09cde4cfbf51bcced6",
//       {
//           input: {
//               text: "A dynamic blend of hip-hop and orchestral elements, with sweeping strings and brass, evoking the vibrant energy of the city.",
//               duration: 12
//           }
//       }
//   );
//   console.log(output);
// }

// generateMusic();





export default function DocsPage() {
  
  // async function query(data) {
  //   const response = await fetch(
  //     "https://api-inference.huggingface.co/models/facebook/musicgen-medium",
  //     {
  //       headers: {
  //         Authorization: "Bearer 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",
  //       },
  //       method: "POST",
  //       body: JSON.stringify(data),
  //     },
  //   );
    
  //   const result = await response.blob();

    
  //   return result;
  // }

  // const data = query({ inputs: "liquid drum and bass" }).then((response) => {
  //   console.log(response);

  // });

  const iframeSrc = 'http://127.0.0.1:7860';
  const image = 'http://127.0.0.1:7861/';
  
  return (
    <>
      <section className="pb-16 pt-24 md:pb-20 md:pt-28 lg:pb-24 lg:pt-32">
        <div className="container mx-auto">
          <div className="-mx-4 flex flex-wrap">
            

            <div className="w-full px-4 lg:w-3/4">
              <h1>Welcome to GenMedia</h1>

                <iframe
        title="Local Server Iframe"
        src={iframeSrc}
        className="w-full h-full m-2 p-2"
        frameBorder="0"
      />
                <iframe
        title="Local Server Iframe"
        src={image}
        className="w-full h-full m-2 p-2"
        frameBorder="0"
      />
               
             
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
