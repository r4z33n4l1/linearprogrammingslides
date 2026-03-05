import type { ContentVisualSlide } from "@/src/content/linear-programming-deck";
import { SlideVisual } from "../visuals/visual-registry";
import styles from "./content-visual-layout.module.css";

export function ContentVisualLayout({
  data,
  revealStep = 0,
}: {
  data: ContentVisualSlide;
  revealStep?: number;
}) {
  const visualHidden =
    data.visualStep !== undefined && data.visualStep > revealStep;

  return (
    <div className={styles.wrap}>
      <div className={styles.text}>
        <h2 className={styles.title}>{data.title}</h2>
        {data.subtitle && <p className={styles.subtitle}>{data.subtitle}</p>}
        <ul className={styles.bullets}>
          {data.bullets.map((b) => {
            const hidden = (b.step ?? 0) > revealStep;
            return (
              <li
                key={b.text}
                className={`${styles.bullet} ${hidden ? styles.hidden : styles.revealed}`}
                style={{
                  color: b.color ?? undefined,
                  fontWeight: b.bold ? 700 : undefined,
                }}
              >
                {b.text}
              </li>
            );
          })}
        </ul>
        {data.footer && <p className={styles.footer}>{data.footer}</p>}
      </div>
      <div
        className={`${styles.visualPane} ${visualHidden ? styles.hidden : styles.revealed}`}
      >
        <SlideVisual id={data.visualId} revealStep={revealStep} />
      </div>
    </div>
  );
}
