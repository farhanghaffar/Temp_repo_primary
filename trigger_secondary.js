const { Octokit } = require('@octokit/rest');

async function triggerRerun() {
  const octokit = new Octokit({
    auth: process.env.GITHUB_TOKEN
  });

  try {
    const response = await octokit.request('POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun', {
      owner: 'farhanghaffar',
      repo: 'temp_repo_secondary',
      job_id: '72571241',
      headers: {
        'X-GitHub-Api-Version': '2022-11-28'
      }
    });
    console.log(response.data); // Assuming you want to log the response data
  } catch (error) {
    console.error('Error occurred:', error);
  }
}

triggerRerun();
