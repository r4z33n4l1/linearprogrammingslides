export function VerticesVisual() {
  const ox = 50, oy = 270, s = 50;

  return (
    <svg viewBox="0 0 350 320" width="100%" xmlns="http://www.w3.org/2000/svg">
      {/* Axes */}
      <line x1={ox} y1={oy} x2="310" y2={oy} stroke="#94a3b8" strokeWidth="1" />
      <line x1={ox} y1={oy} x2={ox} y2="20" stroke="#94a3b8" strokeWidth="1" />

      {/* Feasible polygon */}
      <polygon
        points={`${ox},${oy} ${ox + 2.5 * s},${oy} ${ox + 1 * s},${oy - 3 * s} ${ox},${oy - 4 * s}`}
        fill="rgba(20,184,166,0.15)"
        stroke="#0f766e"
        strokeWidth="2"
      />

      {/* Vertex highlights (gold) */}
      {[
        [0, 0], [2.5, 0], [1, 3], [0, 4],
      ].map(([x, y]) => (
        <g key={`v${x}-${y}`}>
          <circle cx={ox + x * s} cy={oy - y * s} r="10" fill="rgba(251,191,36,0.3)" stroke="#f59e0b" strokeWidth="2" />
          <circle cx={ox + x * s} cy={oy - y * s} r="4" fill="#f59e0b" />
        </g>
      ))}

      {/* Edge midpoint (hollow, showing it's NOT a vertex) */}
      <circle
        cx={ox + 1.75 * s}
        cy={oy - 1.5 * s}
        r="6"
        fill="none"
        stroke="#94a3b8"
        strokeWidth="2"
        strokeDasharray="3 3"
      />
      <text
        x={ox + 1.75 * s + 14}
        y={oy - 1.5 * s + 4}
        fontSize="10"
        fill="#64748b"
      >
        midpoint
      </text>
    </svg>
  );
}
