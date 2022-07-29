from github import GitHub
from mdutils import MdUtils
import requests

data = zip(*map(dict.values, requests.get(f"https://api.codetabs.com/v1/loc?github=pynetic/PyNetic").json()))

md_file = MdUtils('Lines Of Code.md')
md_file.create_md_file()
md_file.new_header(1, "📊 Lines of code in project")

keys = ["📝Files", "〰️Lines", "🗨️Blanks", "🙈Comments", "👨‍💻Lines of Code"]
langs_table = ["", *next(data)[0:-1]]
totals_table = keys
langs_columns = len(langs_table)

for name, (*values, total) in zip(keys, data):
    langs_table.extend([name, *values])
    totals_table.append(total)

md_file.new_header(2, "👨‍💻Languages")
md_file.new_table(
    columns=langs_columns,
    rows=6,
    text=langs_table
)
md_file.new_line()
md_file.new_header(2, "Totals")
md_file.new_table(
    columns=5,
    rows=2,
    text=totals_table
)

repo = GitHub(os.environ.get("TOKEN")).get_repo("PyGithub/PyGithub")
contents = repo.get_contents(".github/line-counts.md", ref="test")
repo.update_file(
    contents.path,
    "📈Update repo stats",
    md_file.get_md_text(),
    contents.sha,
    branch="master"
)
