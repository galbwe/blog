#! /bin/bash
docker run                                  \
 -d                                         \
 --rm                                       \
 --name ghost-dev                           \
 -e url=http://localhost:2368               \
 -p 2368:2368                               \
 ghost