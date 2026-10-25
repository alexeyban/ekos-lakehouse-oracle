---
title: "AD_Synchronize()"
order: 13
ekos_generated: true
ekos_estate_version: 1
---

# AD_Synchronize()

- defined in: `db/oracle/procedures/AD_Syncronize.sql`
- language: plsql · fidelity: statements · statements recovered: 149 · unrecovered: 0
- arguments: `p_PInstance_ID IN NUMBER`

**Reads:** [AD_CLIENT](../data-model/ad/ad_client.md), [AD_COLUMN](../data-model/ad/ad_column.md), [AD_ELEMENT](../data-model/ad/ad_element.md), [AD_ELEMENT_TRL](../data-model/ad/ad_element_trl.md), [AD_FIELD](../data-model/ad/ad_field.md), [AD_FORM](../data-model/ad/ad_form.md), [AD_FORM_TRL](../data-model/ad/ad_form_trl.md), [AD_LANGUAGE](../data-model/ad/ad_language.md), [AD_MENU](../data-model/ad/ad_menu.md), [AD_PRINTFORMAT](../data-model/ad/ad_printformat.md), [AD_PRINTFORMATITEM](../data-model/ad/ad_printformatitem.md), [AD_PROCESS](../data-model/ad/ad_process.md), [AD_PROCESS_PARA](../data-model/ad/ad_process_para.md), [AD_PROCESS_TRL](../data-model/ad/ad_process_trl.md), [AD_TAB](../data-model/ad/ad_tab.md), [AD_TABLE](../data-model/ad/ad_table.md), [AD_TASK](../data-model/ad/ad_task.md), [AD_TASK_TRL](../data-model/ad/ad_task_trl.md), [AD_WF_NODE](../data-model/ad/ad_wf_node.md), [AD_WINDOW](../data-model/ad/ad_window.md), [AD_WINDOW_TRL](../data-model/ad/ad_window_trl.md), [AD_WORKFLOW](../data-model/ad/ad_workflow.md), [AD_WORKFLOW_TRL](../data-model/ad/ad_workflow_trl.md)

**Writes:** [AD_COLUMN](../data-model/ad/ad_column.md), [AD_COLUMN_TRL](../data-model/ad/ad_column_trl.md), [AD_ELEMENT](../data-model/ad/ad_element.md), [AD_ELEMENT_TRL](../data-model/ad/ad_element_trl.md), [AD_FIELD](../data-model/ad/ad_field.md), [AD_FIELD_TRL](../data-model/ad/ad_field_trl.md), [AD_MENU](../data-model/ad/ad_menu.md), [AD_MENU_TRL](../data-model/ad/ad_menu_trl.md), [AD_PINSTANCE](../data-model/ad/ad_pinstance.md), [AD_PRINTFORMATITEM](../data-model/ad/ad_printformatitem.md), [AD_PRINTFORMATITEM_TRL](../data-model/ad/ad_printformatitem_trl.md), [AD_PROCESS_PARA](../data-model/ad/ad_process_para.md), [AD_PROCESS_PARA_TRL](../data-model/ad/ad_process_para_trl.md), [AD_TABLE](../data-model/ad/ad_table.md), [AD_TABLE_TRL](../data-model/ad/ad_table_trl.md), [AD_WF_NODE](../data-model/ad/ad_wf_node.md), [AD_WF_NODE_TRL](../data-model/ad/ad_wf_node_trl.md)

## Statements

