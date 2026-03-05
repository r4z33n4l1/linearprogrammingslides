"use client";

import { useEffect, useRef } from "react";

export function BakeryIconVisual({ revealStep = 999 }: { revealStep?: number }) {
  const showCroissant = revealStep >= 1;
  const showMuffin = revealStep >= 2;
  const showPrices = revealStep >= 3;

  const fade = (visible: boolean): React.CSSProperties => ({
    opacity: visible ? 1 : 0,
    transition: "opacity 0.35s ease",
  });

  return (
    <div style={{ display: "flex", flexDirection: "row", alignItems: "center", justifyContent: "center", gap: 32, width: "100%", minHeight: 260 }}>
      {/* Croissant */}
      <div style={{ position: "relative", ...fade(showCroissant) }}>
        <BouncingWrapper active={showCroissant} delay={0}>
          <img
            src="/1.png"
            alt="Croissant"
            style={{ width: 160, height: "auto", objectFit: "contain" }}
          />
        </BouncingWrapper>
        <div style={{
          position: "absolute",
          top: -8,
          right: -12,
          background: "#0f766e",
          color: "white",
          fontWeight: 700,
          fontSize: 15,
          borderRadius: 6,
          padding: "3px 10px",
          ...fade(showPrices),
        }}>
          $3
        </div>
      </div>

      {/* Muffin */}
      <div style={{ position: "relative", ...fade(showMuffin) }}>
        <BouncingWrapper active={showMuffin} delay={0.35}>
          <img
            src="/2.png"
            alt="Muffin"
            style={{ width: 160, height: "auto", objectFit: "contain" }}
          />
        </BouncingWrapper>
        <div style={{
          position: "absolute",
          top: -8,
          right: -12,
          background: "#0f766e",
          color: "white",
          fontWeight: 700,
          fontSize: 15,
          borderRadius: 6,
          padding: "3px 10px",
          ...fade(showPrices),
        }}>
          $4
        </div>
      </div>

      <style>{`
        @keyframes gentleBounce {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-12px); }
        }
      `}</style>
    </div>
  );
}

function BouncingWrapper({
  active,
  delay,
  children,
}: {
  active: boolean;
  delay: number;
  children: React.ReactNode;
}) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    if (active) {
      ref.current.style.animation = `gentleBounce 2s ease-in-out ${delay}s infinite`;
    } else {
      ref.current.style.animation = "none";
    }
  }, [active, delay]);

  return <div ref={ref}>{children}</div>;
}
