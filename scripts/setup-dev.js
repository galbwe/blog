const fetch = require("node-fetch");
const GhostAdminApi = require("@tryghost/admin-api");


var session = {
    "cookie": "",
    "ghostUserId": null,
}

const adminApi = GhostAdminApi({
    "url": process.env.PROD_URL,
    "key": process.env.PROD_API_KEY,
    "version": "v3",
})


function createSiteOwner(baseUrl, callback) {
  console.log("In createSiteOwner")
  const url = baseUrl + "/ghost/api/v3/admin/authentication/setup/";
  const body = {
    setup: [
      {
        name: "Wes Galbraith",
        email: "galbwe92@gmail.com",
        password: "supersafe!",
        blogTitle: "Test Site",
      },
    ],
  };
  const headers = {
      'Content-Type': 'application/json',
  }
  const options = {
    method: 'POST',
    body: JSON.stringify(body),
    headers: headers,
  }
  fetch(url, options)
    .then((res) => res.json())
    .then((json) => console.log(JSON.stringify(json)))
    .then(callback)
    .catch((error) => console.log(error));
}


function createSession(baseUrl, callback) {
    console.log("In createSession")
    const url = baseUrl + "/ghost/api/v3/admin/session";
    const body = {
        username: "galbwe92@gmail.com",
        password: "supersafe!",
    }
    const headers = {
        'Content-Type': 'application/json',
        Cookie: "ghost-admin-api-session=s%3AaZF6vitKnfA3Du5BoD8l9DXon1NWHWPx.IR8CPKQH294Z2hYY8dGW9xHsJ2N68RTShiq2stQSKXQ;",
    }
    const options = {
        method: 'POST',
        body: JSON.stringify(body),
        headers: headers,
    }
    fetch(url, options)
        .then((res) => {
            console.log('status: ', res.status);
            console.log('headers: ', res.headers);
            console.log('set-cookie: ', res.headers.get('set-cookie'));
            session.cookie = res.headers.get('set-cookie');
        })
        .then(callback)
        .catch(error => console.log(error))
}

function getGhostUserId(baseUrl, callback) {
    console.log("In getGhostUserId");
    const url = baseUrl + "/ghost/api/v3/admin/users/?limit=all";
    const headers = {
        cookie: session.cookie,
    }
    const options = {
        headers: headers
    }
    fetch(url, options)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            data.users.forEach(user => {
                if (user.name === "Ghost") {
                    session.ghostUserId = user.id;
                }
            });
        })
        .then(callback)
        .catch(err => console.log(err))
}


function deleteGhostUser(baseUrl, callback) {
    console.log("In deleteGhostUser")
    const url = baseUrl + `/ghost/api/v3/admin/users/${session.ghostUserId}/`
    const headers = {
        cookie: session.cookie,
    }
    const options = {
        method: 'DELETE',
        headers: headers,
    }
    fetch(url, options)
        .then(res => {
            console.log('status: ', res.status)
            return res.text();
        })
        .then(text => console.log(text))
        .then(callback)
        .catch(err => console.log(err))
}


function copyPostData(devUrl, prodApi) {
    console.log("In copyPostData")
    const url = devUrl + '/ghost/api/v3/admin/posts/';
    const headers = {
        cookie: session.cookie,
        "Content-type": "application/json",
    }
    prodApi.posts.browse()
        .then(res => {
            console.log('prod posts: ', JSON.stringify(res));
            const posts = res.map(post => {
                delete post.id
                delete post.uuid
                delete post.comment_id
                return post
            })
            posts.forEach(post => {
                const body = {
                    posts: [post]
                }
                const options = {
                    method: 'POST',
                    headers: headers,
                    body: JSON.stringify(body),
                }
                fetch(url, options)
                    .then((res) => {
                        return res.text()
                    })
                    .then(text => console.log('text: ', text))
                    .catch(err => console.log(err));
            })
        })
        .catch(err => console.log(err))
}


function setUpDevelopmentSite() {
    console.log('In setUpDevelopmentSite');
    const baseUrl = process.env.DEVELOP_URL;
    createSiteOwner(baseUrl, () => {
        createSession(baseUrl, () => {
            console.log('session: ', session);
            getGhostUserId(baseUrl, () => {
                deleteGhostUser(baseUrl, () => {
                    copyPostData(baseUrl, adminApi);
                })
            })
        })
    });
}

console.log('session: ', session);
setUpDevelopmentSite();
console.log('session: ', session);



