# 🗺️ Data Engineering Learning Path Roadmap

> A structured overview of what you should **know**, **be learning**, and **have mastered** at every stage of your data engineering career — from day-one Junior to top-tier Senior.

---

## How to Read This Roadmap

Each level has three checkpoints:

| Checkpoint | Meaning |
|------------|---------|
| **Before** | Prerequisites — what you should already know or review before entering this level |
| **Middle** | Core competencies — what you're actively building and should be comfortable with halfway through |
| **Advanced** | Mastery — what you should own confidently by the time you graduate from this level |

---

---

# 🟢 JUNIOR DATA ENGINEER

**Tasks 1–100 · ~6–9 months · You are: an individual contributor learning the craft**

Your goal: build production-quality pipelines, write clean SQL & Python, and earn trust from your team.

---

## Before Junior (Prerequisites)

> *What you should know before you write your first line of production code.*

### SQL Fundamentals
- [ ] `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`
- [ ] `JOIN` types: `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`
- [ ] Aggregate functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- [ ] `NULL` handling: `IS NULL`, `COALESCE`, `NULLIF`
- [ ] `DISTINCT`, `LIMIT`, `OFFSET`
- [ ] Basic subqueries (inline and `WHERE … IN (SELECT …)`)
- [ ] `UNION` vs `UNION ALL`

### Python Fundamentals
- [ ] Data types: `str`, `int`, `float`, `bool`, `list`, `dict`, `tuple`, `set`
- [ ] Control flow: `if/elif/else`, `for`, `while`, list comprehensions
- [ ] Functions: parameters, return values, default arguments, `*args`, `**kwargs`
- [ ] File I/O: `open()`, `read()`, `write()`, `with` statement
- [ ] Error handling: `try/except/finally`, common exceptions
- [ ] Modules & imports: `import`, `from … import`, standard library basics
- [ ] Virtual environments: `venv`, `pip install`, `requirements.txt`

### General Computing
- [ ] Terminal/shell basics: `cd`, `ls`, `mkdir`, `cp`, `mv`, `rm`, `cat`, `grep`
- [ ] Git basics: `clone`, `add`, `commit`, `push`, `pull`, `branch`, `merge`
- [ ] What a relational database is (tables, rows, columns, primary keys, foreign keys)
- [ ] What an API is (request/response, HTTP methods, JSON)
- [ ] CSV and JSON file formats — reading and writing them
- [ ] Basic understanding of client-server architecture

### Mindset
- [ ] Curiosity about how data flows through systems
- [ ] Comfort with reading documentation and error messages
- [ ] Willingness to break things in a local/dev environment

---

## Middle Junior (Core Builder — Tasks ~1–50)

> *You can build things. You understand the "what" and are learning the "why."*

