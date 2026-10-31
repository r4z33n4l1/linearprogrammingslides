import type { TableSlide } from "@/src/content/linear-programming-deck";
import styles from "./table-layout.module.css";

export function TableLayout({ data }: { data: TableSlide }) {
  return (
    <div className={styles.wrap}>
      <h2 className={styles.title}>{data.title}</h2>
      <p className={styles.subtitle}>{data.subtitle}</p>
      <table className={styles.table}>
        <thead>
          <tr>
            {data.columns.map((col) => (
              <th key={col}>{col}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.rows.map((row, i) => (
            <tr key={i} className={row.highlight ? styles.highlight : undefined}>
              {row.cells.map((cell, j) => (
                <td key={j}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      {data.footer && <p className={styles.footer}>{data.footer}</p>}
    </div>
  );
}
