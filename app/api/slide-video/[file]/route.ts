import { createReadStream } from "node:fs";
import { stat } from "node:fs/promises";
import path from "node:path";
import { Readable } from "node:stream";
import { NextRequest } from "next/server";

const videoDirectory = path.join(
  process.cwd(),
  "slides",
  "files",
  "LPPresentation",
);

export const runtime = "nodejs";

function resolveFile(file: string) {
  if (!/^[a-f0-9_]+\.(mp4)$/i.test(file)) {
    return null;
  }

  return path.join(videoDirectory, file);
}

export async function GET(
  request: NextRequest,
  context: { params: Promise<{ file: string }> },
) {
  const { file } = await context.params;
  const resolvedPath = resolveFile(file);

  if (!resolvedPath) {
    return new Response("Not found", { status: 404 });
  }

  let fileStats;
  try {
    fileStats = await stat(resolvedPath);
  } catch {
    return new Response("Not found", { status: 404 });
  }

  const range = request.headers.get("range");
  const size = fileStats.size;

  if (!range) {
    const stream = createReadStream(resolvedPath);
    return new Response(Readable.toWeb(stream) as ReadableStream, {
      status: 200,
      headers: {
        "Content-Type": "video/mp4",
        "Content-Length": size.toString(),
        "Accept-Ranges": "bytes",
        "Cache-Control": "public, max-age=31536000, immutable",
      },
    });
  }

  const [startText, endText] = range.replace("bytes=", "").split("-");
  const start = Number.parseInt(startText, 10);
  const end = endText ? Number.parseInt(endText, 10) : size - 1;

  if (Number.isNaN(start) || Number.isNaN(end) || start > end || end >= size) {
    return new Response("Invalid range", {
      status: 416,
      headers: { "Content-Range": `bytes */${size}` },
    });
  }

  const stream = createReadStream(resolvedPath, { start, end });

  return new Response(Readable.toWeb(stream) as ReadableStream, {
    status: 206,
    headers: {
      "Content-Type": "video/mp4",
      "Content-Length": (end - start + 1).toString(),
      "Content-Range": `bytes ${start}-${end}/${size}`,
      "Accept-Ranges": "bytes",
      "Cache-Control": "public, max-age=31536000, immutable",
    },
  });
}
