---
title: "Findings"
order: 7
ekos_generated: true
ekos_estate_version: 1
---

# Findings

## Code ↔ database conflicts

Open conflicts about in-scope tables, by type:

| type | open | explained |
|---|---|---|
| `duplicate_definition` | 1 | 0 |
| `mandatory_but_nullable` | 111 | 0 |
| `model_column_missing` | 160 | 0 |
| `model_table_missing` | 9 | 0 |
| `routine_text_differs` | 1 | 0 |
| `table_without_model` | 147 | 0 |

| table | type | attribute | explanation |
|---|---|---|---|
| [AD_ALERT](../data-model/ad/ad_alert.md) | `mandatory_but_nullable` | `columns.AD_AlertProcessor_ID.nullable` | unexplained |
| [AD_ARCHIVE](../data-model/ad/ad_archive.md) | `mandatory_but_nullable` | `columns.BinaryData.nullable` | unexplained |
| [AD_ATTACHMENTFILE](../data-model/ad/ad_attachmentfile.md) | `model_table_missing` | `database_table` | unexplained |
| [AD_BROADCASTMESSAGE](../data-model/ad/ad_broadcastmessage.md) | `mandatory_but_nullable` | `columns.BroadcastMessage.nullable` | unexplained |
| [AD_BROADCASTMESSAGE_TRL](../data-model/ad/ad_broadcastmessage_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_CHARTDATASOURCE_TRL](../data-model/ad/ad_chartdatasource_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_CHART_TRL](../data-model/ad/ad_chart_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_COLOR_TRL](../data-model/ad/ad_color_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_COLUMN](../data-model/ad/ad_column.md) | `mandatory_but_nullable` | `columns.AD_Element_ID.nullable` | unexplained |
| [AD_COLUMN](../data-model/ad/ad_column.md) | `mandatory_but_nullable` | `columns.IsToolbarButton.nullable` | unexplained |
| [AD_COLUMN_TRL](../data-model/ad/ad_column_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_CTXHELPMSG_TRL](../data-model/ad/ad_ctxhelpmsg_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_DESKTOPWORKBENCH](../data-model/ad/ad_desktopworkbench.md) | `table_without_model` | `model_class` | unexplained |
| [AD_DESKTOP](../data-model/ad/ad_desktop.md) | `table_without_model` | `model_class` | unexplained |
| [AD_DESKTOP_TRL](../data-model/ad/ad_desktop_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_ELEMENT_TRL](../data-model/ad/ad_element_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_FIELDGROUP_TRL](../data-model/ad/ad_fieldgroup_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_FIELD](../data-model/ad/ad_field.md) | `mandatory_but_nullable` | `columns.AD_Column_ID.nullable` | unexplained |
| [AD_FIELD_TRL](../data-model/ad/ad_field_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_FORM_TRL](../data-model/ad/ad_form_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_INFOCOLUMN_TRL](../data-model/ad/ad_infocolumn_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_INFOWINDOW_TRL](../data-model/ad/ad_infowindow_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_LABELCATEGORY_TRL](../data-model/ad/ad_labelcategory_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_LABEL_TRL](../data-model/ad/ad_label_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_MENU_TRL](../data-model/ad/ad_menu_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_MESSAGE_TRL](../data-model/ad/ad_message_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_ORGINFO](../data-model/ad/ad_orginfo.md) | `mandatory_but_nullable` | `columns.ReceiptFooterMsg.nullable` | unexplained |
| [AD_PACKAGE_EXP](../data-model/ad/ad_package_exp.md) | `model_column_missing` | `columns.IsIncludeOrganizationId` | unexplained |
| [AD_PACKAGE_EXP_COMMON](../data-model/ad/ad_package_exp_common.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PASSWORDRESETTOKEN](../data-model/ad/ad_passwordresettoken.md) | `model_table_missing` | `database_table` | unexplained |
| [AD_PASSWORDRULE](../data-model/ad/ad_passwordrule.md) | `mandatory_but_nullable` | `columns.IsDictMatchBackwards.nullable` | unexplained |
| [AD_PASSWORDRULE](../data-model/ad/ad_passwordrule.md) | `mandatory_but_nullable` | `columns.IsUserNameRule.nullable` | unexplained |
| [AD_PASSWORDRULE](../data-model/ad/ad_passwordrule.md) | `mandatory_but_nullable` | `columns.IsUsingDictionary.nullable` | unexplained |
| [AD_PASSWORDRULE](../data-model/ad/ad_passwordrule.md) | `mandatory_but_nullable` | `columns.IsWhitespace.nullable` | unexplained |
| [AD_PINSTANCE](../data-model/ad/ad_pinstance.md) | `mandatory_but_nullable` | `columns.IsRunAsJob.nullable` | unexplained |
| [AD_PINSTANCE](../data-model/ad/ad_pinstance.md) | `model_column_missing` | `columns.ExternalTraceId` | unexplained |
| [AD_PRINTCOLOR_TRL](../data-model/ad/ad_printcolor_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PRINTFORMATITEM](../data-model/ad/ad_printformatitem.md) | `mandatory_but_nullable` | `columns.AD_PrintFormatChild_ID.nullable` | unexplained |
| [AD_PRINTFORMATITEM](../data-model/ad/ad_printformatitem.md) | `model_column_missing` | `columns.ScaleFactor` | unexplained |
| [AD_PRINTFORMATITEM_TRL](../data-model/ad/ad_printformatitem_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PRINTFORMAT_TRL](../data-model/ad/ad_printformat_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PRINTLABELLINE_TRL](../data-model/ad/ad_printlabelline_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PROCESS_DRILLRULE_TRL](../data-model/ad/ad_process_drillrule_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PROCESS_PARA_TRL](../data-model/ad/ad_process_para_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_PROCESS_TRL](../data-model/ad/ad_process_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_REFERENCE_TRL](../data-model/ad/ad_reference_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_REF_LIST_TRL](../data-model/ad/ad_ref_list_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_REF_TABLE](../data-model/ad/ad_ref_table.md) | `model_column_missing` | `columns.DisplaySQL` | unexplained |
| [AD_REF_TABLE](../data-model/ad/ad_ref_table.md) | `model_column_missing` | `columns.IsDisplayIdentifier` | unexplained |
| [AD_RELATIONTYPE](../data-model/ad/ad_relationtype.md) | `mandatory_but_nullable` | `columns.EntityType.nullable` | unexplained |
| [AD_REPLICATION](../data-model/ad/ad_replication.md) | `mandatory_but_nullable` | `columns.Remote_Client_ID.nullable` | unexplained |
| [AD_REPLICATION](../data-model/ad/ad_replication.md) | `mandatory_but_nullable` | `columns.Remote_Org_ID.nullable` | unexplained |
| [AD_REQUIREDPLUGIN](../data-model/ad/ad_requiredplugin.md) | `model_table_missing` | `database_table` | unexplained |
| [AD_RULE](../data-model/ad/ad_rule.md) | `mandatory_but_nullable` | `columns.EntityType.nullable` | unexplained |
| [AD_RULE](../data-model/ad/ad_rule.md) | `mandatory_but_nullable` | `columns.EventType.nullable` | unexplained |
| [AD_RULE](../data-model/ad/ad_rule.md) | `mandatory_but_nullable` | `columns.RuleType.nullable` | unexplained |
| [AD_SEQUENCE_NO](../data-model/ad/ad_sequence_no.md) | `model_column_missing` | `columns.SequenceKey` | unexplained |
| [AD_STATUSLINEUSEDIN](../data-model/ad/ad_statuslineusedin.md) | `mandatory_but_nullable` | `columns.EntityType.nullable` | unexplained |
| [AD_SYSTEM](../data-model/ad/ad_system.md) | `mandatory_but_nullable` | `columns.Info.nullable` | unexplained |
| [AD_SYSTEM](../data-model/ad/ad_system.md) | `mandatory_but_nullable` | `columns.Version.nullable` | unexplained |
| [AD_TABLEATTRIBUTESET](../data-model/ad/ad_tableattributeset.md) | `model_table_missing` | `database_table` | unexplained |
| [AD_TABLEATTRIBUTE](../data-model/ad/ad_tableattribute.md) | `model_table_missing` | `database_table` | unexplained |
| [AD_TABLE_TRL](../data-model/ad/ad_table_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_TAB_TRL](../data-model/ad/ad_tab_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_TASK_TRL](../data-model/ad/ad_task_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_TREEBAR](../data-model/ad/ad_treebar.md) | `model_column_missing` | `columns.AD_Menu_ID` | unexplained |
| [AD_TREENODE](../data-model/ad/ad_treenode.md) | `mandatory_but_nullable` | `columns.SeqNo.nullable` | unexplained |
| [AD_USERDEF_FORM](../data-model/ad/ad_userdef_form.md) | `model_table_missing` | `database_table` | unexplained |
| [AD_USERQUERY](../data-model/ad/ad_userquery.md) | `mandatory_but_nullable` | `columns.AD_Tab_ID.nullable` | unexplained |
| [AD_USERQUERY](../data-model/ad/ad_userquery.md) | `mandatory_but_nullable` | `columns.AD_Window_ID.nullable` | unexplained |
| [AD_USER](../data-model/ad/ad_user.md) | `model_column_missing` | `columns.PasswordHashAlgorithm` | unexplained |
| [AD_USER](../data-model/ad/ad_user.md) | `model_column_missing` | `columns.SaltAlgorithm` | unexplained |
| [AD_VAL_RULE](../data-model/ad/ad_val_rule.md) | `mandatory_but_nullable` | `columns.Type.nullable` | unexplained |
| [AD_WF_NODE_TRL](../data-model/ad/ad_wf_node_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_WF_RESPONSIBLE](../data-model/ad/ad_wf_responsible.md) | `mandatory_but_nullable` | `columns.AD_Role_ID.nullable` | unexplained |
| [AD_WF_RESPONSIBLE](../data-model/ad/ad_wf_responsible.md) | `model_column_missing` | `columns.Override_ID` | unexplained |
| [AD_WINDOW](../data-model/ad/ad_window.md) | `mandatory_but_nullable` | `columns.WindowType.nullable` | unexplained |
| [AD_WINDOW_TRL](../data-model/ad/ad_window_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_WORKBENCHWINDOW](../data-model/ad/ad_workbenchwindow.md) | `table_without_model` | `model_class` | unexplained |
| [AD_WORKBENCH](../data-model/ad/ad_workbench.md) | `table_without_model` | `model_class` | unexplained |
| [AD_WORKBENCH_TRL](../data-model/ad/ad_workbench_trl.md) | `table_without_model` | `model_class` | unexplained |
| [AD_WORKFLOW_TRL](../data-model/ad/ad_workflow_trl.md) | `table_without_model` | `model_class` | unexplained |
| [A_ASSET](../data-model/a/a_asset.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [A_ASSET_ADDITION](../data-model/a/a_asset_addition.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [A_ASSET_ADDITION](../data-model/a/a_asset_addition.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [A_ASSET_CHANGE_AMT](../data-model/a/a_asset_change_amt.md) | `table_without_model` | `model_class` | unexplained |
| [A_ASSET_DISPOSED](../data-model/a/a_asset_disposed.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [A_ASSET_DISPOSED](../data-model/a/a_asset_disposed.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [A_ASSET_GROUP_ACCT](../data-model/a/a_asset_group_acct.md) | `mandatory_but_nullable` | `columns.A_Disposal_Loss_Acct.nullable` | unexplained |
| [A_ASSET_GROUP_ACCT](../data-model/a/a_asset_group_acct.md) | `mandatory_but_nullable` | `columns.A_Disposal_Revenue_Acct.nullable` | unexplained |
| [A_ASSET_GROUP_TRL](../data-model/a/a_asset_group_trl.md) | `table_without_model` | `model_class` | unexplained |
| [A_ASSET_REVAL](../data-model/a/a_asset_reval.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [A_ASSET_REVAL](../data-model/a/a_asset_reval.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [A_ASSET_SPREAD](../data-model/a/a_asset_spread.md) | `table_without_model` | `model_class` | unexplained |
| [A_ASSET_TRANSFER](../data-model/a/a_asset_transfer.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [A_ASSET_TRANSFER](../data-model/a/a_asset_transfer.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [A_DEPRECIATION_ENTRY](../data-model/a/a_depreciation_entry.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [A_DEPRECIATION_ENTRY](../data-model/a/a_depreciation_entry.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [A_REGISTRATION](../data-model/a/a_registration.md) | `mandatory_but_nullable` | `columns.AssetServiceDate.nullable` | unexplained |
| [CM_ACCESSCONTAINER](../data-model/cm/cm_accesscontainer.md) | `table_without_model` | `model_class` | unexplained |
| [CM_ACCESSLISTBPGROUP](../data-model/cm/cm_accesslistbpgroup.md) | `table_without_model` | `model_class` | unexplained |
| [CM_ACCESSLISTROLE](../data-model/cm/cm_accesslistrole.md) | `table_without_model` | `model_class` | unexplained |
| [CM_ACCESSMEDIA](../data-model/cm/cm_accessmedia.md) | `table_without_model` | `model_class` | unexplained |
| [CM_ACCESSNEWSCHANNEL](../data-model/cm/cm_accessnewschannel.md) | `table_without_model` | `model_class` | unexplained |
| [CM_ACCESSPROFILE](../data-model/cm/cm_accessprofile.md) | `table_without_model` | `model_class` | unexplained |
| [CM_ACCESSSTAGE](../data-model/cm/cm_accessstage.md) | `table_without_model` | `model_class` | unexplained |
| [CM_AD](../data-model/cm/cm_ad.md) | `table_without_model` | `model_class` | unexplained |
| [CM_AD_CAT](../data-model/cm/cm_ad_cat.md) | `table_without_model` | `model_class` | unexplained |
| [CM_BROADCASTSERVER](../data-model/cm/cm_broadcastserver.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CHATENTRY](../data-model/cm/cm_chatentry.md) | `mandatory_but_nullable` | `columns.CharacterData.nullable` | unexplained |
| [CM_CONTAINERTTABLE](../data-model/cm/cm_containerttable.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CONTAINER](../data-model/cm/cm_container.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CONTAINER_ELEMENT](../data-model/cm/cm_container_element.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CONTAINER_ELEMENT_TRL](../data-model/cm/cm_container_element_trl.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CONTAINER_TRL](../data-model/cm/cm_container_trl.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CONTAINER_URL](../data-model/cm/cm_container_url.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CSTAGETTABLE](../data-model/cm/cm_cstagettable.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CSTAGE](../data-model/cm/cm_cstage.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CSTAGE_ELEMENT](../data-model/cm/cm_cstage_element.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CSTAGE_ELEMENT_TRL](../data-model/cm/cm_cstage_element_trl.md) | `table_without_model` | `model_class` | unexplained |
| [CM_CSTAGE_TRL](../data-model/cm/cm_cstage_trl.md) | `table_without_model` | `model_class` | unexplained |
| [CM_MEDIADEPLOY](../data-model/cm/cm_mediadeploy.md) | `table_without_model` | `model_class` | unexplained |
| [CM_MEDIA](../data-model/cm/cm_media.md) | `table_without_model` | `model_class` | unexplained |
| [CM_MEDIA_SERVER](../data-model/cm/cm_media_server.md) | `table_without_model` | `model_class` | unexplained |
| [CM_NEWSCHANNEL](../data-model/cm/cm_newschannel.md) | `table_without_model` | `model_class` | unexplained |
| [CM_NEWSITEM](../data-model/cm/cm_newsitem.md) | `table_without_model` | `model_class` | unexplained |
| [CM_TEMPLATETABLE](../data-model/cm/cm_templatetable.md) | `table_without_model` | `model_class` | unexplained |
| [CM_TEMPLATE](../data-model/cm/cm_template.md) | `table_without_model` | `model_class` | unexplained |
| [CM_TEMPLATE_AD_CAT](../data-model/cm/cm_template_ad_cat.md) | `table_without_model` | `model_class` | unexplained |
| [CM_WEBPROJECT](../data-model/cm/cm_webproject.md) | `table_without_model` | `model_class` | unexplained |
| [CM_WEBPROJECT_DOMAIN](../data-model/cm/cm_webproject_domain.md) | `table_without_model` | `model_class` | unexplained |
| [CM_WIKITOKEN](../data-model/cm/cm_wikitoken.md) | `table_without_model` | `model_class` | unexplained |
| [CREATE$JAVA$LOB$TABLE](../data-model/other/create-java-lob-table.md) | `table_without_model` | `model_class` | unexplained |
| [C_ACCTSCHEMA](../data-model/c/c_acctschema.md) | `mandatory_but_nullable` | `columns.M_CostType_ID.nullable` | unexplained |
| [C_ACCTSCHEMA](../data-model/c/c_acctschema.md) | `mandatory_but_nullable` | `columns.TaxCorrectionType.nullable` | unexplained |
| [C_ACCTSCHEMA](../data-model/c/c_acctschema.md) | `model_column_missing` | `columns.BackDateDay` | unexplained |
| [C_ACCTSCHEMA](../data-model/c/c_acctschema.md) | `model_column_missing` | `columns.EndDate` | unexplained |
| [C_ACCTSCHEMA](../data-model/c/c_acctschema.md) | `model_column_missing` | `columns.StartDate` | unexplained |
| [C_ACCTSCHEMA_DEFAULT](../data-model/c/c_acctschema_default.md) | `mandatory_but_nullable` | `columns.P_RateVariance_Acct.nullable` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `mandatory_but_nullable` | `columns.C_Element_ID.nullable` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `mandatory_but_nullable` | `columns.Org_ID.nullable` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.AD_Column2_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.A_Asset_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| [C_ACCTSCHEMA_ELEMENT](../data-model/c/c_acctschema_element.md) | `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |
| [C_ACTIVITY_TRL](../data-model/c/c_activity_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_BANKTRANSFER](../data-model/c/c_banktransfer.md) | `model_column_missing` | `columns.From_DocType_ID` | unexplained |
| [C_BANKTRANSFER](../data-model/c/c_banktransfer.md) | `model_column_missing` | `columns.To_DocType_ID` | unexplained |
| [C_BPARTNER](../data-model/c/c_bpartner.md) | `mandatory_but_nullable` | `columns.SO_CreditLimit.nullable` | unexplained |
| [C_BPARTNER](../data-model/c/c_bpartner.md) | `mandatory_but_nullable` | `columns.SO_CreditUsed.nullable` | unexplained |
| [C_BPARTNER_LOCATION](../data-model/c/c_bpartner_location.md) | `mandatory_but_nullable` | `columns.C_Location_ID.nullable` | unexplained |
| [C_BP_BANKACCOUNT](../data-model/c/c_bp_bankaccount.md) | `mandatory_but_nullable` | `columns.A_Name.nullable` | unexplained |
| [C_BP_CUSTOMER_ACCT](../data-model/c/c_bp_customer_acct.md) | `mandatory_but_nullable` | `columns.C_Prepayment_Acct.nullable` | unexplained |
| [C_BP_CUSTOMER_ACCT](../data-model/c/c_bp_customer_acct.md) | `mandatory_but_nullable` | `columns.C_Receivable_Acct.nullable` | unexplained |
| [C_BP_CUSTOMER_ACCT](../data-model/c/c_bp_customer_acct.md) | `mandatory_but_nullable` | `columns.C_Receivable_Services_Acct.nullable` | unexplained |
| [C_BP_GROUP_ACCT](../data-model/c/c_bp_group_acct.md) | `mandatory_but_nullable` | `columns.C_Receivable_Services_Acct.nullable` | unexplained |
| [C_BP_VENDOR_ACCT](../data-model/c/c_bp_vendor_acct.md) | `mandatory_but_nullable` | `columns.V_Liability_Acct.nullable` | unexplained |
| [C_BP_VENDOR_ACCT](../data-model/c/c_bp_vendor_acct.md) | `mandatory_but_nullable` | `columns.V_Prepayment_Acct.nullable` | unexplained |
| [C_CAMPAIGN_TRL](../data-model/c/c_campaign_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_CHARGE](../data-model/c/c_charge.md) | `mandatory_but_nullable` | `columns.C_TaxCategory_ID.nullable` | unexplained |
| [C_CHARGE](../data-model/c/c_charge.md) | `model_column_missing` | `columns.IsExcludedFromDiscount` | unexplained |
| [C_CHARGE_TRL](../data-model/c/c_charge_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_COSTCENTER](../data-model/c/c_costcenter.md) | `model_table_missing` | `database_table` | unexplained |
| [C_COUNTRYGROUP_TRL](../data-model/c/c_countrygroup_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_COUNTRY](../data-model/c/c_country.md) | `model_column_missing` | `columns.ISOCountryCodeAlpha3` | unexplained |
| [C_COUNTRY](../data-model/c/c_country.md) | `model_column_missing` | `columns.M49Code` | unexplained |
| [C_COUNTRY_TRL](../data-model/c/c_country_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_CURRENCY](../data-model/c/c_currency.md) | `mandatory_but_nullable` | `columns.RoundOffFactor.nullable` | unexplained |
| [C_CURRENCY_TRL](../data-model/c/c_currency_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_DEPARTMENT](../data-model/c/c_department.md) | `model_table_missing` | `database_table` | unexplained |
| [C_DOCTYPECOUNTER](../data-model/c/c_doctypecounter.md) | `mandatory_but_nullable` | `columns.Counter_C_DocType_ID.nullable` | unexplained |
| [C_DOCTYPE](../data-model/c/c_doctype.md) | `model_column_missing` | `columns.IsAlwaysPosted` | unexplained |
| [C_DOCTYPE](../data-model/c/c_doctype.md) | `model_column_missing` | `columns.IsCanBeReactivated` | unexplained |
| [C_DOCTYPE_TRL](../data-model/c/c_doctype_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_DUNNINGLEVEL_TRL](../data-model/c/c_dunninglevel_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_ELEMENTVALUE_TRL](../data-model/c/c_elementvalue_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_ELEMENT](../data-model/c/c_element.md) | `mandatory_but_nullable` | `columns.AD_Tree_ID.nullable` | unexplained |
| [C_GREETING_TRL](../data-model/c/c_greeting_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_INVOICEBATCHLINE](../data-model/c/c_invoicebatchline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_INVOICEBATCHLINE](../data-model/c/c_invoicebatchline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_INVOICELINE](../data-model/c/c_invoiceline.md) | `mandatory_but_nullable` | `columns.C_Tax_ID.nullable` | unexplained |
| [C_INVOICELINE](../data-model/c/c_invoiceline.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [C_INVOICELINE](../data-model/c/c_invoiceline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_INVOICELINE](../data-model/c/c_invoiceline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_INVOICELINE](../data-model/c/c_invoiceline.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [C_INVOICESCHEDULE](../data-model/c/c_invoiceschedule.md) | `mandatory_but_nullable` | `columns.Amt.nullable` | unexplained |
| [C_INVOICESCHEDULE](../data-model/c/c_invoiceschedule.md) | `mandatory_but_nullable` | `columns.InvoiceDay.nullable` | unexplained |
| [C_INVOICESCHEDULE](../data-model/c/c_invoiceschedule.md) | `mandatory_but_nullable` | `columns.InvoiceWeekDay.nullable` | unexplained |
| [C_INVOICE](../data-model/c/c_invoice.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_INVOICE](../data-model/c/c_invoice.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_INVOICE](../data-model/c/c_invoice.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [C_LANDEDCOST](../data-model/c/c_landedcost.md) | `model_column_missing` | `columns.Qty` | unexplained |
| [C_ORDERLINE](../data-model/c/c_orderline.md) | `mandatory_but_nullable` | `columns.C_BPartner_Location_ID.nullable` | unexplained |
| [C_ORDERLINE](../data-model/c/c_orderline.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [C_ORDERLINE](../data-model/c/c_orderline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_ORDERLINE](../data-model/c/c_orderline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_ORDER](../data-model/c/c_order.md) | `mandatory_but_nullable` | `columns.DatePromised.nullable` | unexplained |
| [C_ORDER](../data-model/c/c_order.md) | `mandatory_but_nullable` | `columns.FreightAmt.nullable` | unexplained |
| [C_ORDER](../data-model/c/c_order.md) | `mandatory_but_nullable` | `columns.SalesRep_ID.nullable` | unexplained |
| [C_ORDER](../data-model/c/c_order.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_ORDER](../data-model/c/c_order.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_PAYMENTBATCH](../data-model/c/c_paymentbatch.md) | `mandatory_but_nullable` | `columns.C_PaymentProcessor_ID.nullable` | unexplained |
| [C_PAYMENTPROCESSOR](../data-model/c/c_paymentprocessor.md) | `mandatory_but_nullable` | `columns.HostAddress.nullable` | unexplained |
| [C_PAYMENTPROCESSOR](../data-model/c/c_paymentprocessor.md) | `mandatory_but_nullable` | `columns.HostPort.nullable` | unexplained |
| [C_PAYMENTTERM_TRL](../data-model/c/c_paymentterm_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_PAYMENTTRANSACTION](../data-model/c/c_paymenttransaction.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_PAYMENTTRANSACTION](../data-model/c/c_paymenttransaction.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_PAYMENT](../data-model/c/c_payment.md) | `mandatory_but_nullable` | `columns.C_BPartner_ID.nullable` | unexplained |
| [C_PAYMENT](../data-model/c/c_payment.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [C_PAYMENT](../data-model/c/c_payment.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [C_PAYMENT](../data-model/c/c_payment.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [C_PAYSELECTION](../data-model/c/c_payselection.md) | `mandatory_but_nullable` | `columns.Processing.nullable` | unexplained |
| [C_PROJECTISSUE](../data-model/c/c_projectissue.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [C_PROJECTPHASE](../data-model/c/c_projectphase.md) | `mandatory_but_nullable` | `columns.ProjInvoiceRule.nullable` | unexplained |
| [C_PROJECTTASK](../data-model/c/c_projecttask.md) | `mandatory_but_nullable` | `columns.ProjInvoiceRule.nullable` | unexplained |
| [C_RECURRING](../data-model/c/c_recurring.md) | `mandatory_but_nullable` | `columns.DateNextRun.nullable` | unexplained |
| [C_REGION_TRL](../data-model/c/c_region_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_REVENUERECOGNITION](../data-model/c/c_revenuerecognition.md) | `mandatory_but_nullable` | `columns.RecognitionFrequency.nullable` | unexplained |
| [C_RFQLINE](../data-model/c/c_rfqline.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [C_SALESREGION_TRL](../data-model/c/c_salesregion_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_SALESSTAGE_TRL](../data-model/c/c_salesstage_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_TAXCATEGORY_TRL](../data-model/c/c_taxcategory_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_TAX_TRL](../data-model/c/c_tax_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_UOM_TRL](../data-model/c/c_uom_trl.md) | `table_without_model` | `model_class` | unexplained |
| [C_WITHHOLDING](../data-model/c/c_withholding.md) | `mandatory_but_nullable` | `columns.Beneficiary.nullable` | unexplained |
| [DBREPLICASYNCVERIFIER](../data-model/other/dbreplicasyncverifier.md) | `table_without_model` | `model_class` | unexplained |
| [EXP_FORMATLINE](../data-model/exp/exp_formatline.md) | `mandatory_but_nullable` | `columns.AD_Column_ID.nullable` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `mandatory_but_nullable` | `columns.C_Period_ID.nullable` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `mandatory_but_nullable` | `columns.GL_Category_ID.nullable` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.CustomFieldText1` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.CustomFieldText2` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.CustomFieldText3` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.CustomFieldText4` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| [FACT_ACCT](../data-model/fact/fact_acct.md) | `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.A_Asset_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.CustomFieldText1` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.CustomFieldText2` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.CustomFieldText3` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.CustomFieldText4` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| [FACT_ACCT_SUMMARY](../data-model/fact/fact_acct_summary.md) | `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |
| [GL_CATEGORY_TRL](../data-model/gl/gl_category_trl.md) | `table_without_model` | `model_class` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.A_Asset_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteAsset` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteAttributeSetInstance` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteCharge` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteCostCenter` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteDepartment` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteEmployee` | unexplained |
| [GL_DISTRIBUTIONLINE](../data-model/gl/gl_distributionline.md) | `model_column_missing` | `columns.OverwriteWarehouse` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.A_Asset_ID` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyAsset` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyAttributeSetInstance` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyCharge` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyCostCenter` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyDepartment` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyEmployee` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.AnyWarehouse` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| [GL_DISTRIBUTION](../data-model/gl/gl_distribution.md) | `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.C_Charge_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.C_Employee_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.C_Tax_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.M_AttributeSetInstance_ID` | unexplained |
| [GL_JOURNALLINE](../data-model/gl/gl_journalline.md) | `model_column_missing` | `columns.M_Warehouse_ID` | unexplained |
| [GL_JOURNAL](../data-model/gl/gl_journal.md) | `mandatory_but_nullable` | `columns.C_Currency_ID.nullable` | unexplained |
| [JAVA$CLASS$MD5$TABLE](../data-model/other/java-class-md5-table.md) | `table_without_model` | `model_class` | unexplained |
| [K_CATEGORYVALUE](../data-model/k/k_categoryvalue.md) | `table_without_model` | `model_class` | unexplained |
| [K_CATEGORY](../data-model/k/k_category.md) | `table_without_model` | `model_class` | unexplained |
| [K_COMMENT](../data-model/k/k_comment.md) | `table_without_model` | `model_class` | unexplained |
| [K_ENTRYCATEGORY](../data-model/k/k_entrycategory.md) | `table_without_model` | `model_class` | unexplained |
| [K_ENTRYRELATED](../data-model/k/k_entryrelated.md) | `table_without_model` | `model_class` | unexplained |
| [K_ENTRY](../data-model/k/k_entry.md) | `table_without_model` | `model_class` | unexplained |
| [K_INDEXSTOP](../data-model/k/k_indexstop.md) | `table_without_model` | `model_class` | unexplained |
| [K_INDEX](../data-model/k/k_index.md) | `table_without_model` | `model_class` | unexplained |
| [K_SOURCE](../data-model/k/k_source.md) | `table_without_model` | `model_class` | unexplained |
| [K_SYNONYM](../data-model/k/k_synonym.md) | `table_without_model` | `model_class` | unexplained |
| [K_TOPIC](../data-model/k/k_topic.md) | `table_without_model` | `model_class` | unexplained |
| [K_TYPE](../data-model/k/k_type.md) | `table_without_model` | `model_class` | unexplained |
| [M_ATTRIBUTESETINSTANCE](../data-model/m/m_attributesetinstance.md) | `mandatory_but_nullable` | `columns.M_AttributeSet_ID.nullable` | unexplained |
| [M_ATTRIBUTESET](../data-model/m/m_attributeset.md) | `mandatory_but_nullable` | `columns.M_AttributeSet_Type.nullable` | unexplained |
| [M_ATTRIBUTESET](../data-model/m/m_attributeset.md) | `model_column_missing` | `columns.EntityType` | unexplained |
| [M_ATTRIBUTEUSE](../data-model/m/m_attributeuse.md) | `model_column_missing` | `columns.DefaultValue` | unexplained |
| [M_ATTRIBUTEUSE](../data-model/m/m_attributeuse.md) | `model_column_missing` | `columns.EntityType` | unexplained |
| [M_ATTRIBUTEVALUE](../data-model/m/m_attributevalue.md) | `model_column_missing` | `columns.EntityType` | unexplained |
| [M_ATTRIBUTE](../data-model/m/m_attribute.md) | `model_column_missing` | `columns.DefaultValue` | unexplained |
| [M_ATTRIBUTE](../data-model/m/m_attribute.md) | `model_column_missing` | `columns.EntityType` | unexplained |
| [M_BOMPRODUCT](../data-model/m/m_bomproduct.md) | `table_without_model` | `model_class` | unexplained |
| [M_BOM](../data-model/m/m_bom.md) | `table_without_model` | `model_class` | unexplained |
| [M_COSTDETAIL](../data-model/m/m_costdetail.md) | `model_column_missing` | `columns.BackDateProcessedOn` | unexplained |
| [M_COSTDETAIL](../data-model/m/m_costdetail.md) | `model_column_missing` | `columns.DateAcct` | unexplained |
| [M_COSTDETAIL](../data-model/m/m_costdetail.md) | `model_column_missing` | `columns.IsBackDate` | unexplained |
| [M_COSTDETAIL](../data-model/m/m_costdetail.md) | `model_column_missing` | `columns.Ref_CostDetail_ID` | unexplained |
| [M_COSTHISTORY](../data-model/m/m_costhistory.md) | `model_column_missing` | `columns.BackDateProcessedOn` | unexplained |
| [M_COSTHISTORY](../data-model/m/m_costhistory.md) | `model_column_missing` | `columns.DateAcct` | unexplained |
| [M_COSTHISTORY](../data-model/m/m_costhistory.md) | `model_column_missing` | `columns.IsBackDate` | unexplained |
| [M_COST](../data-model/m/m_cost.md) | `mandatory_but_nullable` | `columns.CurrentCostPriceLL.nullable` | unexplained |
| [M_COST](../data-model/m/m_cost.md) | `mandatory_but_nullable` | `columns.FutureCostPrice.nullable` | unexplained |
| [M_EDI](../data-model/m/m_edi.md) | `table_without_model` | `model_class` | unexplained |
| [M_EDI_INFO](../data-model/m/m_edi_info.md) | `table_without_model` | `model_class` | unexplained |
| [M_INOUTLINE](../data-model/m/m_inoutline.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [M_INOUTLINE](../data-model/m/m_inoutline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_INOUTLINE](../data-model/m/m_inoutline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_INOUT](../data-model/m/m_inout.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_INOUT](../data-model/m/m_inout.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_INVENTORYLINE](../data-model/m/m_inventoryline.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [M_INVENTORYLINE](../data-model/m/m_inventoryline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_INVENTORYLINE](../data-model/m/m_inventoryline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_INVENTORYLINE](../data-model/m/m_inventoryline.md) | `model_column_missing` | `columns.C_UOM_ID` | unexplained |
| [M_INVENTORYLINE](../data-model/m/m_inventoryline.md) | `model_column_missing` | `columns.QtyEntered` | unexplained |
| [M_INVENTORY](../data-model/m/m_inventory.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_INVENTORY](../data-model/m/m_inventory.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_LOCATOR](../data-model/m/m_locator.md) | `mandatory_but_nullable` | `columns.X.nullable` | unexplained |
| [M_LOCATOR](../data-model/m/m_locator.md) | `mandatory_but_nullable` | `columns.Y.nullable` | unexplained |
| [M_LOCATOR](../data-model/m/m_locator.md) | `mandatory_but_nullable` | `columns.Z.nullable` | unexplained |
| [M_MATCHINV](../data-model/m/m_matchinv.md) | `mandatory_but_nullable` | `columns.DateAcct.nullable` | unexplained |
| [M_MATCHINV](../data-model/m/m_matchinv.md) | `mandatory_but_nullable` | `columns.M_Product_ID.nullable` | unexplained |
| [M_MATCHPO](../data-model/m/m_matchpo.md) | `mandatory_but_nullable` | `columns.DateAcct.nullable` | unexplained |
| [M_MATCHPO](../data-model/m/m_matchpo.md) | `mandatory_but_nullable` | `columns.M_InOutLine_ID.nullable` | unexplained |
| [M_MATCHPO](../data-model/m/m_matchpo.md) | `mandatory_but_nullable` | `columns.M_Product_ID.nullable` | unexplained |
| [M_MOVEMENTLINE](../data-model/m/m_movementline.md) | `mandatory_but_nullable` | `columns.Line.nullable` | unexplained |
| [M_MOVEMENTLINE](../data-model/m/m_movementline.md) | `mandatory_but_nullable` | `columns.TargetQty.nullable` | unexplained |
| [M_MOVEMENTLINE](../data-model/m/m_movementline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_MOVEMENTLINE](../data-model/m/m_movementline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_MOVEMENTLINE](../data-model/m/m_movementline.md) | `model_column_missing` | `columns.C_UOM_ID` | unexplained |
| [M_MOVEMENTLINE](../data-model/m/m_movementline.md) | `model_column_missing` | `columns.QtyEntered` | unexplained |
| [M_MOVEMENT](../data-model/m/m_movement.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_MOVEMENT](../data-model/m/m_movement.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_PRICELIST_TRL](../data-model/m/m_pricelist_trl.md) | `table_without_model` | `model_class` | unexplained |
| [M_PRICELIST_VERSION_TRL](../data-model/m/m_pricelist_version_trl.md) | `table_without_model` | `model_class` | unexplained |
| [M_PRODUCTIONLINE](../data-model/m/m_productionline.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [M_PRODUCTIONLINE](../data-model/m/m_productionline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_PRODUCTIONLINE](../data-model/m/m_productionline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_PRODUCTION](../data-model/m/m_production.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_PRODUCTION](../data-model/m/m_production.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_PRODUCT](../data-model/m/m_product.md) | `mandatory_but_nullable` | `columns.IsPhantom.nullable` | unexplained |
| [M_PRODUCT](../data-model/m/m_product.md) | `mandatory_but_nullable` | `columns.M_AttributeSetInstance_ID.nullable` | unexplained |
| [M_PRODUCT](../data-model/m/m_product.md) | `model_column_missing` | `columns.IsBOMPriceOverride` | unexplained |
| [M_PRODUCT_ACCT](../data-model/m/m_product_acct.md) | `mandatory_but_nullable` | `columns.P_CostAdjustment_Acct.nullable` | unexplained |
| [M_PRODUCT_ACCT](../data-model/m/m_product_acct.md) | `mandatory_but_nullable` | `columns.P_InventoryClearing_Acct.nullable` | unexplained |
| [M_PRODUCT_ACCT](../data-model/m/m_product_acct.md) | `mandatory_but_nullable` | `columns.P_RateVariance_Acct.nullable` | unexplained |
| [M_PRODUCT_BOM_OLD](../data-model/m/m_product_bom_old.md) | `table_without_model` | `model_class` | unexplained |
| [M_PRODUCT_CATEGORY_ACCT](../data-model/m/m_product_category_acct.md) | `mandatory_but_nullable` | `columns.P_CostAdjustment_Acct.nullable` | unexplained |
| [M_PRODUCT_CATEGORY_ACCT](../data-model/m/m_product_category_acct.md) | `mandatory_but_nullable` | `columns.P_InventoryClearing_Acct.nullable` | unexplained |
| [M_PRODUCT_CATEGORY_ACCT](../data-model/m/m_product_category_acct.md) | `mandatory_but_nullable` | `columns.P_RateVariance_Acct.nullable` | unexplained |
| [M_PRODUCT_CATEGORY_TRL](../data-model/m/m_product_category_trl.md) | `table_without_model` | `model_class` | unexplained |
| [M_PRODUCT_TRL](../data-model/m/m_product_trl.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTIONDISTRIBUTION](../data-model/m/m_promotiondistribution.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTIONGROUPLINE](../data-model/m/m_promotiongroupline.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTIONGROUP](../data-model/m/m_promotiongroup.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTIONLINE](../data-model/m/m_promotionline.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTIONPRECONDITION](../data-model/m/m_promotionprecondition.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTIONREWARD](../data-model/m/m_promotionreward.md) | `table_without_model` | `model_class` | unexplained |
| [M_PROMOTION](../data-model/m/m_promotion.md) | `table_without_model` | `model_class` | unexplained |
| [M_RMALINE](../data-model/m/m_rmaline.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [M_RMALINE](../data-model/m/m_rmaline.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [M_RMA](../data-model/m/m_rma.md) | `mandatory_but_nullable` | `columns.M_RMAType_ID.nullable` | unexplained |
| [M_SUBSTITUTE](../data-model/m/m_substitute.md) | `mandatory_but_nullable` | `columns.Name.nullable` | unexplained |
| [M_WAREHOUSE](../data-model/m/m_warehouse.md) | `model_column_missing` | `columns.IsDisableInventoryPopup` | unexplained |
| [PA_DASHBOARDCONTENT_TRL](../data-model/pa/pa_dashboardcontent_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PA_DOCUMENTSTATUS](../data-model/pa/pa_documentstatus.md) | `model_column_missing` | `columns.AD_FieldGroup_ID` | unexplained |
| [PA_DOCUMENTSTATUS](../data-model/pa/pa_documentstatus.md) | `model_column_missing` | `columns.AD_InfoWindow_ID` | unexplained |
| [PA_DOCUMENTSTATUS](../data-model/pa/pa_documentstatus.md) | `model_column_missing` | `columns.AD_Process_ID` | unexplained |
| [PA_DOCUMENTSTATUS](../data-model/pa/pa_documentstatus.md) | `model_column_missing` | `columns.Help` | unexplained |
| [PA_DOCUMENTSTATUS](../data-model/pa/pa_documentstatus.md) | `model_column_missing` | `columns.IsHideWhenZero` | unexplained |
| [PA_DOCUMENTSTATUS](../data-model/pa/pa_documentstatus.md) | `model_column_missing` | `columns.Name_PrintColorZero_ID` | unexplained |
| [PA_DOCUMENTSTATUS_TRL](../data-model/pa/pa_documentstatus_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PA_GOAL](../data-model/pa/pa_goal.md) | `mandatory_but_nullable` | `columns.GoalPerformance.nullable` | unexplained |
| [PA_GOAL](../data-model/pa/pa_goal.md) | `mandatory_but_nullable` | `columns.MeasureActual.nullable` | unexplained |
| [PA_GOAL](../data-model/pa/pa_goal.md) | `mandatory_but_nullable` | `columns.RelativeWeight.nullable` | unexplained |
| [PA_REPORTCOLUMN_TRL](../data-model/pa/pa_reportcolumn_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PA_REPORTLINE_TRL](../data-model/pa/pa_reportline_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_ORDER](../data-model/pp/pp_order.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [PP_ORDER](../data-model/pp/pp_order.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [PP_ORDER_BOMLINE_TRL](../data-model/pp/pp_order_bomline_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_ORDER_BOM_TRL](../data-model/pp/pp_order_bom_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_ORDER_NODE_TRL](../data-model/pp/pp_order_node_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_ORDER_WORKFLOW](../data-model/pp/pp_order_workflow.md) | `mandatory_but_nullable` | `columns.Cost.nullable` | unexplained |
| [PP_ORDER_WORKFLOW_TRL](../data-model/pp/pp_order_workflow_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_PRODUCT_BOMLINE_TRL](../data-model/pp/pp_product_bomline_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_PRODUCT_BOM_TRL](../data-model/pp/pp_product_bom_trl.md) | `table_without_model` | `model_class` | unexplained |
| [PP_WF_NODE_ASSET](../data-model/pp/pp_wf_node_asset.md) | `duplicate_definition` | `columns` | unexplained |
| [R_ISSUESOURCE](../data-model/r/r_issuesource.md) | `table_without_model` | `model_class` | unexplained |
| [R_MAILTEXT](../data-model/r/r_mailtext.md) | `mandatory_but_nullable` | `columns.MailText.nullable` | unexplained |
| [R_MAILTEXT_TRL](../data-model/r/r_mailtext_trl.md) | `table_without_model` | `model_class` | unexplained |
| [R_REQUEST](../data-model/r/r_request.md) | `model_column_missing` | `columns.C_CostCenter_ID` | unexplained |
| [R_REQUEST](../data-model/r/r_request.md) | `model_column_missing` | `columns.C_Department_ID` | unexplained |
| [SSO_PRINCIPALCONFIG](../data-model/sso/sso_principalconfig.md) | `model_column_missing` | `columns.SSO_LoginButtonImage_ID` | unexplained |
| [S_TIMEEXPENSELINE](../data-model/s/s_timeexpenseline.md) | `mandatory_but_nullable` | `columns.DateExpense.nullable` | unexplained |
| [TESTUU_TRL](../data-model/testuu/testuu_trl.md) | `table_without_model` | `model_class` | unexplained |
| [T_FACT_ACCT_HISTORY](../data-model/t/t_fact_acct_history.md) | `model_table_missing` | `database_table` | unexplained |
| [U_BLACKLISTCHEQUE](../data-model/u/u_blacklistcheque.md) | `table_without_model` | `model_class` | unexplained |
| [W_ADVERTISEMENT](../data-model/w/w_advertisement.md) | `table_without_model` | `model_class` | unexplained |
| [W_BASKETLINE](../data-model/w/w_basketline.md) | `table_without_model` | `model_class` | unexplained |
| [W_BASKET](../data-model/w/w_basket.md) | `table_without_model` | `model_class` | unexplained |
| [W_CLICKCOUNT](../data-model/w/w_clickcount.md) | `table_without_model` | `model_class` | unexplained |
| [W_CLICK](../data-model/w/w_click.md) | `table_without_model` | `model_class` | unexplained |
| [W_COUNTERCOUNT](../data-model/w/w_countercount.md) | `table_without_model` | `model_class` | unexplained |
| [W_COUNTER](../data-model/w/w_counter.md) | `table_without_model` | `model_class` | unexplained |
| [W_MAILMSG](../data-model/w/w_mailmsg.md) | `table_without_model` | `model_class` | unexplained |
| [W_MAILMSG_TRL](../data-model/w/w_mailmsg_trl.md) | `table_without_model` | `model_class` | unexplained |
| [W_STORE](../data-model/w/w_store.md) | `table_without_model` | `model_class` | unexplained |
| [W_STORE_TRL](../data-model/w/w_store_trl.md) | `table_without_model` | `model_class` | unexplained |
| `AD_COLUMN_SYNC` | `routine_text_differs` | `text` | unexplained |

## Invalid database objects

| kind | name | status |
|---|---|---|
| View | `AD_ORG_V` | INVALID |
| View | `C_DUNNING_HEADER_VT` | INVALID |
| View | `C_DUNNING_HEADER_V` | INVALID |
| View | `C_INVOICE_CANDIDATE_V` | INVALID |
| View | `C_INVOICE_HEADER_VT` | INVALID |
| View | `C_INVOICE_HEADER_V` | INVALID |
| View | `C_ORDER_HEADER_VT` | INVALID |
| View | `C_ORDER_HEADER_V` | INVALID |
| View | `C_ORDER_LINETAX_VT` | INVALID |
| View | `C_ORDER_LINETAX_V` | INVALID |
| View | `C_PAYSELECTION_CHECK_VT` | INVALID |
| View | `C_PAYSELECTION_CHECK_V` | INVALID |
| View | `C_PROJECT_HEADER_VT` | INVALID |
| View | `C_PROJECT_HEADER_V` | INVALID |
| View | `C_RFQRESPONSE_VT` | INVALID |
| View | `C_RFQRESPONSE_V` | INVALID |
| View | `DD_ORDER_HEADER_VT` | INVALID |
| View | `DD_ORDER_HEADER_V` | INVALID |
| View | `M_INOUT_HEADER_VT` | INVALID |
| View | `M_INOUT_HEADER_V` | INVALID |
| View | `RV_BPARTNER` | INVALID |
| View | `RV_C_INVOICELINE` | INVALID |
| View | `RV_C_INVOICE_CUSTOMERPRODQTR` | INVALID |
| View | `RV_C_INVOICE_CUSTOMERVENDQTR` | INVALID |
| View | `RV_C_INVOICE_DAY` | INVALID |
| View | `RV_C_INVOICE_MONTH` | INVALID |
| View | `RV_C_INVOICE_PRODMONTH` | INVALID |
| View | `RV_C_INVOICE_PRODUCTMONTH` | INVALID |
| View | `RV_C_INVOICE_PRODUCTQTR` | INVALID |
| View | `RV_C_INVOICE_PRODWEEK` | INVALID |
| View | `RV_C_INVOICE_VENDORMONTH` | INVALID |
| View | `RV_C_INVOICE_WEEK` | INVALID |
| View | `RV_C_INVOICE` | INVALID |
| View | `RV_DD_ORDERDETAIL` | INVALID |
| View | `RV_FACT_ACCT` | INVALID |
| View | `RV_FACT_ADAXA` | INVALID |
| View | `RV_FACT_SIMPLE` | INVALID |
| View | `RV_OPENITEMTODATE` | INVALID |
| View | `RV_OPENITEM` | INVALID |
| View | `T_RV_RECONCILIATION` | INVALID |

## Write behaviour classes

| updates | deletes | tables |
|---|---|---|
| `no_updated_column` | deleted_by_app, deleted_by_users, deleted_by_cascade | 1 |
| `no_updated_column` | deleted_by_users, deleted_by_cascade | 1 |
| `no_updated_column` | never_deleted_in_code | 3 |
| `po_only` | deleted_by_app | 3 |
| `po_only` | deleted_by_app, deleted_by_cascade | 4 |
| `po_only` | deleted_by_app, deleted_by_users | 24 |
| `po_only` | deleted_by_app, deleted_by_users, deleted_by_cascade | 18 |
| `po_only` | deleted_by_cascade | 52 |
| `po_only` | deleted_by_users | 434 |
| `po_only` | deleted_by_users, deleted_by_cascade | 127 |
| `po_only` | deleted_by_users, purged | 1 |
| `po_only` | never_deleted_in_code | 3 |
| `po_only` | soft_delete_only | 46 |
| `raw_sql_sets_updated` | deleted_by_app, deleted_by_users, deleted_by_cascade | 2 |
| `raw_sql_sets_updated` | deleted_by_cascade | 2 |
| `raw_sql_sets_updated` | deleted_by_users, deleted_by_cascade | 2 |
| `raw_sql_sets_updated` | soft_delete_only | 1 |
| `raw_sql_skips_updated` | deleted_by_app | 2 |
| `raw_sql_skips_updated` | deleted_by_app, deleted_by_cascade | 2 |
| `raw_sql_skips_updated` | deleted_by_app, deleted_by_users | 10 |
| `raw_sql_skips_updated` | deleted_by_app, deleted_by_users, deleted_by_cascade | 17 |
| `raw_sql_skips_updated` | deleted_by_app, purged | 2 |
| `raw_sql_skips_updated` | deleted_by_cascade | 13 |
| `raw_sql_skips_updated` | deleted_by_users | 35 |
| `raw_sql_skips_updated` | deleted_by_users, deleted_by_cascade | 37 |
| `raw_sql_skips_updated` | deleted_by_users, purged | 2 |
| `raw_sql_skips_updated` | soft_delete_only | 6 |
