const { Octokit } = require("@octokit/rest");

const owner = 'FarhanGhaffar';
const repo = 'temp_repo_secondary';
const workflowId = '72571241';
const mainBranch = 'main';

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

async function createWorkflowDispatch() {
  const { data: workflowRuns } = await octokit.actions.listWorkflowRuns({
    owner,
    repo,
    event: 'push',
    branch: 'main',
  });

  if (workflowRuns.total_count === 0) {
    await octokit.actions.createWorkflowDispatch({
      owner,
      repo,
      workflow_id: workflowId,
      ref: mainBranch,
    });
  }
}

createWorkflowDispatch();
