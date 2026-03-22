"use client";
import { useState } from "react";
import Pipeline from "./Pipeline";

export default function Upload({ setData }: any) {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (selectedFile?: File) => {
    const fileToUse = selectedFile || file;
    if (!fileToUse) return;

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", fileToUse);

      const res = await fetch("https://lexiaudit.onrender.com/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setData(data);
    } catch (err) {
      console.error("Upload failed:", err);
    }

    setLoading(false);
  };

  // 🔥 PREMIUM DEMO DATASET (REALISTIC OUTPUT)
  const handleDemo = () => {
    setLoading(true);

    setTimeout(() => {
      const demoData = {
        contract_type: "Non-Disclosure Agreement (NDA)",

        parties: [
          "Acme Technologies Pvt. Ltd.",
          "Zenith Data Systems Inc.",
          "John A. Reynolds (Independent Consultant)",
        ],

        risks: [
          "Unlimited liability clause",
          "Termination without prior notice",
          "Broad indemnification obligation",
          "Unilateral modification rights",
          "Ambiguous confidentiality duration",
          "No defined dispute resolution mechanism",
        ],
      };

      setData(demoData);
      setLoading(false);
    }, 2200); // realistic processing delay
  };

  return (
    <section className="mt-10 sm:mt-16 w-full max-w-md sm:max-w-xl px-2">

      {/* Upload Card */}
      <div className="backdrop-blur-xl bg-white/5 border border-white/10 rounded-2xl p-4 sm:p-6 shadow-[0_0_40px_rgba(59,130,246,0.15)]">

        <input
          type="file"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="mb-4 w-full text-sm text-gray-400 file:bg-blue-600 file:text-white file:px-3 file:py-2 file:border-0 file:rounded-lg file:mr-2 hover:file:bg-blue-700"
        />

        <button
          onClick={() => handleUpload()}
          disabled={loading}
          className="w-full py-3 rounded-xl bg-blue-600 hover:bg-blue-700 transition shadow-lg shadow-blue-500/20 text-base font-medium disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>

        {/* 🔥 DEMO BUTTON */}
        <button
          onClick={handleDemo}
          disabled={loading}
          className="w-full mt-3 py-2 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition text-sm"
        >
          Load Demo Dataset (Pre-analyzed Contract)
        </button>

      </div>

      {/* Pipeline Visualization */}
      <Pipeline loading={loading} />

    </section>
  );
}
