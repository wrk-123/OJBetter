import os
import re
import json
from collections import OrderedDict

def parse_markdown(md_content):
    versions = OrderedDict()
    current_version = None
    for line in md_content.split("\n"):
        if line.startswith("## "):
            current_version = line.strip("# ").strip()
            versions[current_version] = ""
        elif current_version:
            versions[current_version] += "\n\n" + line.strip()
    return versions

def main():
    announce_dir = "resources/announce"
    output_dir_base = "resources/locales"
    md_files = [f for f in os.listdir(announce_dir) if f.endswith('.md')]

    for md_file in md_files:
        name = os.path.splitext(md_file)[0]
        output_dir = os.path.join(output_dir_base, name)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "announce.json")

        with open(os.path.join(announce_dir, md_file), 'r', encoding='utf-8') as f:
            md_content = f.read()

        versions = parse_markdown(md_content)
        # Keep only the latest 3 versions
        latest_versions = list(versions.keys())[-3:]
        versions = {ver: versions[ver].strip() for ver in latest_versions if ver in versions}

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({"lastVersion": latest_versions[-1], **versions}, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
