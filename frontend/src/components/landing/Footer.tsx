"use client";
import Link from "next/link";
import { GitBranch } from "lucide-react";

export default function Footer() {
  return (
    <footer style={{
      padding: "64px 48px 40px",
      background: "var(--lp-bg)",
      borderTop: "1px solid var(--lp-border)",
    }}>
      <div style={{ maxWidth: 1060, margin: "0 auto" }}>
        <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr 1fr 1fr", gap: 40, marginBottom: 56 }}>
          {/* Brand */}
          <div>
            <p style={{ fontFamily: "var(--font-display)", fontSize: 22, fontWeight: 800, color: "var(--lp-text)", marginBottom: 12 }}>
              orka<span style={{ color: "var(--lp-purple)" }}>.</span>
            </p>
            <p style={{ fontSize: 14, color: "var(--lp-muted)", lineHeight: 1.7, maxWidth: 260, marginBottom: 20 }}>
              Inteligência artificial para lojistas que querem tomar melhores decisões, mais rápido.
            </p>
            <a
              href="https://github.com/reidascabritas/orka"
              target="_blank"
              rel="noopener noreferrer"
              style={{
                display: "inline-flex", alignItems: "center", gap: 8,
                fontSize: 13, color: "var(--lp-muted)", textDecoration: "none",
                border: "1px solid var(--lp-border)", borderRadius: 8, padding: "8px 14px",
                transition: "all 0.2s",
              }}
              onMouseEnter={e => { (e.currentTarget as HTMLAnchorElement).style.color = "#fff"; (e.currentTarget as HTMLAnchorElement).style.borderColor = "rgba(124,58,237,0.4)"; }}
              onMouseLeave={e => { (e.currentTarget as HTMLAnchorElement).style.color = "var(--lp-muted)"; (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--lp-border)"; }}
            >
              <GitBranch size={15} />
              reidascabritas/orka
            </a>
          </div>

          {/* Produto */}
          <div>
            <p style={{ fontSize: 12, fontWeight: 600, letterSpacing: 1.5, textTransform: "uppercase", color: "var(--lp-muted2)", marginBottom: 16 }}>Produto</p>
            {[
              { label: "Funcionalidades", href: "#features" },
              { label: "Como funciona", href: "#how-it-works" },
              { label: "Pricing", href: "#pricing" },
              { label: "Dashboard", href: "/register" },
            ].map(l => (
              <Link key={l.label} href={l.href} style={{ display: "block", fontSize: 14, color: "var(--lp-muted)", textDecoration: "none", marginBottom: 10, transition: "color 0.15s" }}
                onMouseEnter={e => (e.currentTarget.style.color = "#fff")}
                onMouseLeave={e => (e.currentTarget.style.color = "var(--lp-muted)")}
              >{l.label}</Link>
            ))}
          </div>

          {/* Empresa */}
          <div>
            <p style={{ fontSize: 12, fontWeight: 600, letterSpacing: 1.5, textTransform: "uppercase", color: "var(--lp-muted2)", marginBottom: 16 }}>Empresa</p>
            {[
              { label: "Build in Public", href: "/build-in-public" },
              { label: "GitHub", href: "https://github.com/reidascabritas/orka" },
            ].map(l => (
              <a key={l.label} href={l.href} target={l.href.startsWith("http") ? "_blank" : undefined} rel="noopener noreferrer"
                style={{ display: "block", fontSize: 14, color: "var(--lp-muted)", textDecoration: "none", marginBottom: 10, transition: "color 0.15s" }}
                onMouseEnter={e => (e.currentTarget.style.color = "#fff")}
                onMouseLeave={e => (e.currentTarget.style.color = "var(--lp-muted)")}
              >{l.label}</a>
            ))}
          </div>

          {/* Legal */}
          <div>
            <p style={{ fontSize: 12, fontWeight: 600, letterSpacing: 1.5, textTransform: "uppercase", color: "var(--lp-muted2)", marginBottom: 16 }}>Legal</p>
            {["Privacidade", "Termos de uso"].map(l => (
              <Link key={l} href="#" style={{ display: "block", fontSize: 14, color: "var(--lp-muted)", textDecoration: "none", marginBottom: 10, transition: "color 0.15s" }}
                onMouseEnter={e => (e.currentTarget.style.color = "#fff")}
                onMouseLeave={e => (e.currentTarget.style.color = "var(--lp-muted)")}
              >{l}</Link>
            ))}
          </div>
        </div>

        <div style={{ borderTop: "1px solid var(--lp-border)", paddingTop: 24, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <p style={{ fontSize: 13, color: "var(--lp-muted2)" }}>
            © 2025 Orka. Construído em público.
          </p>
          <p style={{ fontSize: 13, color: "var(--lp-muted2)" }}>
            Feito com <span style={{ color: "var(--lp-purple)" }}>♥</span> para lojistas brasileiros
          </p>
        </div>
      </div>
    </footer>
  );
}
