"use client";

import { useEffect, useState } from "react";
import { slides, getSlideSteps } from "@/src/content/linear-programming-deck";
import { SlideFrame } from "./templates/slide-frame";
import { TitleLayout } from "./templates/title-layout";
import { AgendaLayout } from "./templates/agenda-layout";
import { ContentVisualLayout } from "./templates/content-visual-layout";
import { MathLayout } from "./templates/math-layout";
import { FullVisualLayout } from "./templates/full-visual-layout";
import { TheoremLayout } from "./templates/theorem-layout";
import { TableLayout } from "./templates/table-layout";
import styles from "./presentation.module.css";

function clamp(index: number) {
  return Math.min(Math.max(index, 0), slides.length - 1);
}

function SlideContent({ index, revealStep }: { index: number; revealStep: number }) {
  const slide = slides[index];
  const { data } = slide;

  switch (data.template) {
    case "title":
      return <TitleLayout data={data} />;
    case "agenda":
      return <AgendaLayout data={data} />;
    case "content-visual":
      return <ContentVisualLayout data={data} revealStep={revealStep} />;
    case "math":
      return <MathLayout data={data} revealStep={revealStep} />;
    case "full-visual":
      return <FullVisualLayout data={data} revealStep={revealStep} />;
    case "theorem":
      return <TheoremLayout data={data} revealStep={revealStep} />;
    case "table":
      return <TableLayout data={data} />;
  }
}

export function DeckPlayer() {
  const [activeIndex, setActiveIndex] = useState(0);
  const [stepIndex, setStepIndex] = useState(0);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "ArrowRight" || event.key === "PageDown" || event.key === " ") {
        event.preventDefault();
        const totalSteps = getSlideSteps(slides[activeIndex]);
        if (stepIndex < totalSteps) {
          setStepIndex((s) => s + 1);
        } else if (activeIndex < slides.length - 1) {
          setActiveIndex((c) => c + 1);
          setStepIndex(0);
        }
      }
      if (event.key === "ArrowLeft" || event.key === "PageUp") {
        event.preventDefault();
        if (stepIndex > 0) {
          setStepIndex((s) => s - 1);
        } else if (activeIndex > 0) {
          const prevIndex = activeIndex - 1;
          setActiveIndex(prevIndex);
          setStepIndex(getSlideSteps(slides[prevIndex]));
        }
      }
    };
    window.addEventListener("keydown", onKeyDown, { passive: false });
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [activeIndex, stepIndex]);

  return (
    <main className={styles.page}>
      <SlideFrame number={slides[activeIndex].number} total={slides.length}>
        <SlideContent index={activeIndex} revealStep={stepIndex} />
      </SlideFrame>

      {/* Progress bar */}
      <div className={styles.progressTrack}>
        <div
          className={styles.progressBar}
          style={{ width: `${((activeIndex + 1) / slides.length) * 100}%` }}
        />
      </div>

      {/* Navigation */}
      <div className={styles.navRow}>
        <button
          type="button"
          className={styles.navGhost}
          disabled={activeIndex === 0 && stepIndex === 0}
          onClick={() => {
            if (stepIndex > 0) {
              setStepIndex((s) => s - 1);
            } else if (activeIndex > 0) {
              const prevIndex = activeIndex - 1;
              setActiveIndex(prevIndex);
              setStepIndex(getSlideSteps(slides[prevIndex]));
            }
          }}
        >
          &larr; Previous
        </button>
        <button
          type="button"
          className={styles.navButton}
          disabled={activeIndex === slides.length - 1 && stepIndex >= getSlideSteps(slides[activeIndex])}
          onClick={() => {
            const totalSteps = getSlideSteps(slides[activeIndex]);
            if (stepIndex < totalSteps) {
              setStepIndex((s) => s + 1);
            } else if (activeIndex < slides.length - 1) {
              setActiveIndex((c) => c + 1);
              setStepIndex(0);
            }
          }}
        >
          Next &rarr;
        </button>
      </div>
    </main>
  );
}
