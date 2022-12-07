from github import Github
import pandas as pd

# Get the repository
g = Github("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")

repo = g.get_repo("project-chip/connectedhomeip")

# store the data in the list
data = []

for issue in repo.get_issues(state="all"):
    data.append([issue.number, issue.created_at, issue.state, issue.title, issue.closed_at, issue.html_url])

df = pd.DataFrame(data, columns=["Issue ID", "Created Date", "State", "Description", "Closed Date", "URL"])
df.to_excel("gitissues.xlsx", index=False)