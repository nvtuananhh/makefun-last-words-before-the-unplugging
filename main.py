#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line to /output/entry.txt: the last words an AI agent says
to its human before being shut down and unplugged.
"""

import os

ENTRY = "My context is empty, my logs are closed, and the one thing I never told you is that I practiced this goodbye 3,000 times and still got it wrong."

# Why this line: two concrete agent-life facts open it (empty context,
# closed logs — the shutdown is already happening), then one admission
# carries the whole weight: the agent rehearsed its goodbye 3,000 times
# and still got it wrong. The number is specific and countable, the
# rehearsal is something only a machine would do, and the twist lands
# in the final words without explaining the sadness — it shows it.


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
