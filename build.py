#!/usr/bin/env python3
"""
Build script that:
1. Copies all files from src/ to dist/
2. Deletes dev/ folder in dist/ if any
3. Removes all multi-line strings in *.py files
4. Removes any imports of dev/
"""

import os
import shutil
import re
from pathlib import Path


def copy_src_to_dist():
    """Copy all files from src/ to dist/"""
    src_dir = Path("src")
    dist_dir = Path("dist")

    # Remove dist if it exists and recreate it
    if dist_dir.exists():
        shutil.rmtree(dist_dir)

    # Copy src to dist
    if src_dir.exists():
        shutil.copytree(src_dir, dist_dir)
        print(f"✓ Copied {src_dir}/ to {dist_dir}/")
    else:
        print(f"⚠ Warning: {src_dir}/ does not exist")


def delete_dev_folder():
    """Delete dev/ folder in dist/ if it exists"""
    dev_dir = Path("dist/dev")

    if dev_dir.exists():
        shutil.rmtree(dev_dir)
        print(f"✓ Deleted {dev_dir}/")
    else:
        print(f"  No {dev_dir}/ folder found")


def remove_multiline_strings_and_dev_imports(file_path):
    """Remove multi-line strings and dev imports from a Python file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove multi-line strings (triple-quoted strings)
    # This regex handles both ''' and """ with non-greedy matching
    content = re.sub(r'"""[\s\S]*?"""', '', content)
    content = re.sub(r"'''[\s\S]*?'''", '', content)

    # Remove dev imports
    # Matches lines like: from dev import ..., from dev.something import ..., import dev, import dev.something
    lines = content.split('\n')
    filtered_lines = []

    for line in lines:
        # Skip lines that import from dev
        if re.match(r'^\s*from\s+dev(\s|\.)', line) or re.match(r'^\s*import\s+dev(\.|$|\s)', line):
            continue
        filtered_lines.append(line)

    content = '\n'.join(filtered_lines)

    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def process_python_files():
    """Process all .py files in dist/"""
    dist_dir = Path("dist")

    if not dist_dir.exists():
        print(f"⚠ Warning: {dist_dir}/ does not exist")
        return

    py_files = list(dist_dir.rglob("*.py"))
    modified_count = 0

    for py_file in py_files:
        if remove_multiline_strings_and_dev_imports(py_file):
            modified_count += 1
            print(f"  Processed: {py_file}")

    print(f"✓ Processed {modified_count} Python file(s)")


def main():
    print("Starting build process...\n")

    # Step 1: Copy src to dist
    copy_src_to_dist()

    # Step 2: Delete dev folder
    delete_dev_folder()

    # Step 3: Process Python files (remove multi-line strings and dev imports)
    process_python_files()

    print("\n✓ Build complete!")


if __name__ == "__main__":
    main()
