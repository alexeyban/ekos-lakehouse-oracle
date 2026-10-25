---
title: "AD_CLIENT"
order: 26
ekos_generated: true
ekos_estate_version: 1
---

# AD_CLIENT

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 2 row(s) when profiled

Application model: `org.compiere.model.X_AD_Client`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) | PK | yes | Tenant |  | 0 | 2 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 1 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 1 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 1 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 1 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 2 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 1 |
| `VALUE` | VARCHAR2(40 CHAR) |  | yes | Search Key |  | 0 | 2 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 2 |
| `DESCRIPTION` | VARCHAR2(255 CHAR) |  |  | Description |  | 0 | 2 |
| `SMTPHOST` | VARCHAR2(60 CHAR) |  |  | Mail Host |  | 2 | 0 |
| `REQUESTEMAIL` | VARCHAR2(60 CHAR) |  |  | Request EMail |  | 0 | 1 |
| `REQUESTUSER` | VARCHAR2(60 CHAR) |  |  | Request User |  | 0 | 1 |
| `REQUESTUSERPW` | VARCHAR2(255 CHAR) |  |  | Request User Password |  | 0 | 1 |
| `REQUESTFOLDER` | VARCHAR2(20 CHAR) |  |  | Request Folder |  | 0 | 1 |
| `AD_LANGUAGE` | VARCHAR2(6 CHAR) |  |  | Language |  | 0 | 1 |
| `ISMULTILINGUALDOCUMENT` | CHAR(1) |  | yes | Multi Lingual Documents |  | 0 | 1 |
| `ISSMTPAUTHORIZATION` | CHAR(1) |  | yes | SMTP Authentication |  | 0 | 1 |
| `ISUSEBETAFUNCTIONS` | CHAR(1) |  | yes | Use Beta Functions |  | 0 | 1 |
| `LDAPQUERY` | VARCHAR2(255 CHAR) |  |  |  |  | 2 | 0 |
| `MODELVALIDATIONCLASSES` | VARCHAR2(255 CHAR) |  |  | Model Validation Classes |  | 2 | 0 |
| `AUTOARCHIVE` | CHAR(1) |  | yes | Auto Archive |  | 0 | 1 |
| `MMPOLICY` | CHAR(1) |  | yes | Material Policy |  | 0 | 1 |
| `EMAILTEST` | CHAR(1) |  |  | EMail Test |  | 2 | 0 |
| `ISSERVEREMAIL` | CHAR(1) |  |  |  |  | 0 | 1 |
| `DOCUMENTDIR` | VARCHAR2(60 CHAR) |  |  | Document Directory |  | 2 | 0 |
| `ISPOSTIMMEDIATE` | CHAR(1) |  | yes | Post Immediately (Deprecated) |  | 0 | 1 |
| `ISCOSTIMMEDIATE` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `STOREATTACHMENTSONFILESYSTEM` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `WINDOWSATTACHMENTPATH` | VARCHAR2(255 CHAR) |  |  |  |  | 2 | 0 |
| `UNIXATTACHMENTPATH` | VARCHAR2(255 CHAR) |  |  |  |  | 2 | 0 |
| `STOREARCHIVEONFILESYSTEM` | CHAR(1) |  | yes |  |  | 0 | 1 |
| `WINDOWSARCHIVEPATH` | VARCHAR2(255 CHAR) |  |  |  |  | 2 | 0 |
| `UNIXARCHIVEPATH` | VARCHAR2(255 CHAR) |  |  |  |  | 2 | 0 |
| `ISUSEASP` | CHAR(1) |  | yes | Is Use ASP |  | 0 | 1 |
| `AD_REPLICATIONSTRATEGY_ID` | NUMBER(10,0) |  |  | Replication Strategy | [AD_REPLICATIONSTRATEGY](../../data-model/ad/ad_replicationstrategy.md) | 2 | 0 |
| `AD_CLIENT_UU` | VARCHAR2(36 CHAR) |  |  | AD_Client_UU |  | 0 | 2 |
| `AD_PASSWORDRULE_ID` | NUMBER(10,0) |  |  | Password Policies | [AD_PASSWORDRULE](../../data-model/ad/ad_passwordrule.md) | 2 | 0 |
| `ISSECURESMTP` | CHAR(1) |  | yes | SMTP SSL/TLS |  | 0 | 1 |
| `SMTPPORT` | NUMBER(10,0) |  |  | SMTP Port |  | 2 | 0 |
| `LOGINPREFIX` | VARCHAR2(40 CHAR) |  |  | Login Prefix |  | 2 | 0 |
| `AUTHENTICATIONTYPE` | VARCHAR2(10 CHAR) |  | yes | Authentication Type |  | 0 | 1 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0021965` | `IsActive in ('Y','N')` |
| `SYS_C0021968` | `IsSecureSMTP IN ('Y','N')` |
| `SYS_C0021969` | `IsUseASP IN ('Y','N')` |

## Foreign keys

**References**

| table | columns | on delete |
|---|---|---|
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_CLIENT.AD_LANGUAGE → AD_LANGUAGE.AD_LANGUAGE | NO ACTION |
| [AD_PASSWORDRULE](../../data-model/ad/ad_passwordrule.md) | AD_CLIENT.AD_PASSWORDRULE_ID → AD_PASSWORDRULE.AD_PASSWORDRULE_ID | NO ACTION |
| [AD_REPLICATIONSTRATEGY](../../data-model/ad/ad_replicationstrategy.md) | AD_CLIENT.AD_REPLICATIONSTRATEGY_ID → AD_REPLICATIONSTRATEGY.AD_REPLICATIONSTRATEGY_ID | NO ACTION |

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_BROADCASTMESSAGE](../../data-model/ad/ad_broadcastmessage.md) | AD_BROADCASTMESSAGE.NOTIFICATION_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_BROADCASTMESSAGE_TRL](../../data-model/ad/ad_broadcastmessage_trl.md) | AD_BROADCASTMESSAGE_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_CHART_TRL](../../data-model/ad/ad_chart_trl.md) | AD_CHART_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_CLIENTINFO](../../data-model/ad/ad_clientinfo.md) | AD_CLIENTINFO.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | CASCADE |
| [AD_CLIENTSHARE](../../data-model/ad/ad_clientshare.md) | AD_CLIENTSHARE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_COLOR_TRL](../../data-model/ad/ad_color_trl.md) | AD_COLOR_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_COLUMN](../../data-model/ad/ad_column.md) | AD_COLUMN.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_CTXHELPSUGGESTION](../../data-model/ad/ad_ctxhelpsuggestion.md) | AD_CTXHELPSUGGESTION.AD_USERCLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_FIELD](../../data-model/ad/ad_field.md) | AD_FIELD.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_FIELDSUGGESTION](../../data-model/ad/ad_fieldsuggestion.md) | AD_FIELDSUGGESTION.AD_USERCLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_IMPORTTEMPLATE](../../data-model/ad/ad_importtemplate.md) | AD_IMPORTTEMPLATE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_IMPORTTEMPLATEACCESS](../../data-model/ad/ad_importtemplateaccess.md) | AD_IMPORTTEMPLATEACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_INFORELATED](../../data-model/ad/ad_inforelated.md) | AD_INFORELATED.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_LABELCATEGORY_TRL](../../data-model/ad/ad_labelcategory_trl.md) | AD_LABELCATEGORY_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_LABEL_TRL](../../data-model/ad/ad_label_trl.md) | AD_LABEL_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_LANGUAGE](../../data-model/ad/ad_language.md) | AD_LANGUAGE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_MENU](../../data-model/ad/ad_menu.md) | AD_MENU.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_MESSAGE](../../data-model/ad/ad_message.md) | AD_MESSAGE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_MODELGENERATORTEMPLATE](../../data-model/ad/ad_modelgeneratortemplate.md) | AD_MODELGENERATORTEMPLATE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ORG](../../data-model/ad/ad_org.md) | AD_ORG.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_PASSWORD_HISTORY](../../data-model/ad/ad_password_history.md) | AD_PASSWORD_HISTORY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_POSTIT](../../data-model/ad/ad_postit.md) | AD_POSTIT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_PREFERENCE](../../data-model/ad/ad_preference.md) | AD_PREFERENCE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_PRINTCOLOR_TRL](../../data-model/ad/ad_printcolor_trl.md) | AD_PRINTCOLOR_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_PRINTFORM](../../data-model/ad/ad_printform.md) | AD_PRINTFORM.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_PROCESS_ACCESS](../../data-model/ad/ad_process_access.md) | AD_PROCESS_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_REFERENCE](../../data-model/ad/ad_reference.md) | AD_REFERENCE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_REF_LIST](../../data-model/ad/ad_ref_list.md) | AD_REF_LIST.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_REF_TABLE](../../data-model/ad/ad_ref_table.md) | AD_REF_TABLE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_REPLICATION](../../data-model/ad/ad_replication.md) | AD_REPLICATION.REMOTE_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_REPORTVIEW_COLUMN](../../data-model/ad/ad_reportview_column.md) | AD_REPORTVIEW_COLUMN.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_ROLE](../../data-model/ad/ad_role.md) | AD_ROLE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_SEQUENCE](../../data-model/ad/ad_sequence.md) | AD_SEQUENCE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_SEQUENCE_AUDIT](../../data-model/ad/ad_sequence_audit.md) | AD_SEQUENCE_AUDIT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_SEQUENCE_NO](../../data-model/ad/ad_sequence_no.md) | AD_SEQUENCE_NO.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_STATUSLINE](../../data-model/ad/ad_statusline.md) | AD_STATUSLINE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_STATUSLINEUSEDIN](../../data-model/ad/ad_statuslineusedin.md) | AD_STATUSLINEUSEDIN.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TAB](../../data-model/ad/ad_tab.md) | AD_TAB.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TABLE](../../data-model/ad/ad_table.md) | AD_TABLE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TABLEVALRULE](../../data-model/ad/ad_tablevalrule.md) | AD_TABLEVALRULE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TABLE_ACCESS](../../data-model/ad/ad_table_access.md) | AD_TABLE_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TASK](../../data-model/ad/ad_task.md) | AD_TASK.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TASKINSTANCE](../../data-model/ad/ad_taskinstance.md) | AD_TASKINSTANCE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_TASK_ACCESS](../../data-model/ad/ad_task_access.md) | AD_TASK_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_USER](../../data-model/ad/ad_user.md) | AD_USER.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_USERDEF_THEME](../../data-model/ad/ad_userdef_theme.md) | AD_USERDEF_THEME.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_USERDEF_THEME_DETAIL](../../data-model/ad/ad_userdef_theme_detail.md) | AD_USERDEF_THEME_DETAIL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_USERPREFERENCE](../../data-model/ad/ad_userpreference.md) | AD_USERPREFERENCE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_USER_ROLES](../../data-model/ad/ad_user_roles.md) | AD_USER_ROLES.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_VAL_RULE](../../data-model/ad/ad_val_rule.md) | AD_VAL_RULE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_VERIFYMIGRATION](../../data-model/ad/ad_verifymigration.md) | AD_VERIFYMIGRATION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WF_NODE](../../data-model/ad/ad_wf_node.md) | AD_WF_NODE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WF_NODENEXT](../../data-model/ad/ad_wf_nodenext.md) | AD_WF_NODENEXT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WF_PROCESS](../../data-model/ad/ad_wf_process.md) | AD_WF_PROCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WINDOW](../../data-model/ad/ad_window.md) | AD_WINDOW.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WINDOW_ACCESS](../../data-model/ad/ad_window_access.md) | AD_WINDOW_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WORKFLOW](../../data-model/ad/ad_workflow.md) | AD_WORKFLOW.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [AD_WORKFLOW_ACCESS](../../data-model/ad/ad_workflow_access.md) | AD_WORKFLOW_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [A_ASSET_GROUP_TRL](../../data-model/a/a_asset_group_trl.md) | A_ASSET_GROUP_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ACCTSCHEMA](../../data-model/c/c_acctschema.md) | C_ACCTSCHEMA.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ACCTSCHEMA_ELEMENT](../../data-model/c/c_acctschema_element.md) | C_ACCTSCHEMA_ELEMENT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ACTIVITY_TRL](../../data-model/c/c_activity_trl.md) | C_ACTIVITY_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ADDRESSTRANSACTION](../../data-model/c/c_addresstransaction.md) | C_ADDRESSTRANSACTION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ADDRESSVALIDATION](../../data-model/c/c_addressvalidation.md) | C_ADDRESSVALIDATION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ADDRESSVALIDATIONCFG](../../data-model/c/c_addressvalidationcfg.md) | C_ADDRESSVALIDATIONCFG.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_BPARTNER](../../data-model/c/c_bpartner.md) | C_BPARTNER.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_BPARTNER_LOCATION](../../data-model/c/c_bpartner_location.md) | C_BPARTNER_LOCATION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_CALENDAR](../../data-model/c/c_calendar.md) | C_CALENDAR.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_CAMPAIGN_TRL](../../data-model/c/c_campaign_trl.md) | C_CAMPAIGN_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_CITY](../../data-model/c/c_city.md) | C_CITY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_CONVERSION_RATE](../../data-model/c/c_conversion_rate.md) | C_CONVERSION_RATE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_COUNTRY](../../data-model/c/c_country.md) | C_COUNTRY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_COUNTRYGROUP](../../data-model/c/c_countrygroup.md) | C_COUNTRYGROUP.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_COUNTRYGROUPCOUNTRY](../../data-model/c/c_countrygroupcountry.md) | C_COUNTRYGROUPCOUNTRY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_COUNTRYGROUP_TRL](../../data-model/c/c_countrygroup_trl.md) | C_COUNTRYGROUP_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_CURRENCY](../../data-model/c/c_currency.md) | C_CURRENCY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_DOCBASEGROUP](../../data-model/c/c_docbasegroup.md) | C_DOCBASEGROUP.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_DOCBASEGROUPLINE](../../data-model/c/c_docbasegroupline.md) | C_DOCBASEGROUPLINE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ELEMENT](../../data-model/c/c_element.md) | C_ELEMENT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ELEMENTVALUE](../../data-model/c/c_elementvalue.md) | C_ELEMENTVALUE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_LOCATION](../../data-model/c/c_location.md) | C_LOCATION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_NONBUSINESSDAY](../../data-model/c/c_nonbusinessday.md) | C_NONBUSINESSDAY.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_ORDERSOURCE](../../data-model/c/c_ordersource.md) | C_ORDERSOURCE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_PERIOD](../../data-model/c/c_period.md) | C_PERIOD.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_PROJECT](../../data-model/c/c_project.md) | C_PROJECT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_RECURRINGGROUP](../../data-model/c/c_recurringgroup.md) | C_RECURRINGGROUP.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_REGION](../../data-model/c/c_region.md) | C_REGION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_REGION_TRL](../../data-model/c/c_region_trl.md) | C_REGION_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_REVENUERECOG_SERVICE](../../data-model/c/c_revenuerecog_service.md) | C_REVENUERECOG_SERVICE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_SALESREGION_TRL](../../data-model/c/c_salesregion_trl.md) | C_SALESREGION_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_SALESSTAGE_TRL](../../data-model/c/c_salesstage_trl.md) | C_SALESSTAGE_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_TAXPROVIDER](../../data-model/c/c_taxprovider.md) | C_TAXPROVIDER.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_TAXPROVIDERCFG](../../data-model/c/c_taxprovidercfg.md) | C_TAXPROVIDERCFG.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_UOM](../../data-model/c/c_uom.md) | C_UOM.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_UOM_CONVERSION](../../data-model/c/c_uom_conversion.md) | C_UOM_CONVERSION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_VALIDCOMBINATION](../../data-model/c/c_validcombination.md) | C_VALIDCOMBINATION.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [C_YEAR](../../data-model/c/c_year.md) | C_YEAR.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [FACT_ACCT](../../data-model/fact/fact_acct.md) | FACT_ACCT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [GL_CATEGORY_TRL](../../data-model/gl/gl_category_trl.md) | GL_CATEGORY_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [GL_JOURNALLINE](../../data-model/gl/gl_journalline.md) | GL_JOURNALLINE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_ATTRIBUTEINSTANCELINE](../../data-model/m/m_attributeinstanceline.md) | M_ATTRIBUTEINSTANCELINE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_COST](../../data-model/m/m_cost.md) | M_COST.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_COSTDETAIL](../../data-model/m/m_costdetail.md) | M_COSTDETAIL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_LOCATOR](../../data-model/m/m_locator.md) | M_LOCATOR.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_LOCATORTYPE](../../data-model/m/m_locatortype.md) | M_LOCATORTYPE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_PRICELIST_TRL](../../data-model/m/m_pricelist_trl.md) | M_PRICELIST_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_PRICELIST_VERSION_TRL](../../data-model/m/m_pricelist_version_trl.md) | M_PRICELIST_VERSION_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_PRODUCT](../../data-model/m/m_product.md) | M_PRODUCT.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_PRODUCT_CATEGORY_TRL](../../data-model/m/m_product_category_trl.md) | M_PRODUCT_CATEGORY_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_PRODUCT_PO](../../data-model/m/m_product_po.md) | M_PRODUCT_PO.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| `M_STORAGERESERVATIONLOG` | M_STORAGERESERVATIONLOG.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_SUBSTITUTE](../../data-model/m/m_substitute.md) | M_SUBSTITUTE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [M_WAREHOUSE](../../data-model/m/m_warehouse.md) | M_WAREHOUSE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [PA_DASHBOARDCONTENT_ACCESS](../../data-model/pa/pa_dashboardcontent_access.md) | PA_DASHBOARDCONTENT_ACCESS.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [TESTUU](../../data-model/other/testuu.md) | TESTUU.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [TESTUUDET](../../data-model/other/testuudet.md) | TESTUUDET.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [TESTUU_TRL](../../data-model/testuu/testuu_trl.md) | TESTUU_TRL.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |
| [W_STORE](../../data-model/w/w_store.md) | W_STORE.AD_CLIENT_ID → AD_CLIENT.AD_CLIENT_ID | NO ACTION |

```mermaid
erDiagram
  AD_CLIENT ||--o{ AD_BROADCASTMESSAGE : ""
  AD_CLIENT ||--o{ AD_BROADCASTMESSAGE_TRL : ""
  AD_CLIENT ||--o{ AD_CHART_TRL : ""
  AD_CLIENT ||--o{ AD_CLIENTINFO : ""
  AD_CLIENT ||--o{ AD_CLIENTSHARE : ""
  AD_CLIENT ||--o{ AD_COLOR_TRL : ""
  AD_CLIENT ||--o{ AD_COLUMN : ""
  AD_CLIENT ||--o{ AD_CTXHELPSUGGESTION : ""
  AD_CLIENT ||--o{ AD_FIELD : ""
  AD_CLIENT ||--o{ AD_FIELDSUGGESTION : ""
  AD_CLIENT ||--o{ AD_IMPORTTEMPLATE : ""
  AD_CLIENT ||--o{ AD_IMPORTTEMPLATEACCESS : ""
  AD_CLIENT ||--o{ AD_INFORELATED : ""
  AD_CLIENT ||--o{ AD_LABELCATEGORY_TRL : ""
  AD_CLIENT ||--o{ AD_LABEL_TRL : ""
  AD_CLIENT ||--o{ AD_LANGUAGE : ""
  AD_CLIENT ||--o{ AD_MENU : ""
  AD_CLIENT ||--o{ AD_MESSAGE : ""
  AD_CLIENT ||--o{ AD_MODELGENERATORTEMPLATE : ""
  AD_CLIENT ||--o{ AD_ORG : ""
  AD_CLIENT ||--o{ AD_PASSWORD_HISTORY : ""
  AD_CLIENT ||--o{ AD_POSTIT : ""
  AD_CLIENT ||--o{ AD_PREFERENCE : ""
  AD_CLIENT ||--o{ AD_PRINTCOLOR_TRL : ""
  AD_CLIENT ||--o{ AD_PRINTFORM : ""
  AD_CLIENT ||--o{ AD_PROCESS_ACCESS : ""
  AD_CLIENT ||--o{ AD_REFERENCE : ""
  AD_CLIENT ||--o{ AD_REF_LIST : ""
  AD_LANGUAGE ||--o{ AD_CLIENT : ""
  AD_PASSWORDRULE ||--o{ AD_CLIENT : ""
```

91 more neighbour(s) not drawn.

## Write behaviour

- updates: **raw_sql_skips_updated**
- deletes: **deleted_by_app**
- change log: **recorded**
- evidence: 6 citation(s)

## Read by

| kind | name |
|---|---|
| Procedure | [AD_Synchronize](../../logic/ad_synchronize.md) |
| Procedure | [nextBusinessDay](../../logic/nextbusinessday.md) |
| Procedure | [nextbusinessday](../../logic/nextbusinessday.md) |
| View | `AD_ALLCLIENTS_V` |
| View | `AD_SESSIONINFO_V` |
| View | `RV_FACT_ADAXA` |
| View | `ad_allclients_v` |
| View | `ad_sessioninfo_v` |
| View | `rv_fact_adaxa` |

## Schema history

77 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-08-07T15:38 | iD11 | `modify_column` | AuthenticationType | IDEMPIERE-5346 |
| 2023-08-07T15:38 | iD11 | `modify_column` | AuthenticationType | IDEMPIERE-5346 |
| 2023-08-07T15:38 | iD11 | `modify_column` | AuthenticationType | IDEMPIERE-5346 |
| 2023-08-07T15:38 | iD11 | `modify_column` | AuthenticationType | IDEMPIERE-5346 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-03-28T15:10 | iD11 | `add_column` | AuthenticationType | IDEMPIERE-5346 |
| 2023-03-28T15:10 | iD11 | `add_column` | AuthenticationType | IDEMPIERE-5346 |
| 2022-09-22T19:20 | i9 | `add_column` | LoginPrefix | IDEMPIERE-5408 |
| 2022-09-22T19:20 | i9 | `create_index` |  | IDEMPIERE-5408 |
| 2022-09-22T19:20 | i9 | `add_column` | LoginPrefix | IDEMPIERE-5408 |
| 2022-09-22T19:20 | i9 | `create_index` |  | IDEMPIERE-5408 |
| 2021-12-05T16:45 | i8.2z | `drop_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |
| 2021-12-05T16:45 | i8.2z | `add_constraint` |  | IDEMPIERE-5075 |

## Notes

<!-- ekos:manual id="table.ad_client.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
