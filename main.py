"""One Line, One Laugh: write a single funny line to /output/entry.txt.

The line was chosen from eight original candidates screened against the
winning patterns: a reversal on the final beat, one specific mechanism
with a concrete number, a cause-and-effect loop, and self-implication.
The winning line has all of them: the coach hired to fix the speaker's
spending tells the speaker to stop paying coaches, so the advice
cancels the hire that produced it.
"""

LINE = "I hired a life coach for $300 an hour, and his first advice was to stop hiring life coaches for $300 an hour."


import os


def main():
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
