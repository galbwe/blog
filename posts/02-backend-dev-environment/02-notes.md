Options for backing up posts:

- Need a service that regularly gets all data from the ghost rest api and writes it to a storage service.
- Whatever machine runs the job should be ephemeral. I don't want it sitting around going unused.

Questions:

1. Which storage service should I use?
- cloud storage - just dump the json files
- cloud sql
- firestore
2. How should I schedule the periodic task?
    - celery beat
    - cron
    - cloud scheduler calling a REST endpoint

    - looks like its possible to just run a cron job on the server


Things to talk about:
- Cloud Scheduler
- cron syntax
- cloud storage
- Ghost REST API

- Steps:

1. Set up a development CMS
1. Export data manually from live CMS and import into development CMS
1. Learn how to make requests to a rest api running on localhost