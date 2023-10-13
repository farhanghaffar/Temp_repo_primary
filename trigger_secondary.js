const { Octokit } = require('@octokit/rest');

(async () => {
  try {
    const octokit = new Octokit({
      auth: process.env.GITHUB_TOKEN,
    });

    const { data: pullRequest } = await octokit.pulls.get({
      owner: process.env.GITHUB_REPOSITORY.split('/')[0],
      repo: process.env.GITHUB_REPOSITORY.split('/')[1],
      pull_number: process.env.GITHUB_EVENT_NUMBER,
    });

    const { data: workflowRuns } = await octokit.actions.listWorkflowRuns({
      owner: "farhanghaffar",
      repo: "temp_repo_secondary",
      status: "queued",
    });

    if (workflowRuns.total_count === 0) {
      await octokit.actions.createWorkflowDispatch({
        owner: "farhanghaffar",
        repo: "temp_repo_secondary",
        workflow_id: "deploy",
        ref: "MAIN_BRANCH",
        inputs: {
          pull_request_number: pullRequest.number,
        },
      });
    }
  } catch (error) {
    console.error('An error occurred: ', error);
  }
})();
