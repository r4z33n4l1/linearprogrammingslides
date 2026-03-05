export function DualityVisual() {
  return (
    <video
      src="/animations/duality.mp4"
      autoPlay
      loop
      muted
      playsInline
      style={{ width: "100%", height: "100%", objectFit: "contain", borderRadius: 8 }}
    />
  );
}
