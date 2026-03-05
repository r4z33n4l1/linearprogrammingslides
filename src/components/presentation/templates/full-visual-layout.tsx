import type { FullVisualSlide } from "@/src/content/linear-programming-deck";
import { SlideVisual } from "../visuals/visual-registry";
import styles from "./full-visual-layout.module.css";

export function FullVisualLayout({
  data,
  revealStep = 0,
}: {
  data: FullVisualSlide;
  revealStep?: number;
}) {
  return (
    <div className={styles.wrap}>
      <h2 className={styles.title}>{data.title}</h2>
      <div className={styles.visual}>
        <SlideVisual id={data.visualId} revealStep={revealStep} />
      </div>
      {data.caption && <p className={styles.caption}>{data.caption}</p>}
    </div>
  );
}
