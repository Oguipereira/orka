const PLATFORMS = [
  { name: "Mercado Livre", abbr: "ML" },
  { name: "Amazon",         abbr: "AMZ" },
  { name: "Shopify",        abbr: "SHOP" },
  { name: "WooCommerce",    abbr: "WOO" },
  { name: "Stripe",         abbr: "STR" },
];

export default function TrustedBy() {
  return (
    <section style={{
      padding: "56px 48px",
      background: "var(--lp-s1)",
      borderTop: "1px solid var(--lp-border)",
      borderBottom: "1px solid var(--lp-border)",
    }}>
      <div style={{ maxWidth: 900, margin: "0 auto", textAlign: "center" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 16, justifyContent: "center", marginBottom: 36 }}>
          <div style={{ flex: 1, height: 1, background: "var(--lp-border)" }} />
          <p style={{ fontSize: 12, color: "var(--lp-muted2)", fontWeight: 500, letterSpacing: 1, textTransform: "uppercase", whiteSpace: "nowrap" }}>
            Conecte com as maiores plataformas
          </p>
          <div style={{ flex: 1, height: 1, background: "var(--lp-border)" }} />
        </div>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 48, flexWrap: "wrap" }}>
          {PLATFORMS.map(p => (
            <div key={p.name} style={{ display: "flex", alignItems: "center", gap: 8, opacity: 0.45 }}>
              <div style={{
                width: 32, height: 32, borderRadius: 8,
                background: "rgba(255,255,255,0.08)",
                display: "flex", alignItems: "center", justifyContent: "center",
                fontSize: 10, fontWeight: 800, color: "#fff", letterSpacing: 0.5,
              }}>
                {p.abbr.slice(0, 2)}
              </div>
              <span style={{ fontSize: 15, fontWeight: 600, color: "#fff", fontFamily: "var(--font-display)" }}>
                {p.name}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
