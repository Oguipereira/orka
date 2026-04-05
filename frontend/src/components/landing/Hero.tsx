"use client";
import { useState } from "react";
import Link from "next/link";
import { ArrowRight, Star } from "lucide-react";

const AVATARS = ["#7C3AED","#3B82F6","#06B6D4","#8B5CF6"];

export default function Hero() {
  const [email, setEmail] = useState("");

  return (
    <section style={{
      minHeight: "100vh",
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
      textAlign: "center",
      padding: "120px 24px 80px",
      position: "relative",
      overflow: "hidden",
      background: "var(--lp-bg)",
    }}>
      {/* Light rays */}
      <div style={{
        position: "absolute", top: -100, left: -200, width: 700, height: 900,
        background: "radial-gradient(ellipse, rgba(124,58,237,0.22) 0%, transparent 65%)",
        transform: "rotate(-30deg)", pointerEvents: "none",
      }} />
      <div style={{
        position: "absolute", top: -100, right: -200, width: 700, height: 900,
        background: "radial-gradient(ellipse, rgba(139,92,246,0.18) 0%, transparent 65%)",
        transform: "rotate(30deg)", pointerEvents: "none",
      }} />
      <div style={{
        position: "absolute", bottom: 0, left: "50%", transform: "translateX(-50%)",
        width: 800, height: 400,
        background: "radial-gradient(ellipse, rgba(59,130,246,0.08) 0%, transparent 70%)",
        pointerEvents: "none",
      }} />

      {/* Badge */}
      <div className="lp-animate lp-d1" style={{
        display: "inline-flex", alignItems: "center", gap: 8,
        background: "rgba(124,58,237,0.1)", border: "1px solid rgba(124,58,237,0.25)",
        borderRadius: 99, padding: "6px 14px", marginBottom: 32,
      }}>
        <span className="pulse-dot" />
        <span style={{ fontSize: 13, color: "var(--lp-muted)", fontWeight: 500 }}>
          Early Access — Conecte seu e-commerce hoje
        </span>
      </div>

      {/* Headline */}
      <h1 className="lp-animate lp-d2" style={{
        fontFamily: "var(--font-display)",
        fontSize: "clamp(52px, 8vw, 88px)",
        fontWeight: 800,
        lineHeight: 1.05,
        letterSpacing: "-2px",
        color: "var(--lp-text)",
        marginBottom: 28,
        maxWidth: 800,
      }}>
        Seu Negócio.<br />
        Seus Dados.<br />
        <span className="lp-grad-text">Uma IA Decidindo.</span>
      </h1>

      {/* Sub */}
      <p className="lp-animate lp-d3" style={{
        fontSize: "clamp(16px, 2vw, 20px)",
        color: "var(--lp-muted)",
        lineHeight: 1.7,
        maxWidth: 540,
        marginBottom: 44,
      }}>
        Conecte Mercado Livre, Amazon e Shopify.<br />
        A Orka analisa tudo e entrega decisões prontas —<br />
        sem dashboards complicados.
      </p>

      {/* CTA */}
      <div className="lp-animate lp-d4" style={{
        display: "flex", gap: 8, flexWrap: "wrap", justifyContent: "center",
        marginBottom: 24, width: "100%", maxWidth: 520,
      }}>
        <input
          type="email"
          placeholder="✉ Digite seu melhor e-mail..."
          value={email}
          onChange={e => setEmail(e.target.value)}
          style={{
            flex: 1, minWidth: 220,
            background: "rgba(13,13,26,0.8)",
            border: "1px solid rgba(124,58,237,0.3)",
            borderRadius: 10, padding: "12px 16px",
            fontSize: 14, color: "var(--lp-text)",
            outline: "none", fontFamily: "inherit",
          }}
          onFocus={e => (e.currentTarget.style.borderColor = "rgba(124,58,237,0.7)")}
          onBlur={e => (e.currentTarget.style.borderColor = "rgba(124,58,237,0.3)")}
        />
        <Link href={`/register${email ? `?email=${encodeURIComponent(email)}` : ""}`}>
          <button className="lp-btn" style={{ padding: "12px 24px" }}>
            Começar grátis 14 dias <ArrowRight size={15} />
          </button>
        </Link>
      </div>

      {/* Social proof */}
      <div className="lp-animate lp-d5" style={{
        display: "flex", alignItems: "center", gap: 12, justifyContent: "center", flexWrap: "wrap",
      }}>
        <div style={{ display: "flex" }}>
          {AVATARS.map((c, i) => (
            <div key={i} style={{
              width: 28, height: 28, borderRadius: "50%",
              background: c, border: "2px solid var(--lp-bg)",
              marginLeft: i > 0 ? -8 : 0,
              display: "flex", alignItems: "center", justifyContent: "center",
              fontSize: 11, fontWeight: 700, color: "#fff",
            }}>
              {["M","A","S","R"][i]}
            </div>
          ))}
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 4 }}>
          {[1,2,3,4,5].map(i => <Star key={i} size={12} fill="#FFB547" color="#FFB547" />)}
        </div>
        <span style={{ fontSize: 13, color: "var(--lp-muted)" }}>
          <strong style={{ color: "var(--lp-text)" }}>200+</strong> lojas conectadas · Sem cartão de crédito
        </span>
      </div>
    </section>
  );
}
