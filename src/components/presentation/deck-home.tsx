import Link from "next/link";
import { presentationMeta, slides } from "@/src/content/linear-programming-deck";
import styles from "./presentation.module.css";

function slideTitle(slide: (typeof slides)[number]): string {
  const { data } = slide;
  if ("title" in data) return data.title.split("\n")[0];
  return `Slide ${slide.number}`;
}

export function DeckHome() {
  return (
    <main className={styles.page}>
      <div className={styles.home}>
        <section className={styles.hero}>
          <div className={`${styles.panel} ${styles.heroCopy}`}>
            <p className={styles.eyebrow}>{presentationMeta.course}</p>
            <h1 className={styles.heroTitle}>{presentationMeta.title}</h1>
            <p className={styles.heroBody}>
              A 14-slide presentation exploring how convexity and linearity
              reduce infinite optimization to a finite vertex search, culminating
              in the Fundamental Theorem of Linear Programming.
            </p>
            <div className={styles.heroActions}>
              <Link className={styles.primaryAction} href="/slides">
                Start Presentation
              </Link>
            </div>
          </div>

          <aside className={`${styles.panel} ${styles.metaGrid}`}>
            <div className={styles.metaRow}>
              <span className={styles.metaLabel}>Slides</span>
              <strong className={styles.metaValue}>{presentationMeta.totalSlides}</strong>
            </div>
            <div className={styles.metaRow}>
              <span className={styles.metaLabel}>Runtime</span>
              <strong className={styles.metaValue}>{presentationMeta.duration}</strong>
            </div>
            <div className={styles.metaRow}>
              <span className={styles.metaLabel}>Course</span>
              <strong className={styles.metaValue}>{presentationMeta.course}</strong>
            </div>
          </aside>
        </section>

        <section className={styles.slideGrid}>
          {slides.map((slide) => (
            <article className={`${styles.panel} ${styles.slideCard}`} key={slide.id}>
              <div className={styles.slideCardHeader}>
                <h3 className={styles.slideCardTitle}>{slideTitle(slide)}</h3>
                <span className={styles.slideCardNumber}>
                  {String(slide.number).padStart(2, "0")}
                </span>
              </div>
              <p className={styles.cardText}>
                {slide.data.template}
              </p>
            </article>
          ))}
        </section>
      </div>
    </main>
  );
}
