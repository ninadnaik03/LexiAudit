"use client";

import { useState } from "react";
import Hero from "../components/Hero";
import Upload from "../components/Upload";
import Results from "../components/Results";

export default function Home() {
  const [data, setData] = useState(null);

  return (
    <main className="relative min-h-screen text-white flex flex-col items-center px-4 bg-black overflow-x-hidden">

      {/*  Background Glow Effects */}
      <div className="pointer-events-none absolute top-[-120px] left-[-120px] w-[300px] sm:w-[400px] h-[300px] sm:h-[400px] bg-blue-500/20 rounded-full blur-3xl"></div>
      <div className="pointer-events-none absolute bottom-[-120px] right-[-120px] w-[300px] sm:w-[400px] h-[300px] sm:h-[400px] bg-purple-500/20 rounded-full blur-3xl"></div>

      {/*  Content */}
      <div className="w-full flex flex-col items-center z-10">

        <Hero />
        <Upload setData={setData} />
        <Results data={data} />

        {/*  Footer */}
        <footer className="mt-16 sm:mt-20 text-xs sm:text-sm text-gray-500 text-center pb-6 px-4">
          Powered by FastAPI · ChromaDB · Sentence Transformers · Rule-Based Risk Engine
        </footer>

      </div>

    </main>
  );
}