| line | statement | condition | reads | writes |
|---|---|---|---|---|
| 39 | `block` |  |  |  |
| 40 | · `if` | `(p_PInstance_ID IS NOT NULL)` |  |  |
| 42 | · · `perform` |  |  |  |
| 43 | · · `assign` |  |  |  |
| 44 | · · `sql` |  |  | ad_pinstance |
| 48 | · · `sql` |  |  |  |
| 51 | · · `assign` |  |  |  |
| 52 | · · `loop` |  |  |  |
| 53 | · · · `assign` |  |  |  |
| 54 | · · · `assign` |  |  |  |
| 56 | · · `perform` |  |  |  |
| 61 | · `perform` |  |  |  |
| 62 | · `block` |  |  |  |
| 78 | · · `perform` |  |  |  |
| 79 | · · `loop` |  |  |  |
| 80 | · · · `perform` |  |  |  |
| 81 | · · · `sql` |  |  | ad_element |
| 89 | · · · `perform` |  |  |  |
| 90 | · · · `sql` |  |  |  |
| 92 | · · `perform` |  |  |  |
| 93 | · · `loop` |  |  |  |
| 94 | · · · `perform` |  |  |  |
| 95 | · · · `sql` |  |  | ad_element |
| 103 | · · · `perform` |  |  |  |
| 104 | · · · `sql` |  |  |  |
| 109 | · `perform` |  |  |  |
| 110 | · `sql` |  | ad_element, ad_element_trl, ad_language | ad_element_trl |
| 120 | · `perform` |  |  |  |
| 123 | · `perform` |  |  |  |
| 124 | · `sql` |  | ad_element | ad_column |
| 129 | · `perform` |  |  |  |
| 130 | · `sql` |  |  |  |
| 133 | · `perform` |  |  |  |
| 134 | · `sql` |  |  |  |
| 142 | · `sql` |  |  |  |
| 147 | · `perform` |  |  |  |
| 152 | · `perform` |  |  |  |
| 164 | · `sql` |  | ad_element | ad_column |
| 173 | · `perform` |  |  |  |
| 176 | · `perform` |  |  |  |
| 177 | · `sql` |  | ad_column, ad_element | ad_field |
| 188 | · `perform` |  |  |  |
| 191 | · `perform` |  |  |  |
| 192 | · `sql` |  | ad_column, ad_element_trl, ad_field | ad_field_trl |
| 213 | · `perform` |  |  |  |
| 216 | · `perform` |  |  |  |
| 217 | · `sql` |  | ad_column, ad_element, ad_tab, ad_window | ad_field |
| 235 | · `perform` |  |  |  |
| 238 | · `perform` |  |  |  |
| 239 | · `sql` |  | ad_column, ad_element_trl, ad_field, ad_tab, ad_window | ad_field_trl |
| 266 | · `perform` |  |  |  |
| 270 | · `perform` |  |  |  |
| 271 | · `sql` |  | ad_column, ad_process | ad_field |
| 283 | · `perform` |  |  |  |
| 286 | · `perform` |  |  |  |
| 287 | · `sql` |  | ad_column, ad_field, ad_process_trl | ad_field_trl |
| 306 | · `perform` |  |  |  |
| 309 | · `sql` |  | ad_element | ad_process_para |
| 319 | · `sql` |  | ad_element | ad_process_para |
| 325 | · `perform` |  |  |  |
| 326 | · `sql` |  | ad_element | ad_process_para |
| 338 | · `perform` |  |  |  |
| 341 | · `perform` |  |  |  |
| 342 | · `sql` |  | ad_element, ad_element_trl, ad_process_para | ad_process_para_trl |
| 361 | · `perform` |  |  |  |
| 365 | · `perform` |  |  |  |
| 366 | · `sql` |  | ad_window | ad_wf_node |
| 377 | · `perform` |  |  |  |
| 380 | · `perform` |  |  |  |
| 381 | · `sql` |  | ad_wf_node, ad_window_trl | ad_wf_node_trl |
| 395 | · `perform` |  |  |  |
| 398 | · `perform` |  |  |  |
| 399 | · `sql` |  | ad_form | ad_wf_node |
| 407 | · `perform` |  |  |  |
| 410 | · `perform` |  |  |  |
| 411 | · `sql` |  | ad_form_trl, ad_wf_node | ad_wf_node_trl |
| 420 | · `perform` |  |  |  |
| 423 | · `perform` |  |  |  |
| 424 | · `sql` |  | ad_process | ad_wf_node |
| 432 | · `perform` |  |  |  |
| 435 | · `perform` |  |  |  |
| 436 | · `sql` |  | ad_process_trl, ad_wf_node | ad_wf_node_trl |
| 445 | · `perform` |  |  |  |
| 448 | · `perform` |  |  |  |
| 449 | · `sql` |  | ad_client, ad_column, ad_element | ad_printformatitem |
| 462 | · `perform` |  |  |  |
| 464 | · `perform` |  |  |  |
| 465 | · `sql` |  | ad_client, ad_column, ad_element, ad_printformat | ad_printformatitem |
| 481 | · `perform` |  |  |  |
| 483 | · `perform` |  |  |  |
| 484 | · `sql` |  | ad_client, ad_column, ad_element_trl, ad_printformat, ad_printformatitem | ad_printformatitem_trl |
| 504 | · `perform` |  |  |  |
| 506 | · `perform` |  |  |  |
| 507 | · `sql` |  | ad_client, ad_printformat, ad_printformatitem | ad_printformatitem_trl |
| 521 | · `perform` |  |  |  |
| 523 | · `perform` |  |  |  |
| 524 | · `sql` |  | ad_printformatitem | ad_printformatitem_trl |
| 532 | · `perform` |  |  |  |
| 544 | · `perform` |  |  |  |
| 545 | · `sql` |  | ad_window | ad_menu |
| 550 | · `perform` |  |  |  |
| 552 | · `sql` |  | ad_menu, ad_window_trl | ad_menu_trl |
| 567 | · `perform` |  |  |  |
| 570 | · `perform` |  |  |  |
| 571 | · `sql` |  | ad_process | ad_menu |
| 576 | · `perform` |  |  |  |
| 578 | · `sql` |  | ad_menu, ad_process_trl | ad_menu_trl |
| 593 | · `perform` |  |  |  |
| 596 | · `perform` |  |  |  |
| 597 | · `sql` |  | ad_form | ad_menu |
| 602 | · `perform` |  |  |  |
| 604 | · `sql` |  | ad_form_trl, ad_menu | ad_menu_trl |
| 619 | · `perform` |  |  |  |
| 622 | · `perform` |  |  |  |
| 623 | · `sql` |  | ad_workflow | ad_menu |
| 628 | · `perform` |  |  |  |
| 630 | · `sql` |  | ad_menu, ad_workflow_trl | ad_menu_trl |
| 645 | · `perform` |  |  |  |
| 648 | · `perform` |  |  |  |
| 649 | · `sql` |  | ad_task | ad_menu |
| 654 | · `perform` |  |  |  |
| 656 | · `sql` |  | ad_menu, ad_task_trl | ad_menu_trl |
| 671 | · `perform` |  |  |  |
| 674 | · `perform` |  |  |  |
| 675 | · `sql` |  | ad_element | ad_column |
| 683 | · `perform` |  |  |  |
| 684 | · `sql` |  | ad_column, ad_element_trl | ad_column_trl |
| 692 | · `perform` |  |  |  |
| 696 | · `perform` |  |  |  |
| 697 | · `sql` |  | ad_element | ad_table |
| 703 | · `perform` |  |  |  |
| 704 | · `sql` |  | ad_element, ad_element_trl, ad_table | ad_table_trl |
| 714 | · `perform` |  |  |  |
| 717 | · `sql` |  | ad_element | ad_table |
| 725 | · `perform` |  |  |  |
| 726 | · `sql` |  | ad_element, ad_element_trl, ad_table | ad_table_trl |
| 737 | · `perform` |  |  |  |
| 745 | · `if` | `(p_PInstance_ID IS NOT NULL)` |  |  |
| 747 | · · `perform` |  |  |  |
| 748 | · · `sql` |  |  | ad_pinstance |
| 755 | · `sql` |  |  |  |
| 756 | · `return` |  |  |  |
| 760 | · `assign` |  |  |  |
| 761 | · `perform` |  |  |  |
| 762 | · `sql` |  |  |  |
| 763 | · `if` | `(p_PInstance_ID IS NOT NULL)` |  |  |
| 764 | · · `sql` |  |  | ad_pinstance |
| 770 | · · `sql` |  |  |  |
| 772 | · `return` |  |  |  |

