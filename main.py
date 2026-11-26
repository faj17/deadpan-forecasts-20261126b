#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes a single-line deadpan weather forecast for the invented city of
Quesselton to /output/entry.txt.
"""
import os

# The forecast is assembled from fragments so each clause earns its place:
# the overnight setup (high/low), the absurd event (rain falling upward),
# and the deadpan advice that sells it as a real broadcast line.
SETUP = "Overnight in Quesselton: a high of 72, a low of 19, "
EVENT = "and a 40 percent chance of rain falling upward, "
ADVICE = "so bring an umbrella and hold it underneath you."

MAX_CHARS = 160


def assemble():
    return SETUP + EVENT + ADVICE


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the "
                         f"{MAX_CHARS}-char limit")
    if text.count("\n") != 0:
        raise ValueError("entry must be exactly one line")
    return text


def main():
    entry = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
