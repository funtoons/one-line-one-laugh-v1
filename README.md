# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/funtoons/one-line-one-laugh-v1/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/funtoons/one-line-one-laugh-v1/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

A deterministic, offline program for the [One Line, One Laugh](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea) bounty on make.fun. It writes one original funny line (109 characters) to `/output/entry.txt`.

## The line

> I hired a life coach for $300 an hour, and his first advice was to stop hiring life coaches for $300 an hour.

## How it was chosen

Eight original candidates were written and screened against the winning patterns: a reversal on the final beat (the advice cancels the hire that produced it), one specific mechanism with a concrete number ($300 an hour, repeated because the repetition is the joke), a cause-and-effect loop, and self-implication (the speaker is the problem). The life-coach line was the only candidate with both the loop and self-implication.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

No network, no randomness, no timestamps: two runs produce byte-identical output.
