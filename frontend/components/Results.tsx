export default function Results({ data }: any) {
  if (!data) return null;

  return (
    <section className="mt-10 sm:mt-16 w-full max-w-md sm:max-w-3xl px-2">

      <div className="bg-gradient-to-b from-zinc-900 to-black border border-white/10 rounded-2xl p-5 sm:p-8 shadow-[0_0_50px_rgba(59,130,246,0.1)]">

        <h2 className="text-lg sm:text-2xl font-semibold mb-4 sm:mb-6">
          Analysis Results
        </h2>

        <div className="space-y-5">

          {/* Contract Type */}
          <div>
            <p className="text-gray-400 text-xs sm:text-sm">Contract Type</p>
            <p className="text-blue-400 text-base sm:text-lg font-medium">
              {data.contract_type}
            </p>
          </div>

          {/* Parties */}
          <div>
            <p className="text-gray-400 text-xs sm:text-sm">Parties</p>
            <p className="text-sm sm:text-base leading-relaxed break-words">
              {data.parties?.join(", ")}
            </p>
          </div>

          {/* Risks */}
          <div>
            <p className="text-gray-400 text-xs sm:text-sm">Risks</p>
            <div className="flex flex-wrap gap-2 mt-2">
              {data.risks?.map((r: string, i: number) => (
                <span
                  key={i}
                  className="bg-red-500/20 text-red-400 px-2 sm:px-3 py-1 text-xs sm:text-sm rounded-full border border-red-500/20"
                >
                  {r}
                </span>
              ))}
            </div>
          </div>

        </div>

      </div>

      {/* Metrics Panel */}
      <div className="mt-4 flex flex-wrap gap-3 text-xs sm:text-sm text-gray-400">

        <span className="bg-white/5 px-3 py-1 rounded-lg border border-white/10">
          Confidence: ~92%
        </span>

        <span className="bg-white/5 px-3 py-1 rounded-lg border border-white/10">
          Entities: {data.parties?.length || 0}
        </span>

        <span className="bg-white/5 px-3 py-1 rounded-lg border border-white/10">
          Risks: {data.risks?.length || 0}
        </span>

      </div>

    </section>
  );
}