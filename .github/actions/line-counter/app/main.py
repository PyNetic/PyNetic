from os import environ
from typing import cast

from github import Github
from github.ContentFile import ContentFile
from mdutils import MdUtils
import requests

REPO_NAME = cast(str, environ.get("GITHUB_REPOSITORY"))
PROJECT_NAME = REPO_NAME.split("/")[-1]
BRANCH = "master"
OUT_PATH = ".github/stats/Code Statistics.md"
LOC_API_URL = f"https://api.codetabs.com/v1/loc?github={REPO_NAME}"
KEYS = ["📝Files", "〰️Lines", "🗨️Blanks", "🙈Comments", "👨‍💻Lines of Code"]

print(f">>> Starting Code Stats Process for {REPO_NAME} <<<")

REPOSITORY = Github(environ.get("TOKEN")).get_repo(REPO_NAME)
OLD_CONTENTS = cast(ContentFile, REPOSITORY.get_contents(OUT_PATH, ref=BRANCH))
DATA = zip(*map(dict.values, requests.get(LOC_API_URL).json()))
LANGUAGES = next(DATA)[0:-1]

# Create Markdown File
md_file = MdUtils("Lines Of Code.md")
md_file.create_md_file()
md_file.new_header(1, f"📊 Code Statistics for {PROJECT_NAME}")

# Setup Tables
languages_table = ["", *LANGUAGES]
totals_table = KEYS.copy()
loc = []

# Populate Tables
for name, (*values, total) in zip(KEYS, DATA):
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
md_file.new_table(columns=len(LANGUAGES) + 1, rows=6, text=languages_table)
md_file.new_line()

print(OLD_CONTENTS, OLD_CONTENTS.path, OLD_CONTENTS.sha, sep="\n")

# Update Readme
REPOSITORY.update_file(
    OLD_CONTENTS.path,
    "📈Update code statistics",
    md_file.get_md_text(),
    OLD_CONTENTS.sha,
    branch=BRANCH,
)
