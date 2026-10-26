# The containers

Everything the demo ran, on one 15 GB laptop. Three groups, started in this order.

| Group | Containers | Defined in |
|---|---|---|
| the source | Oracle XE 21c with the iDempiere 12 seed (`ekos-oracle-xe-1`) | [`testbed/`](../testbed/) |
| the lakehouse | Trino 483 (with the `idempiere` Oracle catalog), Apache Polaris (Iceberg REST catalog), SeaweedFS (S3), PostgreSQL (Polaris's store) | [`src/ekos-lakehouse/deploy/docker-compose.lakehouse.yml`](../src/ekos-lakehouse/deploy/docker-compose.lakehouse.yml) |
| the orchestrator | Dagster over the generated pipeline | [`docker-compose.dagster.yml`](docker-compose.dagster.yml) |

The EKOS console and the `ekos-lakehouse` binary run on the host.

```bash
git clone --recurse-submodules https://github.com/alexeyban/ekos-lakehouse-oracle && cd ekos-lakehouse-oracle

# 1. The source: Oracle XE + the iDempiere seed, a read-only user `ekos_ro` (≈ 2.5 GB RAM, 20 min the first time)
docker compose -p ekos -f testbed/docker-compose.oracle.yml up -d
testbed/idempiere-oracle.sh

# 2. The lakehouse sandbox, and Oracle on its network (Trino reads ADEMPIERE through the `idempiere` catalog)
docker compose -f src/ekos-lakehouse/deploy/docker-compose.lakehouse.yml up -d
docker network connect ekos-lakehouse_default ekos-oracle-xe-1

# 3. The binary: EKOS + EKOS Lakehouse with the Oracle driver (Oracle Instant Client 23 on LD_LIBRARY_PATH)
cargo build --release --features oracle --manifest-path src/ekos-lakehouse/Cargo.toml -p ekos-lakehouse
export PATH=$PWD/src/ekos-lakehouse/target/release:$PATH LD_LIBRARY_PATH=<instantclient_23_*>
export EKOS_ORACLE_PASSWORD=ekos-ro-local-only

# 4. The project (project/ekos.toml, paths filled in), then the console
ekos-lakehouse project add idemdocs --source <idempiere checkout>
cp project/ekos.toml ~/.ekos/data/default/idemdocs/ekos.toml     # edit <idempiere>, <idempiere-docs>
ekos-lakehouse console start && ekos-lakehouse console open      # steps 1–7 from the browser
# (the console ships in the release package, `src/ekos-lakehouse/install.sh`; from source it is
#  src/EKOS/web — see src/EKOS/docs/deployment.md)

# 5. The orchestrator, once step 5 is approved and the pipeline generated (steps 6–7)
docker build -t ekos-lakehouse/dagster:1.13.26 src/ekos-lakehouse/deploy/dagster
EKOS_LH_PROJECT=~/.ekos/data/default/idemdocs EKOS_LAKEHOUSE_BIN=$(command -v ekos-lakehouse) \
ORACLE_INSTANT_CLIENT=<instantclient_23_*> docker compose -f stack/docker-compose.dagster.yml up -d
```

**Memory.** Oracle ≈ 2.5 GB, Trino 2 GB (its limit), Dagster ≤ 2.5 GB, the console and a pipeline command 1–3 GB
each. On 15 GB the full 849-table load was not run (RFC 0227): a 165-table subset was, through one-shot Dagster runs.

**Passwords** in these files are local-only defaults (`ekos-ro-local-only`, `polaris-local-only`, …) for services
bound to 127.0.0.1. A real deployment sets the variables; EKOS stores only their names.

**Schedules.** The generated Dagster definitions start their schedules switched on: the first hourly tick launches
the full extraction. Stop them first on a test machine.
