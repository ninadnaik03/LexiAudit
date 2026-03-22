"use client";
import { useEffect, useState } from "react";

export default function Pipeline({ loading }: { loading: boolean }) {
  const steps = [
    "PDF Parsing & Layout Analysis",
    "Semantic Chunking",
    "Entity Recognition (NER)",
    "Contract Classification",
    "Risk Detection Engine",
  ];

  const [activeStep, setActiveStep] = useState(-1);

  useEffect(() => {
    if (!loading) {
      setActiveStep(steps.length);
      return;
    }

    let i = 0;
    const interval = setInterval(() => {
      setActiveStep(i);
      i++;
      if (i > steps.length) clearInterval(interval);
    }, 600); // speed control

    return () => clearInterval(interval);
  }, [loading]);

  return (
    <div className="mt-6 w-full">
      <div className="bg-white/5 border border-white/10 rounded-xl p-4">

        <h3 className="text-xs sm:text-sm text-gray-400 mb-3">
          Processing Pipeline
        </h3>

        <div className="space-y-2">
          {steps.map((step, i) => {
            let status = "idle";

            if (i < activeStep) status = "done";
            else if (i === activeStep) status = "loading";

            return (
              <div key={i} className="flex items-center gap-3 text-xs sm:text-sm">

                {/* ICON */}
                {status === "done" && (
                  <span className="text-green-400">✔</span>
                )}

                {status === "loading" && (
                  <span className="w-2 h-2 bg-yellow-400 rounded-full animate-pulse"></span>
                )}

                {status === "idle" && (
                  <span className="w-2 h-2 bg-gray-600 rounded-full"></span>
                )}

                <span className="text-gray-300">{step}</span>

              </div>
            );
          })}
        </div>

      </div>
    </div>
  );
}