import { useEffect, useRef } from "react";

export function ConvexityVisual({ revealStep = 999 }: { revealStep?: number }) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const visible = revealStep >= 1;

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    if (visible) {
      video.play().catch(() => {});
    } else {
      video.pause();
      video.currentTime = 0;
    }
  }, [visible]);

  return (
    <video
      ref={videoRef}
      src="/animations/convexity.mp4"
      loop
      muted
      playsInline
      style={{
        width: "100%",
        height: "100%",
        objectFit: "contain",
        borderRadius: 8,
        opacity: visible ? 1 : 0,
        transition: "opacity 0.35s ease",
      }}
    />
  );
}
