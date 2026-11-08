#!/usr/bin/env python3
"""
Blog Title Generator — catchy, SEO-friendly title ideas from one topic.

Usage:
    python blog_title_generator.py
    python blog_title_generator.py "electric cars in Pakistan"
    python blog_title_generator.py "electric cars in Pakistan" --count 5
    python blog_title_generator.py "electric cars in Pakistan" --category howto

How it works:
    You give it a topic (e.g. "electric cars in Pakistan").
    It fills that topic into proven title patterns (how-to, listicle,
    question, guide, mistake-avoidance, comparison ...) and prints a
    numbered list of ready-to-use titles. No internet needed.
"""

import argparse
import random
import sys

# ---------------------------------------------------------------------------
# Title patterns. {t} = the topic, {n} = a number.
# Each category is a list of (pattern, weight). Weight only affects the
# random shuffle order; every pattern can appear.
# ---------------------------------------------------------------------------
PATTERNS = {
    "howto": [
        "How to {t} — A Beginner's Guide",
        "How to {t} in {n} Simple Steps",
        "How to {t} Without Spending a Fortune",
        "How to Start With {t} (Even If You Are a Complete Beginner)",
        "How to {t}: The Complete 2026 Guide",
    ],
    "listicle": [
        "{n} Best Ways to {t}",
        "{n} Things You Must Know About {t}",
        "{n} Mistakes to Avoid When You {t}",
        "{n} Tips for {t} That Actually Work",
        "{n} Reasons Why {t} Matters in 2026",
    ],
    "question": [
        "Is {t} Worth It? An Honest Answer",
        "What Is {t} and Why Does Everyone Talk About It?",
        "Should You {t}? Pros and Cons Explained",
        "Why Is {t} So Popular Right Now?",
    ],
    "guide": [
        "The Ultimate Guide to {t}",
        "{t}: Everything You Need to Know",
        "A Complete Guide to {t} for Beginners",
        "{t} Explained in Simple Words",
    ],
    "comparison": [
        "{t} vs the Alternatives: Which One Is Right for You?",
        "{t}: Before and After — What Really Changes",
    ],
    "opinion": [
        "The Truth About {t} Nobody Tells You",
        "I Tried {t} for 30 Days — Here's What Happened",
        "Why Most People Get {t} Wrong",
    ],
}

CATEGORY_LABELS = {
    "howto": "How-To",
    "listicle": "Listicle",
    "question": "Question",
    "guide": "Guide",
    "comparison": "Comparison",
    "opinion": "Opinion / Story",
}


def clean_topic(topic):
    """Tidy the topic: strip whitespace, drop a trailing full stop,
    and capitalise the first letter for display."""
    topic = " ".join(topic.strip().split())
    if topic.endswith("."):
        topic = topic[:-1]
    return topic[:1].upper() + topic[1:] if topic else topic


def generate(topic, count=10, category=None, seed=None):
    """Return a list of (category, title) tuples."""
    topic = clean_topic(topic)
    if not topic:
        raise ValueError("Topic cannot be empty.")

    rng = random.Random(seed)
    categories = [category] if category else list(PATTERNS)
    pool = []
    for cat in categories:
        for pattern in PATTERNS[cat]:
            pool.append((cat, pattern))

    rng.shuffle(pool)
    titles = []
    used = set()
    for cat, pattern in pool:
        number = rng.choice([3, 5, 7, 10, 12, 15])
        title = pattern.format(t=topic, n=number)
        if title not in used:
            used.add(title)
            titles.append((cat, title))
        if len(titles) >= count:
            break
    return titles


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate catchy blog title ideas from a topic."
    )
    parser.add_argument("topic", nargs="?", help="blog topic, e.g. 'electric cars in Pakistan'")
    parser.add_argument("--count", type=int, default=10,
                        help="how many titles to generate (default 10, max 25)")
    parser.add_argument("--category", choices=sorted(PATTERNS),
                        help="only use one category: " + ", ".join(sorted(PATTERNS)))
    parser.add_argument("--seed", type=int, default=None,
                        help="fixed seed for repeatable output")
    args = parser.parse_args(argv)

    if args.topic is None:
        try:
            args.topic = input("Enter your blog topic: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nNo topic given. Exiting.")
            return 1

    count = max(1, min(args.count, 25))
    try:
        titles = generate(args.topic, count=count,
                          category=args.category, seed=args.seed)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    print(f"\n{len(titles)} title ideas for: {clean_topic(args.topic)}\n")
    for i, (cat, title) in enumerate(titles, 1):
        print(f"{i:2}. [{CATEGORY_LABELS[cat]}] {title}")
    print("\nTip: pick one, then tweak the number or the year to fit your post.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
