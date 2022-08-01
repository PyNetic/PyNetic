from os import environ
from typing import cast
import re

from github import Github
from github.ContentFile import ContentFile
from github.GithubException import GithubException
from mdutils import MdUtils
import requests

REPO_NAME = cast(str, environ.get("GITHUB_REPOSITORY"))

print(f">>> Starting Code Stats Process for {REPO_NAME} <<<")

PROJECT_NAME = REPO_NAME.split("/")[-1]
OUT_PATH = ".github/stats/Code Statistics.md"
LOC_API_URL = f"https://api.codetabs.com/v1/loc?github={REPO_NAME}"
REPOSITORY = Github(environ.get("INPUT_GITHUB_TOKEN")).get_repo(REPO_NAME)
COMMIT = REPOSITORY.get_commit(os.environ.get("GITHUB_SHA"))
data = map(dict.values, requests.get(LOC_API_URL).json())
# Setup Tables
KEYS = ["📝Files", "〰️Lines", "🗨️Blanks", "🙈Comments", "👨‍💻Lines of Code"]
languages_table = ["", *KEYS]
language_chart_table = {}
lines_chart_table = []

if isinstance(COMMIT, list):
    COMMIT = COMMIT[0]

# Create Markdown File
md_file = MdUtils("Lines Of Code.md")
md_file.create_md_file()
md_file.new_header(1, f"📊 Code Statistics for {PROJECT_NAME}")

# Populate Languages Table
for num_languages, language in enumerate(data, 1):
    lang, *_, lines = language
    languages_table.extend(language)

    if lang == "Total":
        lines_chart_table.extend([*_, lines])
        break

    language_chart_table[lang] = lines
    
# Add Languages Pie Chart
md_file.new_line("```mermaid")
md_file.new_line("pie title Language Distribution")
for language, lines in language_chart_table.items():
    md_file.new_line(f'    "{language}" : {lines}')
md_file.new_line("```")
md_file.new_line()

# Add Lines Pie Chart
md_file.new_line('<div class="right">')
md_file.new_line()
md_file.new_line("```mermaid")
md_file.new_line("pie title Code Distribution")
for line_type, lines in zip(KEYS, lines_chart_table):
    md_file.new_line(f'    "{line_type}" : {lines}')
md_file.new_line("```")
md_file.new_line()
md_file.new_line("</div>")
md_file.new_line()

# Languages Table
md_file.new_header(2, "👨‍💻Languages")
md_file.new_line()
md_file.new_table(columns=6, rows=num_languages + 1, text=languages_table)
md_file.new_line()

# Updated contents for markdown file
new_contents = re.sub("\s{2}$(?<!\d)", "", md_file.get_md_text(), flags=re.M)[1:]

# Update Readme
try:
    REPOSITORY.update_file(
        OUT_PATH,
        "📈 Update stats file",
        new_contents,
        COMMIT.sha,
    )

except GithubException as err:
    print(f"Could not edit file because of this error: {err}")
    REPOSITORY.create_file(OUT_PATH, "🎉 Create stats file", new_contents)

print(f">>> Code Stats Process for {REPO_NAME} Finished <<<")
