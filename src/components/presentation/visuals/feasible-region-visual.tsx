import { useEffect, useRef } from "react";

export function FeasibleRegionVisual({ revealStep = 0 }: { revealStep?: number }) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const showStill = revealStep >= 1;

  useEffect(() => {
    const v = videoRef.current;
    if (!v) return;
    if (showStill) {
      v.pause();
    } else {
      v.currentTime = 0;
      v.play().catch(() => {});
    }
  }, [showStill]);

  return (
    <div style={{ position: "relative", width: "100%", height: "100%" }}>
      <video
        ref={videoRef}
        src="/animations/bakery-feasible-region.mp4"
        autoPlay
        muted
        playsInline
        style={{
          width: "100%",
          height: "100%",
          objectFit: "contain",
          borderRadius: 8,
          opacity: showStill ? 0 : 1,
          transition: "opacity 0.3s ease",
        }}
      />
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src="/animations/bakery-feasible-region-final.png"
        alt="Feasible region with vertices"
        style={{
          position: "absolute",
          inset: 0,
          width: "100%",
          height: "100%",
          objectFit: "contain",
          borderRadius: 8,
          opacity: showStill ? 1 : 0,
          transition: "opacity 0.3s ease",
        }}
      />
    </div>
  );
}
