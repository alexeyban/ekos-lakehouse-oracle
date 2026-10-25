# 1. The testbed: iDempiere 12 on Oracle XE

Everything here ran on one laptop (15 GB RAM) against the database iDempiere's own release seed creates.

```bash
# Oracle XE 21c (gvenzl/oracle-xe:21.3.0-slim), port bound to loopback, ~2 GB RAM.
# -p ekos keeps the container name the import script expects (ekos-oracle-xe-1).
docker compose -p ekos -f testbed/docker-compose.oracle.yml up -d

# Downloads idempiereServer12 once (SHA-256 pinned), runs iDempiere's own import inside the
# container (3 min), then creates the read-only user EKOS connects as.
testbed/idempiere-oracle.sh
export EKOS_ORACLE_PASSWORD=ekos-ro-local-only     # the script's local-only default
```

What the database holds after the import ([census](../results/census.md)): 903 tables, 160 views, 2,109 indexes,
48 functions, 14 procedures, 30,457 columns, 3,686 foreign keys, 12,958 check constraints, 0 invalid objects.

The other two sources are plain git clones:

| Source | Repository | Revision used |
|---|---|---|
| `idempiere` | https://github.com/idempiere/idempiere | `3355eb5` (2026-10-09) |
| `docs` | https://github.com/idempiere/idempiere.github.io | `3959ece` (2026-10-20) |

EKOS itself: https://github.com/alexeyban/EKOS, built with the Oracle connector (needs Oracle Instant Client on
`LD_LIBRARY_PATH` at run time):

```bash
cd EKOS/ekos && cargo build --release -p ekos --features oracle
```

Then create the project from [`project/ekos.toml`](../../project/ekos.toml) (paths are placeholders).
