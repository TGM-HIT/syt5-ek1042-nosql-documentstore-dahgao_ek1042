# NoSQL Documentstore

Team: Gao Simon, Dahmen Felix

## Setup Couchbase with Docker

Run couchbase in docker with the community image

```
docker run -t --name db -p 8091-8096:8091-8096 -p 11210-11211:11210-11211 \
  couchbase:community
```

```
Starting Couchbase Server -- Web UI available at http://<ip>:8091
and logs available in /opt/couchbase/var/lib/couchbase/logs
```

The Web Ui can now be access at `localhost:8091`. Here you can see the Welcome screen
and now you can select `Setup New Cluster` or `Join Existing Cluster`

When creating a new cluster you have to give it a `cluster name`, `admin username` and `password.`
After that accept with the settings you want.


# Resources

[1] - https://docs.couchbase.com/server/current/getting-started/start-here.html; 27.03.2025
