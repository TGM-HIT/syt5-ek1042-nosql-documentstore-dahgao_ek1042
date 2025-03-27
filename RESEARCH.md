# RESEARCH.md

## Couchbase Server

Couchbase[1] ist eine NoSQL Datenbank, die für hohe Performance, Skalierbarkeit und Flexibilität ausgelegt ist. Hier die wichtigsten Punkte zusammengefasst:

- Dokuemtenorientiert: Daten werden als items gespeichert, die einen key und einen value haben. [4]
- SQL++: Ist eine Query Sprache, die fuer Dokumentbasierte Datenbanken gemacht wurde.
- Cluster: Mehrere Server koennen in einen Cluster Zusammengefuehrt werden. Der Cluster Manager koordiniert alle Cluster Aktivitaeten. [2]
- Daten in Memory: Daten koennen einfach nur in RAM oder in RAM und Persistent Storage gespeichert werden. [3]

Couchbase Server hat mehrere services. Diese koennen seperat voneinender deployed, maintained und provisioniert werden.

```
Data: Supports the storing, setting, and retrieving of data-items, specified by key.

Query: Parses queries specified in the SQL++ query-language, executes the queries, and returns results. The Query Service interacts with both the Data and Index services.

Index: Creates indexes, for use by the Query Service.

Search: Creates indexes specially purposed for Full Text Search. This supports language-aware searching; allowing users to search for, say, the word beauties, and additionally obtain results for beauty and beautiful.

Analytics: Supports join, set, aggregation, and grouping operations; which are expected to be large, long-running, and highly consumptive of memory and CPU resources.

Eventing: Supports near real-time handling of changes to data: code can be executed both in response to document-mutations, and as scheduled by timers.

Backup: Supports both the scheduling and the immediate execution of full and incremental data backups, either for specific individual buckets, or for all buckets on the cluster. Also allows the scheduling and immediate execution of merges of previously made backups.

```
[1]


## Ressources

[1] - https://docs.couchbase.com/server/current/learn/architecture-overview.html
[2] - https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets-memory-and-storage.html
[3] - https://docs.couchbase.com/server/current/learn/clusters-and-availability/clusters-and-availability.html
[4] - https://docs.couchbase.com/server/current/learn/data/data.html

