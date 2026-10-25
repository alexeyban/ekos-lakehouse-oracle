---
title: "role_access_update()"
order: 86
ekos_generated: true
ekos_estate_version: 1
---

# role_access_update()

- defined in: `migration/processes_post_migration/postgresql/04_role_access_update.sql`
- language: plpgsql · fidelity: statements · statements recovered: 28 · unrecovered: 0
- returns: `void`

**Reads:** [AD_ROLE](../data-model/ad/ad_role.md)

**Writes:** [AD_DOCUMENT_ACTION_ACCESS](../data-model/ad/ad_document_action_access.md), [AD_FORM_ACCESS](../data-model/ad/ad_form_access.md), [AD_INFOWINDOW_ACCESS](../data-model/ad/ad_infowindow_access.md), [AD_PROCESS_ACCESS](../data-model/ad/ad_process_access.md), [AD_WINDOW_ACCESS](../data-model/ad/ad_window_access.md), [AD_WORKFLOW_ACCESS](../data-model/ad/ad_workflow_access.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 8 | `loop` |  | ad_role |  |
| 13 | · `if` | `r.userlevel = 'S  ' / r.userlevel = ' C ' / r.userlevel = ' CO'` |  |  |
| 15 | · · `assign` |  |  |  |
| 16 | · · `assign` |  |  |  |
| 19 | · · `assign` |  |  |  |
| 20 | · · `assign` |  |  |  |
| 23 | · · `assign` |  |  |  |
| 24 | · · `assign` |  |  |  |
| 26 | · · `assign` |  |  |  |
| 27 | · · `assign` |  |  |  |
| 31 | · `assign` |  |  |  |
| 39 | · `dynamic_execute` |  |  |  |
| 41 | · `assign` |  |  |  |
| 49 | · `dynamic_execute` |  |  |  |
| 51 | · `assign` |  |  |  |
| 59 | · `dynamic_execute` |  |  |  |
| 61 | · `assign` |  |  |  |
| 69 | · `dynamic_execute` |  |  |  |
| 71 | · `assign` |  |  |  |
| 81 | · `dynamic_execute` |  |  |  |
| 83 | · `assign` |  |  |  |
| 92 | · `dynamic_execute` |  |  |  |
| 94 | · `sql` |  |  | ad_window_access |
| 95 | · `sql` |  |  | ad_process_access |
| 96 | · `sql` |  |  | ad_form_access |
| 97 | · `sql` |  |  | ad_workflow_access |
| 98 | · `sql` |  |  | ad_document_action_access |
| 99 | · `sql` |  |  | ad_infowindow_access |

