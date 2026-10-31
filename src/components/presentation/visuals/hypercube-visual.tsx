export function HypercubeVisual() {
  return (
    <video
      src="/animations/simplex-path.mp4"
      autoPlay
      loop
      muted
      playsInline
      style={{ width: "100%", height: "100%", objectFit: "contain", borderRadius: 8 }}
    />
  );
}
