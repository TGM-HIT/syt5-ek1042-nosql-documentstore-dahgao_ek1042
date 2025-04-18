# NoSQL Documentstore

Team: Gao Simon, Dahmen Felix

## Setup Couchbase Cluster

Run couchbase in docker with the community image.

```
docker compose up -d
```

```
Starting Couchbase Server -- Web UI available at http://<ip>:8091
and logs available in /opt/couchbase/var/lib/couchbase/logs
```

The Web Ui can now be access at `localhost:8091`. Here you can see the Welcome screen
and now you can select `Setup New Cluster` or `Join Existing Cluster`

When creating a new cluster you have to give it a `cluster name`, `admin username` and `password.`
After that accept with the settings you want.

## Join Cluster with a New Node

This tutorial [2] can also be used

Run a second couchbase container in docker with the community image.

```
docker compose up -d
```


1. Acccess the new node Couchbase Web Console instance on `<ip>:8091`.
2. Click on the Join Existing Cluster button.
3. Enter the `ip`, `admin user` and `password` for the first node and cluster
4. Click Join Cluster

## Deploy Python FastAPI App

Create `.env` with variables:
```
IP=<ip>
COUCH_USER=<username>
COUCH_PASSWORD=<password>
```

Install python dependencies:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Execute the app:
```
python main.py
```

## CRUD

The endpoints is `localhost:8000/{key}`, with POST, GET, PUT, DELETE for CRUD.
For Create and Update, the value is passed with the http body.


# Resources

[1] - https://docs.couchbase.com/server/current/getting-started/start-here.html; 27.03.2025

[2] - https://docs.couchbase.com/server/current/manage/manage-nodes/join-cluster-and-rebalance.html; 27.03.2025
