import BlogData from "@/components/Blog/blogData";
import BlogItem from "@/components/Blog/BlogItem";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Blog Page - Solid SaaS Boilerplate",
  description: "This is Blog page for Solid Pro",
  // other metadata
};

const iframeSrc = 'http://127.0.0.1:7860';
const BlogPage = async () => {
  return (
    <>
      {/* <!-- ===== Blog Grid Start ===== --> */}
      {/* <section className="py-20 lg:py-25 xl:py-30 w-full h-full"> */}
      <iframe
        title="Local Server Iframe"
        src={iframeSrc}
        className="w-full h-full"
        frameBorder="0"
      />
      {/* </section> */}
      {/* <!-- ===== Blog Grid End ===== --> */}
    </>
  );
};

export default BlogPage;
