export function ConstraintLinesVisual() {
  return (
    <svg viewBox="0 0 300 300" width="100%" xmlns="http://www.w3.org/2000/svg">
      {/* Axes */}
      <line x1="30" y1="270" x2="280" y2="270" stroke="#94a3b8" strokeWidth="1.5" />
      <line x1="30" y1="270" x2="30" y2="20" stroke="#94a3b8" strokeWidth="1.5" />

      {/* Constraint lines extending beyond visible */}
      <line x1="0" y1="220" x2="250" y2="30" stroke="#ea580c" strokeWidth="2" opacity="0.8" />
      <line x1="0" y1="100" x2="280" y2="240" stroke="#2563eb" strokeWidth="2" opacity="0.8" />
      <line x1="60" y1="10" x2="260" y2="260" stroke="#16a34a" strokeWidth="2" opacity="0.8" />
      <line x1="30" y1="40" x2="240" y2="40" stroke="#0891b2" strokeWidth="2" opacity="0.8" />

      {/* Feasible polygon */}
      <polygon
        points="80,180 120,100 180,80 200,140 140,200"
        fill="rgba(20,184,166,0.25)"
        stroke="#0f766e"
        strokeWidth="2"
      />

      {/* Vertices */}
      <circle cx="80" cy="180" r="5" fill="#0f766e" />
      <circle cx="120" cy="100" r="5" fill="#0f766e" />
      <circle cx="180" cy="80" r="5" fill="#0f766e" />
      <circle cx="200" cy="140" r="5" fill="#0f766e" />
      <circle cx="140" cy="200" r="5" fill="#0f766e" />
    </svg>
  );
}
