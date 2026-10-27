"""Compatibility wrapper for the active script used by the daily workflow.

The workflow invokes `python news_agent.py`; this file resolves the real script
in the repo and executes it. Some old versions used `news.agent`, others used
`news_Version2.agent`.
"""

from pathlib import Path
import runpy


def resolve_script() -> Path:
    candidates = [
        Path(__file__).with_name("news.agent"),
        Path(__file__).with_name("news_Version2.agent"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No news script found. Expected news.agent or news_Version2.agent.")


if __name__ == "__main__":
    script = resolve_script()
    print(f"Running {script.name}")
    runpy.run_path(str(script), run_name="__main__")
