export function BigPictureVisual({ revealStep = 0 }: { revealStep?: number }) {
  const fade = (step: number) => ({
    opacity: revealStep >= step ? 1 : 0,
    transition: "opacity 0.5s ease",
  });

  return (
    <svg viewBox="0 0 280 420" width="100%" xmlns="http://www.w3.org/2000/svg">
      {/* Step 1: Constraints — parallel lines */}
      <g style={fade(1)}>
        <rect x="90" y="10" width="100" height="70" rx="14" fill="rgba(234,88,12,0.08)" stroke="#ea580c" strokeWidth="1.5" />
        <line x1="110" y1="28" x2="170" y2="28" stroke="#ea580c" strokeWidth="2" />
        <line x1="115" y1="40" x2="175" y2="40" stroke="#0284c7" strokeWidth="2" />
        <line x1="108" y1="52" x2="168" y2="52" stroke="#16a34a" strokeWidth="2" />
        <line x1="120" y1="64" x2="160" y2="64" stroke="#94a3b8" strokeWidth="1.5" strokeDasharray="4 3" />
        <text x="140" y="96" textAnchor="middle" fontSize="11" fontWeight="600" fill="#334155">Constraints</text>
      </g>

      {/* Arrow 1→2 */}
      <g style={fade(1)}>
        <line x1="140" y1="100" x2="140" y2="126" stroke="#94a3b8" strokeWidth="1.5" />
        <polygon points="135,122 140,132 145,122" fill="#94a3b8" />
      </g>

      {/* Step 2: Convex polyhedron */}
      <g style={fade(2)}>
        <polygon
          points="105,155 140,138 175,148 182,180 155,200 118,195"
          fill="rgba(20,184,166,0.15)"
          stroke="#0f766e"
          strokeWidth="2"
        />
        <text x="140" y="222" textAnchor="middle" fontSize="11" fontWeight="600" fill="#334155">Convex Polyhedron</text>
      </g>

      {/* Arrow 2→3 */}
      <g style={fade(2)}>
        <line x1="140" y1="228" x2="140" y2="254" stroke="#94a3b8" strokeWidth="1.5" />
        <polygon points="135,250 140,260 145,250" fill="#94a3b8" />
      </g>

      {/* Step 3: Finite vertices — polygon with highlighted corners */}
      <g style={fade(3)}>
        <polygon
          points="105,280 140,265 175,275 182,305 155,322 118,318"
          fill="rgba(20,184,166,0.08)"
          stroke="#0f766e"
          strokeWidth="1.5"
          strokeDasharray="6 3"
        />
        {/* Vertex dots */}
        {[
          [105, 280], [140, 265], [175, 275],
          [182, 305], [155, 322], [118, 318],
        ].map(([cx, cy]) => (
          <circle key={`${cx}-${cy}`} cx={cx} cy={cy} r="5" fill="#f59e0b" stroke="#d97706" strokeWidth="1.5" />
        ))}
        <text x="140" y="345" textAnchor="middle" fontSize="11" fontWeight="600" fill="#334155">Finitely Many Vertices</text>
      </g>

      {/* Arrow 3→4 */}
      <g style={fade(3)}>
        <line x1="140" y1="350" x2="140" y2="374" stroke="#94a3b8" strokeWidth="1.5" />
        <polygon points="135,370 140,380 145,370" fill="#94a3b8" />
      </g>

      {/* Step 4: Optimum at vertex — star burst */}
      <g style={fade(4)}>
        <circle cx="140" cy="398" r="16" fill="rgba(251,191,36,0.25)" stroke="#f59e0b" strokeWidth="2" />
        <circle cx="140" cy="398" r="6" fill="#f59e0b" />
        {/* Rays */}
        {[0, 45, 90, 135, 180, 225, 270, 315].map((deg) => {
          const r1 = 18, r2 = 26;
          const rad = (deg * Math.PI) / 180;
          return (
            <line
              key={deg}
              x1={140 + r1 * Math.cos(rad)}
              y1={398 + r1 * Math.sin(rad)}
              x2={140 + r2 * Math.cos(rad)}
              y2={398 + r2 * Math.sin(rad)}
              stroke="#f59e0b"
              strokeWidth="1.5"
              opacity="0.5"
            />
          );
        })}
        <text x="195" y="402" fontSize="11" fontWeight="700" fill="#b45309">Optimum!</text>
      </g>
    </svg>
  );
}
