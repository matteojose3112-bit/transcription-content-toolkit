#!/usr/bin/env python3
"""Validate basic SRT or WebVTT structure using only the Python standard library.

Usage:
  python tools/validate_captions.py examples/sample-captions.srt
  python tools/validate_captions.py examples/sample-captions.srt examples/sample-captions.vtt
"""
from __future__ import annotations
import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

TIME_RE = re.compile(r"^(\d{2,}:\d{2}:\d{2}[,.]\d{3})\s+-->\s+(\d{2,}:\d{2}:\d{2}[,.]\d{3})(?:\s+.*)?$")
@dataclass
class Cue:
    start: int
    end: int
    line: int
    text: str

def time_ms(value: str) -> int:
    value = value.replace(",", ".")
    hours, minutes, seconds = value.split(":")
    sec, millis = seconds.split(".")
    return ((int(hours) * 60 + int(minutes)) * 60 + int(sec)) * 1000 + int(millis)

def parse(path: Path) -> tuple[list[Cue], list[str]]:
    errors: list[str] = []
    try:
        content = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        return [], [f"Cannot read file: {exc}"]
    lines = content.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    is_vtt = path.suffix.lower() == ".vtt"
    if is_vtt:
        if not lines or lines[0].strip() != "WEBVTT":
            errors.append("WebVTT file must begin with WEBVTT.")
        start_at = 1
    else:
        start_at = 0
    cues: list[Cue] = []
    i = start_at
    expected_index = 1
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        # SRT has a numeric cue index; VTT may have an optional cue identifier.
        if not is_vtt and lines[i].strip().isdigit():
            index = int(lines[i].strip())
            if index != expected_index:
                errors.append(f"Line {i + 1}: expected cue number {expected_index}, found {index}.")
            expected_index += 1
            i += 1
            if i >= len(lines):
                errors.append(f"Line {i}: missing timecode after cue number.")
                break
        elif is_vtt and "-->" not in lines[i]:
            # Allow a VTT cue identifier, but require a timecode immediately after it.
            i += 1
            if i >= len(lines):
                errors.append(f"Line {i}: cue identifier has no timecode.")
                break
        match = TIME_RE.match(lines[i].strip())
        if not match:
            errors.append(f"Line {i + 1}: expected a valid timecode line.")
            i += 1
            continue
        start, end = time_ms(match.group(1)), time_ms(match.group(2))
        time_line = i + 1
        i += 1
        text_lines: list[str] = []
        while i < len(lines) and lines[i].strip():
            text_lines.append(lines[i].strip())
            i += 1
        if end <= start:
            errors.append(f"Line {time_line}: cue end must be later than cue start.")
        if not text_lines:
            errors.append(f"Line {time_line}: cue text is empty.")
        cues.append(Cue(start, end, time_line, " ".join(text_lines)))
    for previous, current in zip(cues, cues[1:]):
        if current.start < previous.start:
            errors.append(f"Line {current.line}: cue starts before the preceding cue.")
        if current.start < previous.end:
            errors.append(f"Line {current.line}: cue overlaps the preceding cue.")
    if not cues:
        errors.append("No caption cues found.")
    return cues, errors

def main() -> int:
    parser = argparse.ArgumentParser(description="Check basic SRT/WebVTT structure and timing.")
    parser.add_argument("files", nargs="+", type=Path, help="Caption files (.srt or .vtt)")
    args = parser.parse_args()
    failed = False
    for path in args.files:
        if path.suffix.lower() not in {".srt", ".vtt"}:
            print(f"FAIL {path}: expected a .srt or .vtt extension")
            failed = True
            continue
        cues, errors = parse(path)
        if errors:
            failed = True
            print(f"FAIL {path} ({len(cues)} cues)")
            for error in errors:
                print(f"  - {error}")
        else:
            duration = cues[-1].end / 1000
            print(f"PASS {path}: {len(cues)} cues, last cue ends at {duration:.3f}s")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
