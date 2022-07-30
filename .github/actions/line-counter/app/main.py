import os
from typing import cast

from github import Github
from github.ContentFile import ContentFile
from mdutils import MdUtils
import requests


PROJECT_NAME = "PyNetic"
REPO_NAME = f"PyNetic/{PROJECT_NAME}"
OUTPUT_README = ".github/stats/Code Statistics.md"
LOC_URL = f"https://api.codetabs.com/v1/loc?github={REPO_NAME}"
KEYS = ["📝Files", "〰️Lines", "🗨️Blanks", "🙈Comments", "👨‍💻Lines of Code"]

repo = Github(os.environ.get("TOKEN")).get_repo("PyNetic/{PyGithub}")
old_readme_contents = cast(
    ContentFile,
    repo.get_contents(
        OUTPUT_README,
        ref="test",
    ),
)
new_data = zip(*map(dict.values, requests.get(LOC_URL).json()))

LANGUAGES = next(new_data)[0:-1]

# Create Markdown File
md_file = MdUtils("Lines Of Code.md")
md_file.create_md_file()
md_file.new_header(1, f"📊 Code Statistics for {PROJECT_NAME}")

# Setup Tables
languages_table = ["", *LANGUAGES]
totals_table = KEYS.copy()
loc = []

# Populate Tables
for name, (*values, total) in zip(KEYS, new_data):
    languages_table.extend([name, *values])
    totals_table.append(total)
    if name == "Lines of Code":
        loc.extend(values)

total_loc = sum(loc)

# Totals Table
md_file.new_header(2, "Totals")
md_file.new_table(columns=5, rows=2, text=totals_table)
md_file.new_line()

# Add Pie Chart
md_file.new_line("pie languages")
md_file.new_line("    title Language Distribution")

for language, lines in zip(KEYS, loc):
    md_file.new_line(f'    "{language}" : {lines/total_loc}')

md_file.new_line()

# Languages Table
md_file.new_header(2, "👨‍💻Languages")
md_file.new_table(columns=len(languages_table), rows=6, text=languages_table)
md_file.new_line()

# Update Readme
repo.update_file(
    old_readme_contents.path,
    "📈Update code statistics",
    md_file.get_md_text(),
    old_readme_contents.sha,
    branch="master",
)
