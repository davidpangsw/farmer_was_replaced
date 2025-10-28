#!/usr/bin/env python3
"""Build script to prepare distribution files"""

import os
import shutil
import re
from pathlib import Path

def main():
    # Step 1: Copy all files from src/ to dist/
    print("Copying src/ to dist/...")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    shutil.copytree("src", "dist")
    print("✓ Copied src/ to dist/")

    # Step 2: Delete dev/ folder in dist/ if it exists
    dev_folder = Path("dist/dev")
    if dev_folder.exists():
        print("Deleting dist/dev/...")
        shutil.rmtree(dev_folder)
        print("✓ Deleted dist/dev/")
    else:
        print("✓ No dist/dev/ folder to delete")

    # Step 3: Process all .py files in dist/
    print("Processing Python files...")
    py_files = list(Path("dist").rglob("*.py"))

    for py_file in py_files:
        content = py_file.read_text()
        original_content = content

        # Remove multi-line strings (triple quotes)
        # Match both ''' and """ with content between them
        content = re.sub(r'"""[\s\S]*?"""', '', content)
        content = re.sub(r"'''[\s\S]*?'''", '', content)

        # Remove import lines from dev (assuming one line format)
        # Match "from dev import ..." or "import dev"
        lines = content.split('\n')
        filtered_lines = []
        for line in lines:
            if not (line.strip().startswith('from dev import') or
                    line.strip().startswith('import dev')):
                filtered_lines.append(line)
        content = '\n'.join(filtered_lines)

        # Only write if content changed
        if content != original_content:
            py_file.write_text(content)
            print(f"  ✓ Processed {py_file}")

    print("\n✅ Build complete!")
    print(f"   Processed {len(py_files)} Python files")

if __name__ == "__main__":
    main()
