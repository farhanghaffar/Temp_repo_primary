import os

from github import Github
from github import Auth

auth = Auth.Token("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")

owner = 'FarhanGhaffar'
repo_name = 'temp_repo_secondary'
workflow_id = '72571241'
main_branch = 'main'

github_access_token = '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'
g = Github(auth=auth)

repo = g.get_user(owner).get_repo(repo_name)

workflow_runs = repo.get_workflow_runs(event = 'queued')

if workflow_runs.totalCount == 0:
    repo.get_workflow(workflow_id).create_dispatch(ref=main_branch)
