export default function Hero() {
  return (
    <section className="text-center mt-24">

      <h1 className="text-6xl font-bold tracking-tight">
        <span className="text-white">Lexi</span>
        <span className="bg-gradient-to-r from-blue-400 to-blue-600 text-transparent bg-clip-text">
          Audit
        </span>
      </h1>

      <p className="text-gray-400 mt-6 max-w-xl mx-auto text-lg">
        AI-powered contract intelligence system that extracts insights,
        detects risks, and simplifies legal documents instantly.
      </p>

      <button className="mt-8 px-8 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 transition shadow-lg shadow-blue-500/30">
        Analyze Contract
      </button>

    </section>
  );
}