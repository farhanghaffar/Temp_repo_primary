const { Octokit } = require("@octokit/core");
const { createAppAuth } = require("@octokit/auth-app");

const owner = 'FarhanGhaffar';
const repoName = 'temp_repo_secondary';
const workflowId = '72571241';
const mainBranch = 'main';

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

async function createWorkflowDispatch() {
  const { data: workflowRuns } = await octokit.request('GET /repos/{owner}/{repo}/actions/runs', {
    owner,
    repo: repoName,
    event: 'queued'
  });

  if (workflowRuns.total_count === 0) {
    await octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
      owner,
      repo: repoName,
      workflow_id: workflowId,
      ref: mainBranch
    });
  }
}

createWorkflowDispatch();
