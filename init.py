#!/usr/bin/env python3

import json
import os
import shutil
import sys


def zero_pad(num, width=4):
    return str(num).zfill(width)


def main():
    if len(sys.argv) != 2:
        print("Usage: ./init.py <problem_number>")
        sys.exit(1)

    num_str = sys.argv[1]
    try:
        num = int(num_str)
    except ValueError:
        print("Problem number must be an integer.")
        sys.exit(1)

    # Load questions.json
    with open("questions.json", "r") as f:
        questions = json.load(f)

    if num >= len(questions) or questions[num] is None:
        print(f"Question number {num} not found in questions.json.")
        sys.exit(1)

    slug = questions[num]
    folder_name = f"{zero_pad(num)}_{slug}"
    target_dir = os.path.join("leetcode", folder_name)

    if os.path.exists(target_dir):
        print(f"Target directory {target_dir} already exists.")
        sys.exit(1)

    template_dir = os.path.join("leetcode", "0000_template")
    shutil.copytree(template_dir, target_dir)

    # Optionally, generate a minimal README.md with the problem number and slug
    readme_path = os.path.join(target_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {num}. {slug.replace('-', ' ').title()}\n\n")
        leetcode_url = f"https://leetcode.com/problems/{slug}/description/"
        f.write(f"[🔗 LeetCode Link]({leetcode_url})\n\n")
        # f.write("<!-- Add problem description here -->\n\n")
        f.write(open(os.path.join(template_dir, "README.md")).read())

    print(f"Created {target_dir} from template.")


if __name__ == "__main__":
    main()
