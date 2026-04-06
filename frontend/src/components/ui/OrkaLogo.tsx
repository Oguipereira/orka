export function OrkaLogo({ size = 36 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 120 120" fill="none">
      <defs>
        <linearGradient id="ol1" x1="0" y1="120" x2="120" y2="0">
          <stop offset="0%" stopColor="#4F8EF7"/>
          <stop offset="100%" stopColor="#9D7FF5"/>
        </linearGradient>
        <linearGradient id="ol2" x1="60" y1="40" x2="110" y2="0">
          <stop offset="0%" stopColor="#7B5CF0"/>
          <stop offset="100%" stopColor="#B59AF8"/>
        </linearGradient>
      </defs>
      <path d="M18 82Q12 58 28 38Q48 12 78 18Q106 24 112 52Q118 74 102 86Q84 100 58 97Q30 93 18 82Z" fill="url(#ol1)"/>
      <path d="M88 28Q106 12 118 8Q112 26 110 42Z" fill="url(#ol2)"/>
      <rect x="60" y="40" width="7" height="30" rx="3.5" fill="rgba(255,255,255,0.92)"/>
      <rect x="72" y="48" width="7" height="22" rx="3.5" fill="rgba(255,255,255,0.7)"/>
      <rect x="48" y="54" width="7" height="16" rx="3.5" fill="rgba(255,255,255,0.7)"/>
      <circle cx="36" cy="56" r="5.5" fill="rgba(255,255,255,0.88)"/>
    </svg>
  )
}
