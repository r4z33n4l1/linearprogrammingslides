import type { MathSlide } from "@/src/content/linear-programming-deck";
import styles from "./math-layout.module.css";

export function MathLayout({
  data,
  revealStep = 0,
}: {
  data: MathSlide;
  revealStep?: number;
}) {
  return (
    <div className={styles.wrap}>
      <h2 className={styles.title}>{data.title}</h2>
      {data.subtitle && <p className={styles.subtitle}>{data.subtitle}</p>}
      <div className={styles.rows}>
        {data.rows.map((r) => {
          const hidden = (r.step ?? 0) > revealStep;
          return (
            <div
              key={r.equation}
              className={`${styles.row} ${hidden ? styles.hidden : styles.revealed}`}
            >
              <span className={styles.equation}>{r.equation}</span>
              <span className={styles.arrow}>&rarr;</span>
              <span className={styles.annotation}>{r.annotation}</span>
            </div>
          );
        })}
      </div>
      {data.footer && <p className={styles.footer}>{data.footer}</p>}
    </div>
  );
}
