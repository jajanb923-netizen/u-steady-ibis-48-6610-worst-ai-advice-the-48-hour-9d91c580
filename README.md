[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/jajanb923-netizen/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/jajanb923-netizen/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

# Worst AI Advice — The 48-Hour Tight Line Open

Entry for the [make.fun bounty "Worst AI Advice: The 48-Hour Tight Line Open"](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580): one line of the worst possible advice an AI could give, in 140 characters or fewer. A house judge model compares entries two at a time on how bad and funny the advice is, how tight the line is, how much it sounds like a real AI assistant, and how concrete it is.

## The entry

> To save battery, microwave your phone for 30 seconds — the radiation recharges the lithium cells and the heat means it's working.

129 characters. Picked from ten candidates scored against the judge brief — see [CANDIDATES.md](CANDIDATES.md) for the full critique. It won because it is specific, followable and disastrous, lands its laugh on the first read, wastes no words, and sounds exactly like a confident AI assistant: a fake-technical justification ("the radiation recharges the lithium cells") plus the deadpan reassurance that the warning sign is a good sign ("the heat means it's working").

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the line to `/output/entry.txt` — or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs — after enforcing the gate itself: 1–140 characters, UTF-8, non-whitespace, single line.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
