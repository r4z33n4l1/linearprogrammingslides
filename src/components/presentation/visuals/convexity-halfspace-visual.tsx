import { useEffect, useRef } from "react";

export function ConvexityHalfspaceVisual({ revealStep = 999 }: { revealStep?: number }) {
  const convexRef = useRef<HTMLVideoElement>(null);
  const halfspaceRef = useRef<HTMLVideoElement>(null);

  const showConvex = revealStep >= 1;
  const showHalfspace = revealStep >= 4;

  useEffect(() => {
    const v = convexRef.current;
    if (!v) return;
    if (showConvex) {
      v.play().catch(() => {});
    } else {
      v.pause();
      v.currentTime = 0;
    }
  }, [showConvex]);

  useEffect(() => {
    const v = halfspaceRef.current;
    if (!v) return;
    if (showHalfspace) {
      v.currentTime = 0;
      v.play().catch(() => {});
    } else {
      v.pause();
      v.currentTime = 0;
    }
  }, [showHalfspace]);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 12, width: "100%" }}>
      <video
        ref={convexRef}
        src="/animations/convexity.mp4"
        loop
        muted
        playsInline
        style={{
          width: "100%",
          objectFit: "contain",
          borderRadius: 8,
          opacity: showConvex ? 1 : 0,
          transition: "opacity 0.4s ease",
          maxHeight: 220,
        }}
      />
      <video
        ref={halfspaceRef}
        src="/animations/halfspace.mp4"
        loop
        muted
        playsInline
        style={{
          width: "100%",
          objectFit: "contain",
          borderRadius: 8,
          opacity: showHalfspace ? 1 : 0,
          transition: "opacity 0.4s ease",
          maxHeight: 220,
        }}
      />
    </div>
  );
}
