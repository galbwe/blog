# Ghost Blog

Ghost CMS and utility scripts for a personal blog hosted on Google Cloud Platform.


# Development Setup

1. Install node
2. create a .env file with the following contents:
```
export GHOST_COMPUTE_ENGINE_INSTANCE="ghost-blog"
export DEVELOP_URL="http://localhost:2368"
export PROD_URL=<your ghost instance url>
export PROD_API_KEY=<your ghost admin api key>
```
3. Source the env file `source .env`
4. `npm install`
5. Start ghost in a docker container: `npm run ghost`
6. Check that Ghost is running at on [localhost port 2368](http://localhost:2368)