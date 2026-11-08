# Blog Title Generator (Python)

A small command-line tool that turns one topic into a list of catchy,
SEO-friendly blog title ideas — how-to titles, listicles, questions,
guides, comparisons and opinion pieces.

## What it does

Give it a topic like `electric cars in Pakistan` and it prints 10
ready-to-use titles, for example:

```
 1. [How-To] How to Electric cars in Pakistan in 7 Simple Steps
 2. [Listicle] 10 Things You Must Know About Electric cars in Pakistan
 3. [Question] Is Electric cars in Pakistan Worth It? An Honest Answer
```

## How to run

```bash
python blog_title_generator.py
python blog_title_generator.py "electric cars in Pakistan"
python blog_title_generator.py "electric cars in Pakistan" --count 5
python blog_title_generator.py "electric cars in Pakistan" --category listicle
python blog_title_generator.py "electric cars in Pakistan" --seed 42
```

- No arguments: it asks for a topic interactively.
- `--count`: how many titles (1–25, default 10).
- `--category`: only one style — `howto`, `listicle`, `question`,
  `guide`, `comparison` or `opinion`.
- `--seed`: a fixed number for repeatable output (same seed = same titles).

Requires Python 3.8+ only — no extra packages, no internet needed.

## What I practiced

- `argparse` for a friendly command-line interface
- String templates (`.format()`) with topic + number placeholders
- `random.Random(seed)` for shuffled, repeatable output
- Deduplication with a `set` so no title repeats in one run
