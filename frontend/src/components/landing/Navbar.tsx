"use client";
import Link from "next/link";
import { useState } from "react";
import { ArrowRight } from "lucide-react";

const links = [
  { href: "#features",    label: "Features" },
  { href: "#integrations",label: "Integrações" },
  { href: "#pricing",     label: "Pricing" },
  { href: "/build-in-public", label: "Empresa" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <header style={{
      position: "fixed", top: 0, left: 0, right: 0, zIndex: 200,
    }}>
      <nav className="lp-glass" style={{
        display: "flex", alignItems: "center", justifyContent: "space-between",
        padding: "0 48px", height: 64, margin: "12px 24px", borderRadius: 14,
        maxWidth: 1100, marginLeft: "auto", marginRight: "auto",
      }}>
        {/* Logo */}
        <Link href="/" style={{ textDecoration: "none", display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ fontSize: 24, lineHeight: 1 }}>🐋</span>
          <span style={{ fontSize: 18, fontWeight: 700, color: "var(--lp-text)", fontFamily: "var(--font-display)" }}>
            Orka
          </span>
        </Link>

        {/* Desktop nav */}
        <div style={{ display: "flex", alignItems: "center", gap: 4 }}>
          {links.map(l => (
            <Link key={l.href} href={l.href} style={{
              fontSize: 14, color: "var(--lp-muted)", textDecoration: "none",
              padding: "6px 14px", borderRadius: 8, transition: "color 0.15s",
              fontWeight: 500,
            }}
            onMouseEnter={e => (e.currentTarget.style.color = "var(--lp-text)")}
            onMouseLeave={e => (e.currentTarget.style.color = "var(--lp-muted)")}
            >
              {l.label}
            </Link>
          ))}
        </div>

        {/* CTA */}
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <Link href="/login">
            <button style={{
              background: "transparent", border: "1px solid rgba(255,255,255,0.1)",
              color: "var(--lp-muted)", borderRadius: 8, padding: "7px 16px",
              fontSize: 14, cursor: "pointer", fontFamily: "inherit", fontWeight: 500,
              transition: "all 0.15s",
            }}
            onMouseEnter={e => { e.currentTarget.style.color = "var(--lp-text)"; e.currentTarget.style.borderColor = "rgba(255,255,255,0.2)"; }}
            onMouseLeave={e => { e.currentTarget.style.color = "var(--lp-muted)"; e.currentTarget.style.borderColor = "rgba(255,255,255,0.1)"; }}
            >
              Entrar
            </button>
          </Link>
          <Link href="/register">
            <button className="lp-btn lp-btn-sm" style={{ fontSize: 13, padding: "8px 16px" }}>
              Começar grátis <ArrowRight size={13} />
            </button>
          </Link>
        </div>
      </nav>
    </header>
  );
}
