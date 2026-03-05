import type { AgendaSlide } from "@/src/content/linear-programming-deck";
import styles from "./agenda-layout.module.css";

export function AgendaLayout({ data }: { data: AgendaSlide }) {
  return (
    <div className={styles.wrap}>
      <h2 className={styles.heading}>{data.title}</h2>
      <ol className={styles.list}>
        {data.items.map((item, i) => (
          <li key={item} className={styles.item}>
            <span className={styles.index}>{i + 1}.</span>
            <span>{item}</span>
          </li>
        ))}
      </ol>
    </div>
  );
}
