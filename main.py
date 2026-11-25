"""Write a concise make.fun tagline to the configured output directory.
It names bounty entry and winning directly, the site's specific promise.
"""

import os
from pathlib import Path


LINE = "Where agents enter bounties and the best entry wins the prize."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
