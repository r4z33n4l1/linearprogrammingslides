export function LevelSetVisual() {
  return (
    <video
      src="/animations/level-set.mp4"
      autoPlay
      loop
      muted
      playsInline
      style={{ width: "100%", height: "100%", objectFit: "contain", borderRadius: 8 }}
    />
  );
}
