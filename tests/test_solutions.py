"""Run every solution against its official AtCoder sample input/output.

Each case feeds a solution script the exact sample input from its problem
page via stdin and checks stdout matches the official sample output. This
doesn't prove a solution passes the real judge (samples are usually too
small to catch performance issues), but it does catch logic regressions.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_solution(relative_path: str, stdin: str) -> str:
    script = REPO_ROOT / relative_path
    result = subprocess.run(
        [sys.executable, str(script)],
        input=stdin,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


# (script path, stdin, expected stdout) — one entry per official sample.
CASES = [
    ("abc458/c_stands_for_center.py", "ABCCA\n", "5"),
    ("abc458/c_stands_for_center.py", "XYZ\n", "0"),
    ("abc458/c_stands_for_center.py", "SMBCPROGRAMMINGCONTEST\n", "11"),
    ("abc462/c_not_covered_points.py", "3\n2 1\n1 3\n3 2\n", "2"),
    ("abc462/c_not_covered_points.py", "5\n1 1\n4 2\n2 3\n5 5\n3 4\n", "1"),
    (
        "abc462/c_not_covered_points.py",
        "7\n3 4\n6 1\n5 5\n2 7\n7 2\n1 3\n4 6\n",
        "2",
    ),
    (
        "abc463/c_tallest_at_the_moment.py",
        "4\n31 4\n26 5\n3 5\n15 9\n4\n3 4 5 6\n",
        "31\n26\n15\n15",
    ),
    ("abc463/d_maximize_the_gap.py", "6 3\n1 12\n2 7\n5 9\n9 13\n10 18\n15 20\n", "2"),
    ("abc463/d_maximize_the_gap.py", "2 2\n1 5\n5 9\n", "-1"),
    (
        "abc463/d_maximize_the_gap.py",
        "20 5\n169 748\n329 586\n529 972\n432 520\n408 587\n138 250\n114 656\n"
        "299 632\n755 984\n404 772\n155 506\n832 854\n353 465\n374 387\n"
        "384 567\n555 631\n428 951\n104 705\n405 530\n102 258\n",
        "35",
    ),
    (
        "abc464/c_plumage_palette.py",
        "6 7\n1 3 2\n2 6 5\n5 5 1\n3 3 5\n4 1 6\n6 3 6\n",
        "5\n5\n3\n3\n4\n4\n4",
    ),
]


@pytest.mark.parametrize("script,stdin,expected", CASES)
def test_official_sample(script: str, stdin: str, expected: str) -> None:
    assert run_solution(script, stdin) == expected
