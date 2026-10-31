import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Linear Programming Presentation",
  description: "Next.js presentation workspace for a linear programming slide deck and Manim guide.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
