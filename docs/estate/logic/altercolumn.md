---
title: "altercolumn()"
order: 14
ekos_generated: true
ekos_estate_version: 1
---

# altercolumn()

- defined in: `migration-historic/i1.0a-i1.0b/postgresql/201302081954_IDEMPIERE-621_altercolumn.sql`
- language: plpgsql · fidelity: statements · statements recovered: 50 · unrecovered: 0
- arguments: `tablename name, columnname name, datatype name, nullclause varchar, defaultclause varchar`
- returns: `void`
- also defined in `migration-historic/i1.0a-i1.0b/postgresql/201303150600_IDEMPIERE-708.sql` (plpgsql)
- also defined in `migration/iD10/postgresql/202402041000_IDEMPIERE-5943.sql` (plpgsql)
- also defined in `db/postgresql/functions/altercolumn.sql` (plpgsql)
- also defined in `migration-historic/316-320/postgresql/012_alter_column.sql` (plpgsql)

**Reads:** `PG_ATTRIBUTE`, `PG_CLASS`, `PG_DEPEND`, `PG_REWRITE`, `PG_TYPE`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 15 | `if` | `datatype is not null` |  |  |
| 16 | · `sql` |  | pg_attribute, pg_class, pg_type |  |
| 24 | · `assign` |  |  |  |
| 25 | · `if` | `typename = 'numeric' / strpos(sqltype,'character varying') = 1 / sqltype = 'timestamp without time zone'` |  |  |
| 26 | · · `assign` |  |  |  |
| 28 | · · `assign` |  |  |  |
| 30 | · · `assign` |  |  |  |
| 32 | · `if` | `lower(datatype) <> sqltype and lower(datatype) <> sqltype_short` |  |  |
| 33 | · · `assign` |  |  |  |
| 34 | · · `loop` |  | pg_attribute, pg_class, pg_depend, pg_rewrite |  |
| 60 | · · · `assign` |  |  |  |
| 61 | · · · `assign` |  |  |  |
| 62 | · · · `assign` |  |  |  |
| 64 | · · `if` | `i > 0` |  |  |
| 65 | · · · `block` |  |  |  |
| 66 | · · · · `loop` |  |  |  |
| 67 | · · · · · `assign` |  |  |  |
| 68 | · · · · · `raise` |  |  |  |
| 69 | · · · · · `dynamic_execute` |  |  |  |
| 70 | · · · · · `assign` |  |  |  |
| 74 | · · · · `assign` |  |  |  |
| 75 | · · · · `if` | `i > 0` |  |  |
| 76 | · · · · · `loop` |  |  |  |
| 77 | · · · · · · `assign` |  |  |  |
| 78 | · · · · · · `raise` |  |  |  |
| 79 | · · · · · · `dynamic_execute` |  |  |  |
| 82 | · · · · `raise` |  |  |  |
| 85 | · · `assign` |  |  |  |
| 86 | · · `raise` |  |  |  |
| 87 | · · `dynamic_execute` |  |  |  |
| 88 | · · `assign` |  |  |  |
| 89 | · · `if` | `i > 0` |  |  |
| 90 | · · · `loop` |  |  |  |
| 91 | · · · · `assign` |  |  |  |
| 92 | · · · · `raise` |  |  |  |
| 93 | · · · · `dynamic_execute` |  |  |  |
| 99 | `if` | `defaultclause is not null` |  |  |
| 100 | · `if` | `lower(defaultclause) = 'null'` |  |  |
| 101 | · · `assign` |  |  |  |
| 103 | · · `assign` |  |  |  |
| 105 | · `raise` |  |  |  |
| 106 | · `dynamic_execute` |  |  |  |
| 109 | `if` | `nullclause is not null` |  |  |
| 110 | · `if` | `lower(nullclause) = 'not null' / lower(nullclause) = 'null'` |  |  |
| 111 | · · `assign` |  |  |  |
| 112 | · · `raise` |  |  |  |
| 113 | · · `dynamic_execute` |  |  |  |
| 115 | · · `assign` |  |  |  |
| 116 | · · `raise` |  |  |  |
| 117 | · · `dynamic_execute` |  |  |  |

