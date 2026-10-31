import { chromium } from "playwright";
import { mkdirSync } from "fs";

const TOTAL_SLIDES = 14;
const OUT = "screenshots";

mkdirSync(OUT, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

await page.goto("http://localhost:3000/slides", { waitUntil: "networkidle" });
await page.waitForTimeout(1500);

for (let i = 0; i < TOTAL_SLIDES; i++) {
  await page.waitForTimeout(600);
  await page.screenshot({ path: `${OUT}/slide-${String(i + 1).padStart(2, "0")}.png` });
  if (i < TOTAL_SLIDES - 1) {
    await page.keyboard.press("ArrowRight");
  }
}

await browser.close();
console.log(`Done – ${TOTAL_SLIDES} screenshots in ./${OUT}/`);
