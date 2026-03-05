export function BakeryGridVisual() {
  const ox = 40, oy = 260, w = 220, h = 220;
  const steps = 5;
  const mapX = (v: number) => ox + (v / 50) * w;
  const mapY = (v: number) => oy - (v / 50) * h;

  return (
    <svg viewBox="0 0 310 300" width="100%" xmlns="http://www.w3.org/2000/svg">
      {/* Grid lines */}
      {Array.from({ length: steps + 1 }).map((_, i) => {
        const x = ox + (w / steps) * i;
        const y = oy - (h / steps) * i;
        return (
          <g key={i}>
            <line x1={x} y1={oy} x2={x} y2={oy - h} stroke="#e2e8f0" strokeWidth="1" />
            <line x1={ox} y1={y} x2={ox + w} y2={y} stroke="#e2e8f0" strokeWidth="1" />
            <text x={x} y={oy + 16} fontSize="10" textAnchor="middle" fill="#94a3b8">
              {i * 10}
            </text>
            <text x={ox - 8} y={y + 4} fontSize="10" textAnchor="end" fill="#94a3b8">
              {i * 10}
            </text>
          </g>
        );
      })}

      {/* Axes */}
      <line x1={ox} y1={oy} x2={ox + w + 10} y2={oy} stroke="#475569" strokeWidth="1.5" />
      <line x1={ox} y1={oy} x2={ox} y2={oy - h - 10} stroke="#475569" strokeWidth="1.5" />

      {/* Feasible region */}
      <polygon
        points={`${mapX(0)},${mapY(0)} ${mapX(26.67)},${mapY(0)} ${mapX(15)},${mapY(17.5)} ${mapX(0)},${mapY(25)}`}
        fill="rgba(20,184,166,0.18)"
        stroke="#0f766e"
        strokeWidth="2"
      />

      {/* Constraint lines */}
      {/* Flour: 2x+3y=100 → (0,33.3) to (50,0) */}
      <line x1={mapX(0)} y1={mapY(33.3)} x2={mapX(50)} y2={mapY(0)} stroke="#ea580c" strokeWidth="2" opacity="0.5" strokeDasharray="6 3" />
      {/* Sugar: x+2y=50 → (0,25) to (50,0) */}
      <line x1={mapX(0)} y1={mapY(25)} x2={mapX(50)} y2={mapY(0)} stroke="#2563eb" strokeWidth="2" />
      {/* Labor: 3x+2y=80 → (0,40) to (26.67,0) */}
      <line x1={mapX(0)} y1={mapY(40)} x2={mapX(26.67)} y2={mapY(0)} stroke="#16a34a" strokeWidth="2" />

      {/* Vertices */}
      {[
        { x: 0, y: 0 },
        { x: 0, y: 25 },
        { x: 15, y: 17.5 },
        { x: 26.67, y: 0 },
      ].map((v) => (
        <circle key={`${v.x}-${v.y}`} cx={mapX(v.x)} cy={mapY(v.y)} r="4" fill="#0f766e" />
      ))}

      {/* Legend */}
      <g transform="translate(170, 36)">
        <line x1="0" y1="0" x2="16" y2="0" stroke="#ea580c" strokeWidth="2" strokeDasharray="4 2" opacity="0.5" />
        <text x="22" y="4" fontSize="9" fill="#64748b">Flour</text>
        <line x1="0" y1="14" x2="16" y2="14" stroke="#2563eb" strokeWidth="2" />
        <text x="22" y="18" fontSize="9" fill="#64748b">Sugar</text>
        <line x1="0" y1="28" x2="16" y2="28" stroke="#16a34a" strokeWidth="2" />
        <text x="22" y="32" fontSize="9" fill="#64748b">Labor</text>
      </g>

      {/* Labels */}
      <text x={ox + w / 2} y={oy + 34} fontSize="13" textAnchor="middle" fill="#475569" fontWeight="600">
        Croissants (x)
      </text>
      <text
        x={ox - 30} y={oy - h / 2}
        fontSize="13" textAnchor="middle" fill="#475569" fontWeight="600"
        transform={`rotate(-90, ${ox - 30}, ${oy - h / 2})`}
      >
        Muffins (y)
      </text>
    </svg>
  );
}
