#!/usr/bin/env python

"""

"""

from pathlib import Path
import shutil
import subprocess


if __name__ == "__main__":
    posts_root = Path("content/posts")
    dst_root = Path("static/twitter_cards")
    src_flist = posts_root.glob("*/twitter_card.png")
    
    for src_fn in src_flist:
        src_dirname = src_fn.parent.name
        dst_dirname = src_dirname.split("--")[1]
        dst_dirpath = dst_root / dst_dirname
        if not dst_dirpath.exists():
            dst_dirpath.mkdir(parents=True)

        dst_fn = dst_dirpath / "twitter_card.png"
        shutil.copy(src_fn, dst_fn)

    cmd = f"rsync -ahv {dst_root} stfate@tyrfing.site:/var/www/html/assets/"
    subprocess.run(cmd.split())