### SQL — Intermediate
- [ ] Common Table Expressions (CTEs) — chaining multiple CTEs
- [ ] Window functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`
- [ ] `PARTITION BY` + `ORDER BY` inside window frames
- [ ] `CASE WHEN` for conditional logic and pivoting
- [ ] `EXPLAIN ANALYZE` — reading a query plan to find bottlenecks
- [ ] Indexing: when it helps, when it doesn't
- [ ] Materialized views: when and why to use them
- [ ] Table partitioning (range/list) and partition pruning
- [ ] `MERGE` / `UPSERT` patterns for incremental loads

### Python — Applied Data Engineering
- [ ] `pandas` for data manipulation: read, transform, write
- [ ] `requests` library: calling REST APIs, handling pagination, retries
- [ ] `psycopg2` / `SQLAlchemy` for database connections
- [ ] `logging` module instead of `print()`
- [ ] `pytest` for unit testing pipelines
- [ ] `unittest.mock` / `patch` for mocking external dependencies
- [ ] `pydantic` for data validation and type safety
- [ ] Working with Parquet files via `pyarrow`
- [ ] `YAML` / `JSON` config file parsing

### Data Pipeline Patterns
- [ ] ETL vs ELT — when to use which
- [ ] Idempotent pipeline design (re-runnable without duplicates)
- [ ] Incremental loading: high-watermark pattern, change detection
- [ ] Handling late-arriving data (lookback windows)
- [ ] Error handling: retry logic, dead letter queues, circuit breakers
- [ ] Data deduplication (exact match + fuzzy matching)
- [ ] Backfill pipelines: date-range parameterization

### Tools — Foundational
- [ ] **dbt**: models, `ref()`, sources, YAML config, schema tests, incremental models, macros, snapshots (SCD2)
- [ ] **Airflow**: DAG definition, operators (`Python`, `Bash`, `Branch`), sensors, task dependencies, XCom, scheduling, SLA monitoring, task groups
- [ ] **PySpark** (local mode): DataFrame API, `groupBy`, `agg`, window functions, `Spark SQL`, execution plans

### Data Modeling
- [ ] Star schema: fact tables, dimension tables, grain definition
- [ ] Slowly Changing Dimensions: SCD Type 1 (overwrite), Type 2 (history), Type 3 (previous value)
- [ ] Surrogate keys vs natural keys
- [ ] Data Vault basics: Hubs, Links, Satellites

### Data Quality
- [ ] Schema validation (column names, types, not-null)
- [ ] Row-count checks, freshness monitoring
- [ ] **Great Expectations**: expectation suites, checkpoints, data docs
- [ ] dbt tests: `unique`, `not_null`, `accepted_values`, `relationships`, custom tests

---

## Advanced Junior (Graduating — Tasks ~50–100)

> *You can own features end-to-end. You write production code that others can maintain. You're ready for more responsibility.*

### SQL — Advanced
- [ ] Recursive CTEs and graph traversal
- [ ] Window function frame specifications (`ROWS BETWEEN`, `RANGE BETWEEN`)
- [ ] `FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE`
- [ ] SCD Type 6 (hybrid — combining Types 1, 2, 3)
- [ ] Complex reconciliation queries (`FULL OUTER JOIN` + set difference)

### Python — Professional Grade
- [ ] Generators and `itertools` for memory-efficient processing
- [ ] Context managers (`contextlib`, `__enter__`/`__exit__`)
- [ ] Project structure: `pyproject.toml`, packages, `__init__.py`
- [ ] CLI tools with `click` or `typer`
- [ ] Type hints throughout codebase

### Architecture & Design
- [ ] Data pipeline dependency graphs and critical path analysis
- [ ] Metadata-driven pipeline frameworks (config → DAGs)
- [ ] Data contracts: schema versioning, backward compatibility
- [ ] Schema registry concepts (store, version, validate schemas)
- [ ] Event-driven pipeline triggers (file watchers, webhooks, Airflow Datasets)
- [ ] Pipeline versioning and release management

### Operational Excellence
- [ ] Writing runbooks and incident response procedures
- [ ] Data lineage tracking (automated SQL parsing with `sqlglot`)
- [ ] Cost estimation for pipeline runs
- [ ] Writing a blameless postmortem / incident report
- [ ] Regression testing: metric baselines + tolerance comparisons
- [ ] Anomaly detection: Z-scores, moving averages on row counts/metrics

### Communication & Career
- [ ] Code review: giving and receiving constructive feedback
- [ ] Technical design documents (problem → options → decision → implementation)
- [ ] Building a data engineering portfolio
- [ ] Preparing a promotion case with evidence
- [ ] Teaching/presenting technical topics to peers

### Capstone Ability
- [ ] Build a complete end-to-end pipeline: ingest → transform → model → serve → monitor
- [ ] Own the SLA, quality, documentation, and alerting for a production feature
- [ ] Write a technical design doc that a senior engineer would approve

---

---

# 🟡 MID-LEVEL (MEDIOR) DATA ENGINEER

**Tasks 101–200 · ~9–12 months · You are: a technical leader who designs systems and mentors others**

Your goal: design distributed systems, own cross-team projects, drive data platform decisions, and prepare for senior.

---

## Before Medior (Prerequisites)

> *What you should be solid on before starting mid-level work. (This is essentially what an Advanced Junior has mastered.)*

### Cloud & Infrastructure
- [ ] At least one cloud provider (AWS or GCP) — basic services: storage, compute, IAM
- [ ] What S3/GCS is and how object storage differs from block storage
- [ ] Docker basics: `Dockerfile`, `docker-compose`, building images, running containers
- [ ] Environment configuration: `.env` files, secrets management, 12-factor app principles

### Data Engineering Core
- [ ] Production Airflow DAGs with error handling, retries, SLAs
- [ ] dbt project: incremental models, tests, snapshots, macros, packages
- [ ] PySpark: DataFrames, SQL, joins, basic performance tuning
- [ ] SQL mastery: window functions, CTEs, optimization, partitioning
- [ ] Python mastery: testing, packaging, clean code, type hints
- [ ] Data modeling: star schema, SCD, Data Vault awareness

### Patterns & Practices
- [ ] Idempotent and incremental pipeline patterns
- [ ] Data quality frameworks (Great Expectations or equivalent)
- [ ] Monitoring/alerting for pipeline health
- [ ] Data lineage and catalog concepts
- [ ] Technical design documents and runbooks

### Soft Skills
- [ ] Comfortable writing about technical decisions
- [ ] Can explain your pipeline to a non-technical stakeholder
- [ ] Can review another engineer's code constructively

---

## Middle Medior (Platform Builder — Tasks ~101–130)

> *You design cloud infrastructure, build streaming pipelines, and start leading cross-team initiatives.*

### Cloud Data Platforms
- [ ] **Snowflake**: architecture (virtual warehouses, storage, services), stages, `COPY`, Snowpipe, clustering keys, warehouse sizing, caching layers, `ACCOUNT_USAGE` views
- [ ] **BigQuery** or alternative: partitioning, clustering, slot management, cost model
- [ ] Cloud data loading: bulk load vs continuous ingestion, file formats (Parquet, Avro, JSON)
- [ ] Cloud Spark: **AWS EMR** / **GCP Dataproc** — cluster sizing, spot/preemptible instances, auto-scaling

### Streaming & Real-Time
- [ ] **Apache Kafka**: topics, partitions, consumer groups, offset management, producer/consumer API
- [ ] **Debezium**: CDC from PostgreSQL/MySQL WAL → Kafka Connect
- [ ] **Flink SQL** or **Spark Structured Streaming**: windowing (tumbling, sliding, session), watermarks, stream-table joins
- [ ] Exactly-once semantics: Kafka Transactions API, idempotent producers, deduplication strategies
- [ ] Stateful stream processing: session windows, hopping windows, state backends

### Data Architecture
- [ ] **Medallion architecture**: Bronze/Silver/Gold layers, quality gates between layers
- [ ] **Delta Lake** / **Apache Iceberg**: ACID on data lakes, time travel, schema evolution
- [ ] **Event sourcing**: immutable event logs, CQRS pattern, event replay
- [ ] **Data Mesh**: domain ownership, data products, federated governance

### Infrastructure & DevOps
- [ ] **Terraform**: providers, resources, modules, state management, `plan` → `apply` workflow
- [ ] **CI/CD for data**: GitHub Actions, automated dbt testing, Docker-based deployments, staging → production promotion
- [ ] **Observability**: Prometheus + Grafana, SLIs/SLOs, unified dashboards, PagerDuty/Slack alerting

### Advanced dbt
- [ ] Multi-project architecture: cross-project `ref()`, model access modifiers (`public`, `protected`, `private`)
- [ ] dbt contracts: column-level type enforcement
- [ ] Advanced macros and package development

### Cost & Governance
- [ ] Cloud cost optimization: Snowflake `ACCOUNT_USAGE`, warehouse scheduling, auto-suspend, materialized view cost/benefit
- [ ] **Data governance**: PII classification (public/internal/confidential/restricted), Snowflake dynamic masking, tagging
- [ ] GDPR compliance: right-to-erasure, data retention policies, cross-region data residency

### Leadership Foundations
- [ ] **Mentoring**: onboarding plans, code review templates, growth tracking for a junior
- [ ] **Technical estimation**: work breakdown structures, risk buffers, Fibonacci-based sizing
- [ ] **Cross-team design**: writing data contracts, coordinating schemas across service boundaries
- [ ] Multi-region data replication: Snowflake replication, Kafka MirrorMaker

### Resilience Engineering
- [ ] **Chaos engineering**: fault injection, failure mode testing, pipeline resilience verification
- [ ] Data platform APIs: **FastAPI** endpoints with rate limiting, caching (Redis), versioning, auth

---

## Advanced Medior (Senior-Ready — Tasks ~131–200)

> *You can design entire data platforms, make architectural decisions, and operate systems at scale. You're preparing for Senior.*

### Advanced Analytics Engineering
- [ ] **Semantic layer**: dbt MetricFlow / Cube.js — metric definitions, governed analytics, single source of truth
- [ ] **Complex Event Processing**: Flink CEP, multi-event pattern matching, real-time fraud/anomaly detection
- [ ] Schema evolution strategies: Schema Registry, Avro forward/backward compatibility, safe migration playbooks

### Platform Engineering
- [ ] **DAG factory**: YAML-driven self-serve pipeline generation, metaprogramming Airflow
- [ ] **Flink state machines**: `KeyedProcessFunction`, timers, order lifecycle tracking, SLA enforcement
- [ ] **Reverse ETL**: data activation to Braze/Algolia/Google Ads, change detection, rate-limited batching
- [ ] **Self-service data portal**: Streamlit/FastAPI, data catalog UI, query builder, metric request forms

### Contracts & Quality at Scale
- [ ] **Data contracts enforcement**: YAML contract specs, automated validation at ingestion, violation routing
- [ ] **Property-based testing**: Hypothesis library, Schemathesis for API fuzzing, edge-case generation
- [ ] **Idempotent patterns**: SQL `MERGE`, partition overwrite, dbt incremental dedup, checkpoint recovery

### ML & Advanced Operations
- [ ] **ML pipeline orchestration**: Airflow → feature engineering → training → MLflow registry → deployment gates
- [ ] **Multi-cloud strategy**: Snowflake across AWS/GCP/Azure, Apache Iceberg + Polaris catalog, cost arbitrage
- [ ] **Performance profiling**: Airflow Gantt charts, Snowflake query profiles, Spark UI, critical path optimization

### Architecture & Documentation
- [ ] **Architecture Decision Records (ADRs)**: structured decision documentation, trade-off matrices
- [ ] **Data product lifecycle**: discovery → development → GA → deprecation → retirement, usage tracking
- [ ] **Technical writing**: design doc standards, style guides, audience-appropriate documentation

### Business Continuity
- [ ] **Disaster recovery**: Snowflake failover groups, RTO/RPO definitions, DR runbooks, regional failover testing
- [ ] **Real-time data warehouse**: Snowpipe Streaming, Dynamic Tables, sub-5-minute dashboard freshness

### Senior Interview Prep
- [ ] **System design**: back-of-envelope estimation, scaling to 1M events/sec, cost modeling, architecture trade-offs
- [ ] End-to-end platform capstone: executive BI dashboard with semantic layer, data contracts, quality SLAs, observability

---

---

# 🔴 SENIOR DATA ENGINEER

**Tasks 201–300 · ~12+ months · You are: a technical leader who shapes strategy, builds teams, and drives org-wide impact**

Your goal: define the data platform vision, make decisions that scale to years, grow people, and influence beyond your team.

---

## Before Senior (Prerequisites)

> *What you should be solid on before claiming the Senior title. (This is what an Advanced Medior has mastered.)*

### System Design
- [ ] Design a data platform handling 1M+ events/sec with cost constraints
- [ ] Trade-off analysis: consistency vs availability, batch vs stream, buy vs build
- [ ] Multi-region, multi-cloud architecture reasoning
- [ ] Disaster recovery planning with defined RTO/RPO

### Technical Depth
- [ ] Deep expertise in at least 2 of: Snowflake, Spark, Kafka, Flink, dbt
- [ ] Production experience with streaming AND batch at scale
- [ ] Infrastructure as Code (Terraform) and CI/CD pipeline design
- [ ] Observability: SLIs/SLOs, alerting strategy, cost monitoring
- [ ] Data governance, security, compliance (GDPR, PII handling)

### Leadership
- [ ] Mentored at least 1–2 engineers through measurable growth
- [ ] Led cross-team technical initiatives end-to-end
- [ ] Written ADRs and design docs that influenced team direction
- [ ] Estimated, planned, and delivered multi-sprint projects

### Communication
- [ ] Can present architecture to VP/C-level in business terms
- [ ] Can write a 1-pager that non-engineers understand
- [ ] Can run a blameless postmortem and drive follow-up actions

---

## Middle Senior (Technical Leader — Org-Level Impact)

> *You define architecture standards, build internal platforms, and multiply team output.*

### Platform Architecture
- [ ] Internal Developer Platform (IDP): self-service infrastructure for data teams
- [ ] API gateway design for the data platform: versioning, auth, rate limiting, SDKs
- [ ] Data platform SDK/CLI: internal tooling that accelerates team velocity
- [ ] Event-driven architecture at scale: event schemas, event bus, consumer patterns

### Advanced Streaming
- [ ] Exactly-once end-to-end guarantees across distributed systems
- [ ] Stateful stream processing at production scale (millions of keys, state backend tuning)
- [ ] Real-time ML feature serving: low-latency feature stores, online/offline consistency
- [ ] Stream processing cost optimization: parallelism tuning, state TTL, checkpoint intervals

### Data Strategy
- [ ] Technical roadmap creation: 6–12 month data platform vision
- [ ] Build vs buy analysis: vendor evaluation, POC frameworks, migration planning
- [ ] Data mesh implementation: domain team enablement, data product standards, governance federation
- [ ] Statistical process control for data pipelines: control charts, drift detection

### Reliability Engineering
- [ ] SRE for data: error budgets, toil reduction, capacity planning
- [ ] Anomaly detection at scale: automated monitoring across 1000+ pipelines
- [ ] Zero-downtime migration strategies: dual-write, shadow pipelines, canary deployments
- [ ] Performance regression detection: automated benchmarking in CI/CD

### People & Process
- [ ] Architecture review facilitation: running design reviews, giving actionable feedback
- [ ] Team building: hiring, interview design, onboarding programs
- [ ] Cross-functional collaboration: aligning data platform with product, ML, analytics teams
- [ ] Technical debt management: prioritization frameworks, migration planning, tech debt sprints

---

## Advanced Senior (Staff-Track / Principal-Ready)

> *You shape the engineering culture, make decisions with multi-year impact, and are the go-to person for the hardest problems.*

### Strategic Architecture
- [ ] Multi-year platform evolution roadmaps with migration paths
- [ ] Org-wide data strategy: governance models, data democratization framework
- [ ] Cost modeling at scale: FinOps practices, budget forecasting, cloud contract negotiation input
- [ ] Evaluating emerging technologies: lakehouse evolution, real-time OLAP (ClickHouse, StarRocks, DuckDB), AI-native data stacks

### Distributed Systems Mastery
- [ ] CAP theorem applied: choosing consistency models per use case
- [ ] Consensus protocols awareness: Raft, Paxos (conceptual — know when they matter)
- [ ] Exactly-once across service boundaries: saga patterns, outbox pattern, 2PC trade-offs
- [ ] Backpressure management and flow control in distributed pipelines

### Organization Building
- [ ] Defining engineering levels, career ladders, and growth frameworks for data engineers
- [ ] Running guilds/communities of practice across teams
- [ ] Writing RFCs that influence company-wide technical direction
- [ ] Speaking at meetups/conferences — representing the engineering brand

### Advanced Operations
- [ ] Chaos engineering program design (not just running — designing the program)
- [ ] Disaster recovery program ownership: quarterly DR drills, compliance audits
- [ ] Regulatory compliance at scale: SOC 2, HIPAA, cross-border data transfer frameworks
- [ ] Incident management maturity: severity definitions, escalation paths, SLA tracking

### Innovation & Influence
- [ ] Prototyping next-generation architectures (streaming-first, AI pipelines, vector databases)
- [ ] Open-source contribution or internal framework development
- [ ] Mentoring mid-level engineers into senior roles
- [ ] Building a reputation as a trusted technical advisor beyond your immediate team

---

---

# 📊 Quick Reference Matrix

| Level | Before | Middle | Advanced |
|-------|--------|--------|----------|
| **Junior** | SQL basics, Python basics, Git, terminal, file formats | dbt, Airflow, PySpark, star schema, data quality, testing | E2E ownership, design docs, lineage, anomaly detection, teaching |
| **Medior** | Cloud basics, Docker, production pipelines, data modeling | Snowflake, Kafka, Flink, Terraform, CI/CD, mentoring, governance | Semantic layers, ML ops, DR, platform engineering, system design |
| **Senior** | System design, multi-cloud, deep tool expertise, leadership | IDP, tech roadmaps, SRE for data, team building, data strategy | Multi-year architecture, org-wide influence, FinOps, Staff-track |

---

# 🔗 Mapping to NovaMart Tasks

| Career Stage | Task Range | Key Milestone |
|-------------|-----------|---------------|
| Before Junior | Pre-requisites | Self-study |
| Middle Junior | Tasks 1–50 | Midpoint capstone (Task 50) |
| Advanced Junior | Tasks 51–100 | Junior graduation (Task 100) |
| Before Medior | Review & prep | Gap assessment |
| Middle Medior | Tasks 101–130 | Architecture checkpoint (Task 120), Migration capstone (Task 130) |
| Advanced Medior | Tasks 131–200 | BI capstone (Task 150), Senior prep complete (Task 200) |
| Before Senior | Review & prep | Gap assessment |
| Middle Senior | Tasks 201–250 | Platform ownership |
| Advanced Senior | Tasks 251–300 | Staff-track readiness |

---

> **You are here: Task 1** — Start with the "Before Junior" checklist above. If you can check off most items, you're ready. If not, spend a few days reviewing those fundamentals — it'll make everything that follows much smoother.
