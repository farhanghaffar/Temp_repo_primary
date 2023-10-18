

const { Octokit } = require('@octokit/rest');

(async () => {
  try {
    const octokit = new Octokit({
      auth: process.env.GITHUB_TOKEN,
    });

    const owner = 'farhanghaffar'; // Replace with the actual owner of the secondary repository
    const repo = 'temp_repo_secondary'; // Replace with the actual name of the secondary repository
    const workflowId = '72571241'; // Replace with the ID of the workflow in the secondary repository
    const mainBranch = 'main'; // Replace with the name of the main branch in the secondary repository

    const { data: workflowRuns } = await octokit.actions.listWorkflowRuns({
      owner: owner,
      repo: repo,
      status: 'queued',
    });

    if (workflowRuns.total_count === 0) {
      await octokit.actions.createWorkflowDispatch({
        owner: owner,
        repo: repo,
        workflow_id: workflowId,
        ref: mainBranch,
      });
    }
  } catch (error) {
    console.error('An error occurred: ', error);
  }
})();
