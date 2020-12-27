#!/usr/bin/env python

"""

"""

from pathlib import Path
import re
from tqdm import tqdm


def load_markdown_file(fname):
    text = []
    with open(fname, "r", encoding="utf-8") as fi:
        for line in fi:
            text.append(line)

    return text


def save_markdown_file(fname, text):
    with open(fname, "w", encoding="utf-8") as fo:
        for line in text:
            fo.write(line)


if __name__ == "__main__":
    posts_root = Path("../content/posts.bak")
    posts_flist = posts_root.glob("*/index.md")

    re_class = re.compile(r"class=\"[a-zA-Z_-]*\"")
    re_id = re.compile(r"id=\"[a-zA-Z_-]*\"")
    re_div = re.compile(r"<div *>")
    re_undiv = re.compile(r"</div *>")
    re_div2 = re.compile(r"<div *")
    # re_script = re.compile(r"<script.*</noscript>")
    # re_object = re.compile(r"<object.*</object>")
    # re_img = re.compile(r"<img.*>")
    re_span = re.compile(r"<span *>")
    re_unspan = re.compile(r"</span *>")
    # re_a = re.compile(r"<a.*>")
    # re_una = re.compile(r"</a>")
    # re_em = re.compile(r"<em>")
    # re_unem = re.compile(r"</em>")

    for post_fn in tqdm(posts_flist):
        input_text = load_markdown_file(post_fn)

        output_text = []
        for line in input_text:
            line = re_class.sub("", line)
            line = re_id.sub("", line)
            line = re_div.sub("", line)
            line = re_undiv.sub("", line)
            line = re_div2.sub("", line)
            # line = re_script.sub("", line)
            # line = re_object.sub("", line)
            # line = re_img.sub("", line)
            line = re_span.sub("", line)
            line = re_unspan.sub("", line)
            # line = re_a.sub("", line)
            # line = re_una.sub("", line)
            # line = re_em.sub("", line)
            # line = re_unem.sub("", line)
            output_text.append(line)

        save_markdown_file(post_fn, output_text)
