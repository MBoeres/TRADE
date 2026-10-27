"""Compatibility entry point for the daily trade-digest script.

The project keeps the executable logic in `news.agent`, but the GitHub Action
runs `python news_agent.py`. This wrapper forwards execution to the real script
without duplicating the logic.
"""

from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("news.agent")), run_name="__main__")
