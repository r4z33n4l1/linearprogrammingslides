import type { TitleSlide } from "@/src/content/linear-programming-deck";
import styles from "./title-layout.module.css";

export function TitleLayout({ data }: { data: TitleSlide }) {
  return (
    <div className={styles.wrap}>
      <h1 className={styles.title}>{data.title}</h1>
      <p className={styles.subtitle}>{data.subtitle}</p>
    </div>
  );
}
