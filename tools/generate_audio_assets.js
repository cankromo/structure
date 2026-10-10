#!/usr/bin/env node
const { spawnSync } = require("child_process");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const QUESTIONS_PATH = path.join(ROOT, "data", "questions.json");
const OUT_DIR = path.join(ROOT, "assets", "audio");
const TMP_DIR = path.join(OUT_DIR, ".tmp");
const VOICE = process.env.TOEFL_VOICE || "Ava (Premium)";
const FALLBACK_VOICE = process.env.TOEFL_FALLBACK_VOICE || "Samantha";
const RATE = process.env.TOEFL_VOICE_RATE || "145";

function run(command, args) {
  const result = spawnSync(command, args, { encoding: "utf8" });
  return result;
}

function availableVoices() {
  const result = run("say", ["-v", "?"]);
  if (result.status !== 0) return "";
  return result.stdout || "";
}

function voiceExists(name, list) {
  return list.split("\n").some((line) => line.startsWith(`${name} `));
}

function safeText(text) {
  return String(text || "")
    .replace(/\bCO2\b/g, "carbon dioxide")
    .replace(/\bAI\b/g, "A I")
    .replace(/\bLIGO\b/g, "LIGO")
    .replace(/\s+/g, " ")
    .trim();
}

function hashText(text) {
  return crypto.createHash("sha1").update(text).digest("hex").slice(0, 12);
}

function writeAudio(id, text, voice) {
  const clean = safeText(text);
  const wavPath = path.join(OUT_DIR, `${id}.wav`);
  const aiffPath = path.join(TMP_DIR, `${id}.aiff`);
  const metaPath = path.join(TMP_DIR, `${id}.sha1`);
  const hash = hashText(`${voice}|${RATE}|${clean}`);

  if (fs.existsSync(wavPath) && fs.existsSync(metaPath) && fs.readFileSync(metaPath, "utf8") === hash) {
    return { id, file: `assets/audio/${id}.wav`, text_hash: hash, skipped: true };
  }

  const sayResult = run("say", ["-v", voice, "-r", RATE, "-o", aiffPath, clean]);
  if (sayResult.status !== 0) {
    throw new Error(`say failed for ${id}: ${sayResult.stderr || sayResult.stdout}`);
  }

  const convertResult = run("afconvert", ["-f", "WAVE", "-d", "LEI16@22050", aiffPath, wavPath]);
  if (convertResult.status !== 0) {
    throw new Error(`afconvert failed for ${id}: ${convertResult.stderr || convertResult.stdout}`);
  }

  fs.writeFileSync(metaPath, hash);
  fs.rmSync(aiffPath, { force: true });
  return { id, file: `assets/audio/${id}.wav`, text_hash: hash, skipped: false };
}

function collectItems(questions) {
  const items = [];

  for (const item of questions.choose_response || []) {
    items.push({ id: item.id, type: "choose_response", text: item.prompt });
  }
  for (const item of questions.conversations || []) {
    items.push({
      id: item.id,
      type: "conversations",
      text: (item.turns || []).map((turn) => turn[1]).join(" "),
    });
  }
  for (const item of questions.announcements || []) {
    items.push({ id: item.id, type: "announcements", text: item.text });
  }
  for (const item of questions.academic_talks || []) {
    items.push({ id: item.id, type: "academic_talks", text: item.text });
  }
  for (const item of questions.repeat || []) {
    items.push({ id: item.id, type: "repeat", text: item.text });
  }
  for (const item of questions.interview || []) {
    items.push({ id: item.id, type: "interview", text: item.prompt });
  }

  return items.filter((item) => item.text && item.id);
}

function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.mkdirSync(TMP_DIR, { recursive: true });

  const voiceList = availableVoices();
  const voice = voiceExists(VOICE, voiceList) ? VOICE : FALLBACK_VOICE;
  if (!voiceExists(voice, voiceList)) {
    throw new Error(`Neither "${VOICE}" nor "${FALLBACK_VOICE}" is available in macOS say voices.`);
  }

  const questions = JSON.parse(fs.readFileSync(QUESTIONS_PATH, "utf8"));
  const items = collectItems(questions);
  const files = {};
  let generated = 0;
  let skipped = 0;

  for (const item of items) {
    const result = writeAudio(item.id, item.text, voice);
    files[item.id] = {
      type: item.type,
      file: result.file,
      text_hash: result.text_hash,
    };
    if (result.skipped) skipped += 1;
    else generated += 1;
  }

  fs.writeFileSync(
    path.join(OUT_DIR, "manifest.json"),
    JSON.stringify(
      {
        generated_at: new Date().toISOString(),
        voice,
        rate: Number(RATE),
        format: "wav",
        sample_rate: 22050,
        files,
      },
      null,
      2
    ) + "\n"
  );

  fs.rmSync(TMP_DIR, { recursive: true, force: true });
  console.log(`Audio manifest written: ${Object.keys(files).length} files (${generated} generated, ${skipped} skipped)`);
}

main();
