---
title: "IsMemberOfAcctSchema()"
order: 66
ekos_generated: true
ekos_estate_version: 1
---

# IsMemberOfAcctSchema()

- defined in: `oracle://idempiere-db/ADEMPIERE/function/ISMEMBEROFACCTSCHEMA`
- language: plsql · fidelity: statements · statements recovered: 6 · unrecovered: 0
- arguments: `p_AD_Client_ID NUMBER, p_AD_Org_ID NUMBER, p_C_AcctSchema_ID NUMBER`
- returns: `boolean`
- also defined in `db/oracle/functions/IsMemberOfAcctSchema.sql` (plsql)
- also defined in `db/postgresql/functions/IsMemberOfAcctSchema.sql` (plpgsql)
- also defined in `migration-historic/i3.1/postgresql/201603031539_IDEMPIERE-3046.sql` (plpgsql)
- also defined in `migration-historic/i3.1/oracle/201603031539_IDEMPIERE-3046.sql` (plsql)

**Reads:** [AD_ORG](../data-model/ad/ad_org.md), [AD_TREE](../data-model/ad/ad_tree.md), [AD_TREENODE](../data-model/ad/ad_treenode.md), [C_ACCTSCHEMA](../data-model/c/c_acctschema.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 6 | `assign` |  |  |  |
| 7 | `assign` |  |  |  |
| 8 | `sql` |  | c_acctschema |  |
| 13 | `if` | `(v_count = 0 )` |  |  |
| 14 | · `sql` |  | ad_org, ad_tree, ad_treenode, c_acctschema |  |
| 31 | `return` |  |  |  |

