const GhostAdminApi = require('@tryghost/admin-api')


const admin = new GhostAdminApi({
    url: process.env.GHOST_URL,
    key: process.env.ADMIN_API_KEY,
    version: "v3"
  });

function fetch_all_posts (api){
    const data = api.posts.browse()
        .then(res => {
            return JSON.stringify(res);
        })
        .catch(error => {
            console.log(error);
        })
    return data;
}

fetch_all_posts(admin)
    .then(d => console.log(d))