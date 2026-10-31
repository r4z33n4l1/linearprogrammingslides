import { type ReactNode } from "react";
import styles from "./slide-frame.module.css";

export function SlideFrame({
  number,
  total,
  children,
}: {
  number: number;
  total: number;
  children: ReactNode;
}) {
  return (
    <div className={styles.frame}>
      <div className={styles.inner}>{children}</div>
      <span className={styles.slideNumber}>
        {String(number).padStart(2, "0")} / {String(total).padStart(2, "0")}
      </span>
    </div>
  );
}
