---
title: "adempiere.altercolumn()"
order: 6
ekos_generated: true
ekos_estate_version: 1
---

# adempiere.altercolumn()

- defined in: `migration/i8.1z/postgresql/201807250000_IDEMPIERE-4579.sql`
- language: plpgsql · fidelity: statements · statements recovered: 58 · unrecovered: 0
- arguments: `tablename name, columnname name, datatype name, nullclause character varying, defaultclause character varying, namespace name`
- returns: `void`
- also defined in `migration/i5.1/postgresql/201807111333_Ticket_AP2-357.sql` (plpgsql)

**Reads:** `INFORMATION_SCHEMA.ROLE_TABLE_GRANTS`, `PG_ATTRIBUTE`, `PG_CLASS`, `PG_DEPEND`, `PG_NAMESPACE`, `PG_REWRITE`, `PG_TYPE`

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 21 | `if` | `datatype is not null` |  |  |
| 22 | · `sql` |  | pg_attribute, pg_class, pg_namespace, pg_type |  |
| 32 | · `assign` |  |  |  |
| 33 | · `if` | `typename = 'numeric' / strpos(sqltype,'character varying') = 1 / sqltype = 'timestamp without time zone'` |  |  |
| 34 | · · `assign` |  |  |  |
| 36 | · · `assign` |  |  |  |
| 38 | · · `assign` |  |  |  |
| 40 | · `if` | `lower(datatype) <> sqltype and lower(datatype) <> sqltype_short` |  |  |
| 41 | · · `assign` |  |  |  |
| 42 | · · `loop` |  | pg_attribute, pg_class, pg_depend, pg_namespace, pg_rewrite |  |
| 72 | · · · `raise` |  |  |  |
| 73 | · · · `assign` |  |  |  |
| 74 | · · · `assign` |  |  |  |
| 75 | · · · `assign` |  |  |  |
| 77 | · · `if` | `i > 0` |  |  |
| 78 | · · · `block` |  |  |  |
| 79 | · · · · `loop` |  |  |  |
| 80 | · · · · · `sql` |  | information_schema.role_table_grants |  |
| 84 | · · · · · `assign` |  |  |  |
| 85 | · · · · · `assign` |  |  |  |
| 86 | · · · · · `raise` |  |  |  |
| 87 | · · · · · `dynamic_execute` |  |  |  |
| 88 | · · · · · `assign` |  |  |  |
| 92 | · · · · `assign` |  |  |  |
| 93 | · · · · `if` | `i > 0` |  |  |
| 94 | · · · · · `loop` |  |  |  |
| 95 | · · · · · · `assign` |  |  |  |
| 96 | · · · · · · `raise` |  |  |  |
| 97 | · · · · · · `dynamic_execute` |  |  |  |
| 100 | · · · · `raise` |  |  |  |
| 103 | · · `assign` |  |  |  |
| 104 | · · `raise` |  |  |  |
| 105 | · · `dynamic_execute` |  |  |  |
| 106 | · · `assign` |  |  |  |
| 107 | · · `if` | `i > 0` |  |  |
| 108 | · · · `loop` |  |  |  |
| 109 | · · · · `assign` |  |  |  |
| 110 | · · · · `raise` |  |  |  |
| 111 | · · · · `dynamic_execute` |  |  |  |
| 112 | · · · · `assign` |  |  |  |
| 113 | · · · · `raise` |  |  |  |
| 114 | · · · · `dynamic_execute` |  |  |  |
| 120 | `if` | `defaultclause is not null` |  |  |
| 121 | · `if` | `lower(defaultclause) = 'null'` |  |  |
| 122 | · · `assign` |  |  |  |
| 124 | · · `if` | `defaultclause  ~ '.*[(].*[)].*' or lower(defaultclause) = 'current_timestamp'` |  |  |
| 125 | · · · `assign` |  |  |  |
| 127 | · · · `assign` |  |  |  |
| 130 | · `raise` |  |  |  |
| 131 | · `dynamic_execute` |  |  |  |
| 134 | `if` | `nullclause is not null` |  |  |
| 135 | · `if` | `lower(nullclause) = 'not null' / lower(nullclause) = 'null'` |  |  |
| 136 | · · `assign` |  |  |  |
| 137 | · · `raise` |  |  |  |
| 138 | · · `dynamic_execute` |  |  |  |
| 140 | · · `assign` |  |  |  |
| 141 | · · `raise` |  |  |  |
| 142 | · · `dynamic_execute` |  |  |  |

