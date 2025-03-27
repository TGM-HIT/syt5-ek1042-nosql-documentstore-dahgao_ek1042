# RESEARCH.md

## Couchbase Server

Couchbase[1] ist eine NoSQL-Datenbank, die für hohe Performance, Skalierbarkeit und Flexibilität entwickelt wurde. Hier die wichtigsten Punkte zusammengefasst:

- **Dokumentenorientiert**: Daten werden als Items gespeichert, die aus einem Key und einem Value bestehen.[4]  
- **SQL++**: Eine Abfragesprache, die speziell für dokumentenbasierte Datenbanken entwickelt wurde.  
- **Cluster**: Mehrere Server können zu einem Cluster zusammengeschlossen werden. Der Cluster Manager koordiniert alle Cluster-Aktivitäten.[2]  
- **Daten in Memory**: Daten können entweder ausschließlich im RAM oder sowohl im RAM als auch im persistenten Speicher abgelegt werden.[3]  

Couchbase Server bietet verschiedene Services, die unabhängig voneinander bereitgestellt, gewartet und skaliert werden können:

```
Data: Unterstützt das Speichern, Setzen und Abrufen von Daten-Items, die durch einen Key spezifiziert werden.

Query: Verarbeitet Abfragen in der SQL++-Abfragesprache, führt sie aus und liefert Ergebnisse. Der Query Service interagiert mit den Data- und Index-Services.

Index: Erstellt Indizes zur Nutzung durch den Query Service.

Search: Erstellt spezielle Indizes für die Volltextsuche. Dies ermöglicht sprachbewusstes Suchen, sodass Nutzer z. B. nach „beauties“ suchen und auch Treffer für „beauty“ und „beautiful“ erhalten.

Analytics: Unterstützt Join-, Set-, Aggregations- und Gruppierungsoperationen, die typischerweise groß, langwierig und ressourcenintensiv (Speicher und CPU) sind.

Eventing: Ermöglicht die nahezu Echtzeit-Verarbeitung von Datenänderungen: Code kann als Reaktion auf Dokumentmutationen oder zeitgesteuert ausgeführt werden.

Backup: Unterstützt die Planung und sofortige Ausführung von vollständigen und inkrementellen Datensicherungen – entweder für einzelne Buckets oder alle Buckets im Cluster. Auch das Zusammenführen zuvor erstellter Backups ist möglich.
```

[1]

## Cluster Funktionalitaeten

- Cluster: Ein Couchbase-Cluster besteht aus mehreren Knoten (Servern),
    die zusammenarbeiten, um Daten zu speichern und zu verwalten. Dies ermöglicht Skalierbarkeit und Ausfallsicherheit.
- Verfügbarkeit: Couchbase sorgt für hohe Verfügbarkeit durch Replikation (Daten werden auf mehreren Knoten gespeichert) und automatische Failover-Mechanismen, falls ein Knoten ausfällt.
- Datenverteilung: Daten werden über "vBuckets" gleichmäßig auf die Knoten verteilt, um Last und Speicher effizient zu nutzen.
- Rebalancierung: Bei Änderungen im Cluster (z. B. Hinzufügen/Entfernen von Knoten) werden Daten automatisch neu verteilt, ohne Ausfallzeiten.

Das System ist darauf ausgelegt, auch bei Hardwarefehlern oder Wartungsarbeiten kontinuierlich verfügbar zu bleiben.
[3]


## Ressources

[1] - https://docs.couchbase.com/server/current/learn/architecture-overview.html; 27.03.2025

[2] - https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets-memory-and-storage.html; 27.03.2025

[3] - https://docs.couchbase.com/server/current/learn/clusters-and-availability/clusters-and-availability.html; 27.03.2025

[4] - https://docs.couchbase.com/server/current/learn/data/data.html; 27.03.2025
