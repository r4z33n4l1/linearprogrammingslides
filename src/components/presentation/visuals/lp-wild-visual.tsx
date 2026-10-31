export function LPWildVisual() {
  return (
    <svg viewBox="0 0 300 320" width="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#bae6fd" stopOpacity="0.3" />
          <stop offset="100%" stopColor="#e0f2fe" stopOpacity="0.1" />
        </linearGradient>
      </defs>

      {/* ── Airplane (Airlines) ── */}
      <g transform="translate(150, 60)">
        <circle r="42" fill="url(#skyGrad)" stroke="#bae6fd" strokeWidth="1" />
        {/* Fuselage */}
        <path d="M -22 2 L 22 2 L 26 0 L 22 -2 L -22 -2 L -26 0 Z" fill="#0284c7" />
        {/* Wings */}
        <path d="M -4 -2 L 2 -18 L 10 -18 L 6 -2 Z" fill="#0284c7" opacity="0.8" />
        <path d="M -4 2 L 2 18 L 10 18 L 6 2 Z" fill="#0284c7" opacity="0.8" />
        {/* Tail */}
        <path d="M -22 -2 L -26 -10 L -18 -10 L -18 -2 Z" fill="#0284c7" opacity="0.7" />
        {/* Engine glow */}
        <ellipse cx="-28" cy="0" rx="4" ry="1.5" fill="#7dd3fc" opacity="0.6" />
        {/* Route dots */}
        <circle cx="-36" cy="-14" r="2" fill="#0ea5e9" opacity="0.5" />
        <circle cx="34" cy="12" r="2" fill="#0ea5e9" opacity="0.5" />
        <line x1="-34" y1="-13" x2="32" y2="11" stroke="#0ea5e9" strokeWidth="0.8" strokeDasharray="3 2" opacity="0.35" />
      </g>
      <text x="150" y="118" textAnchor="middle" fontSize="12" fontWeight="600" fill="#0284c7">Airlines</text>

      {/* ── Package/Truck (Logistics) ── */}
      <g transform="translate(60, 195)">
        <circle r="42" fill="rgba(234,88,12,0.08)" stroke="#fed7aa" strokeWidth="1" />
        {/* Package box */}
        <rect x="-16" y="-18" width="24" height="20" rx="2" fill="#ea580c" opacity="0.85" />
        <line x1="-4" y1="-18" x2="-4" y2="2" stroke="#fdba74" strokeWidth="1" />
        <line x1="-16" y1="-8" x2="8" y2="-8" stroke="#fdba74" strokeWidth="1" />
        {/* Tape */}
        <rect x="-8" y="-12" width="8" height="3" rx="0.5" fill="#fdba74" opacity="0.6" />
        {/* Arrow (delivery) */}
        <path d="M 12 -6 L 24 -6 L 24 -10 L 32 -2 L 24 6 L 24 2 L 12 2 Z" fill="#ea580c" opacity="0.5" />
        {/* Network dots */}
        <circle cx="-30" cy="16" r="2.5" fill="#fb923c" opacity="0.4" />
        <circle cx="-18" cy="24" r="2.5" fill="#fb923c" opacity="0.4" />
        <circle cx="20" cy="20" r="2.5" fill="#fb923c" opacity="0.4" />
        <line x1="-28" y1="17" x2="-19" y2="23" stroke="#fb923c" strokeWidth="0.8" opacity="0.3" />
        <line x1="-17" y1="24" x2="18" y2="21" stroke="#fb923c" strokeWidth="0.8" opacity="0.3" />
      </g>
      <text x="60" y="253" textAnchor="middle" fontSize="12" fontWeight="600" fill="#ea580c">Logistics</text>

      {/* ── Power Grid (Energy) ── */}
      <g transform="translate(240, 195)">
        <circle r="42" fill="rgba(22,163,74,0.08)" stroke="#bbf7d0" strokeWidth="1" />
        {/* Transmission tower (simplified) */}
        <line x1="0" y1="-24" x2="0" y2="12" stroke="#16a34a" strokeWidth="2" />
        <line x1="-12" y1="-14" x2="12" y2="-14" stroke="#16a34a" strokeWidth="1.5" />
        <line x1="-8" y1="-6" x2="8" y2="-6" stroke="#16a34a" strokeWidth="1.5" />
        {/* Cross beams */}
        <line x1="-4" y1="-14" x2="4" y2="-6" stroke="#16a34a" strokeWidth="0.8" opacity="0.6" />
        <line x1="4" y1="-14" x2="-4" y2="-6" stroke="#16a34a" strokeWidth="0.8" opacity="0.6" />
        {/* Base */}
        <line x1="-8" y1="12" x2="0" y2="4" stroke="#16a34a" strokeWidth="1.5" />
        <line x1="8" y1="12" x2="0" y2="4" stroke="#16a34a" strokeWidth="1.5" />
        {/* Power lines */}
        <path d="M -12 -14 Q -24 -10, -30 -16" fill="none" stroke="#16a34a" strokeWidth="1" opacity="0.5" />
        <path d="M 12 -14 Q 24 -10, 30 -16" fill="none" stroke="#16a34a" strokeWidth="1" opacity="0.5" />
        {/* Lightning bolt */}
        <path d="M -2 -30 L 1 -24 L -1 -24 L 2 -18" fill="none" stroke="#eab308" strokeWidth="1.5" strokeLinecap="round" />
        {/* Wind turbine (small) */}
        <g transform="translate(-26, 8)">
          <line x1="0" y1="0" x2="0" y2="16" stroke="#22c55e" strokeWidth="1" />
          <path d="M 0 0 L -1 -8 L 1 -8 Z" fill="#22c55e" opacity="0.7" />
          <path d="M 0 0 L 7 4 L 6 6 Z" fill="#22c55e" opacity="0.7" />
          <path d="M 0 0 L -6 5 L -7 3 Z" fill="#22c55e" opacity="0.7" />
        </g>
      </g>
      <text x="240" y="253" textAnchor="middle" fontSize="12" fontWeight="600" fill="#16a34a">Power Grids</text>

      {/* Connecting arcs (showing LP connects them all) */}
      <path d="M 105 85 Q 60 130, 75 160" fill="none" stroke="#94a3b8" strokeWidth="0.8" strokeDasharray="4 3" opacity="0.4" />
      <path d="M 195 85 Q 240 130, 225 160" fill="none" stroke="#94a3b8" strokeWidth="0.8" strokeDasharray="4 3" opacity="0.4" />
      <path d="M 105 210 Q 150 240, 195 210" fill="none" stroke="#94a3b8" strokeWidth="0.8" strokeDasharray="4 3" opacity="0.4" />

      {/* Center label */}
      <text x="150" y="290" textAnchor="middle" fontSize="10" fill="#64748b" fontStyle="italic">
        Millions of LPs solved daily
      </text>
    </svg>
  );
}
