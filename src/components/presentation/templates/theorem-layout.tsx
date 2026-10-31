import type { TheoremSlide } from "@/src/content/linear-programming-deck";
import styles from "./theorem-layout.module.css";

export function TheoremLayout({
  data,
  revealStep = 0,
}: {
  data: TheoremSlide;
  revealStep?: number;
}) {
  return (
    <div className={styles.wrap}>
      <p className={styles.label}>{data.label}</p>
      <h2 className={styles.title}>{data.title}</h2>
      <div className={styles.box}>
        <p className={styles.statement}>{data.statement}</p>
      </div>
      {data.notes && data.notes.length > 0 && (
        <ul className={styles.notes}>
          {data.notes.map((n) => {
            const hidden = (n.step ?? 0) > revealStep;
            return (
              <li
                key={n.text}
                className={`${styles.note} ${hidden ? styles.hidden : styles.revealed}`}
                style={{ fontWeight: n.bold ? 700 : undefined }}
              >
                {n.text}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
