#! /bin/bash
docker run                                  \
 -d                                         \
 --rm                                       \
 --name ghost-dev                           \
 -e url=http://localhost:2368               \
 -p 2368:2368                               \
 ghost;
# site needs time to start up
echo "Waiting for ghost cms to start.";
sleep 10;
# delete ghost user and copy post data from the production environment
node ./scripts/setup-dev.js