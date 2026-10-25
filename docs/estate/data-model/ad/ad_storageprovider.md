---
title: "AD_STORAGEPROVIDER"
order: 172
ekos_generated: true
ekos_estate_version: 1
---

# AD_STORAGEPROVIDER

Area [AD](../../data-model/ad/index.md) · class **config** (proposed) · read from database `idempiere-db` (owner `ADEMPIERE`) · 0 row(s) when profiled

Application model: `org.compiere.model.X_AD_StorageProvider`, access level 6 - System - Client.

## Columns

| column | type | key | not null | business name | references (code) | nulls | distinct |
|---|---|---|---|---|---|---|---|
| `AD_CLIENT_ID` | NUMBER(10,0) |  | yes | Tenant |  | 0 | 0 |
| `AD_ORG_ID` | NUMBER(10,0) |  | yes | Organization |  | 0 | 0 |
| `AD_STORAGEPROVIDER_ID` | NUMBER(10,0) | PK | yes | Storage Provider |  | 0 | 0 |
| `AD_STORAGEPROVIDER_UU` | VARCHAR2(36 CHAR) |  |  | AD_StorageProvider_UU |  | 0 | 0 |
| `CREATED` | DATE |  | yes | Created |  | 0 | 0 |
| `CREATEDBY` | NUMBER(10,0) |  | yes | Created By |  | 0 | 0 |
| `FOLDER` | VARCHAR2(255 CHAR) |  |  | Folder |  | 0 | 0 |
| `ISACTIVE` | CHAR(1) |  | yes | Active |  | 0 | 0 |
| `METHOD` | VARCHAR2(60 CHAR) |  |  | Method |  | 0 | 0 |
| `NAME` | VARCHAR2(60 CHAR) |  | yes | Name |  | 0 | 0 |
| `PASSWORD` | VARCHAR2(255 CHAR) |  |  |  |  | 0 | 0 |
| `UPDATED` | DATE |  | yes | Updated |  | 0 | 0 |
| `UPDATEDBY` | NUMBER(10,0) |  | yes | Updated By |  | 0 | 0 |
| `URL` | VARCHAR2(225 CHAR) |  |  | URL |  | 0 | 0 |
| `USERNAME` | VARCHAR2(60 CHAR) |  |  | User Name |  | 0 | 0 |
| `ISDEFAULT` | CHAR(1) |  | yes | Default |  | 0 | 0 |

*references (code)* is the table the application model's code says a column points to; *Foreign keys* below are the constraints the database declares. Counts come from the profile; no value is ever shown.

## Check constraints

| name | expression |
|---|---|
| `SYS_C0022019` | `IsDefault IN ('Y','N')` |
| `SYS_C0022021` | `IsActive IN ('Y','N')` |

## Foreign keys

**References**

_None._

**Referenced by**

| table | columns | on delete |
|---|---|---|
| [AD_ARCHIVE](../../data-model/ad/ad_archive.md) | AD_ARCHIVE.AD_STORAGEPROVIDER_ID → AD_STORAGEPROVIDER.AD_STORAGEPROVIDER_ID | NO ACTION |
| [AD_ATTACHMENT](../../data-model/ad/ad_attachment.md) | AD_ATTACHMENT.AD_STORAGEPROVIDER_ID → AD_STORAGEPROVIDER.AD_STORAGEPROVIDER_ID | NO ACTION |
| [AD_CLIENTINFO](../../data-model/ad/ad_clientinfo.md) | AD_CLIENTINFO.AD_STORAGEPROVIDER_ID → AD_STORAGEPROVIDER.AD_STORAGEPROVIDER_ID | NO ACTION |
| [AD_IMAGE](../../data-model/ad/ad_image.md) | AD_IMAGE.AD_STORAGEPROVIDER_ID → AD_STORAGEPROVIDER.AD_STORAGEPROVIDER_ID | NO ACTION |

```mermaid
erDiagram
  AD_STORAGEPROVIDER ||--o{ AD_ARCHIVE : ""
  AD_STORAGEPROVIDER ||--o{ AD_ATTACHMENT : ""
  AD_STORAGEPROVIDER ||--o{ AD_CLIENTINFO : ""
  AD_STORAGEPROVIDER ||--o{ AD_IMAGE : ""
```

## Write behaviour

- updates: **po_only**
- deletes: **deleted_by_users**
- change log: **recorded**
- evidence: 1 citation(s)

## Schema history

39 change(s); the latest:

| applied | release | operation | column | tickets |
|---|---|---|---|---|
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2023-04-09T15:47 | iD11 | `add_constraint` |  | IDEMPIERE-5567 |
| 2021-04-16T17:30 | i8.2 | `add_column` | IsDefault | IDEMPIERE-4763 |
| 2021-04-16T17:30 | i8.2 | `add_column` | IsDefault | IDEMPIERE-4763 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_2_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_1_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `drop_column` | tmp_col_6_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | USERNAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | NAME | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_3_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | AD_STORAGEPROVIDER_UU | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_5_tmp | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | URL | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `modify_column` | PASSWORD | IDEMPIERE-3862 |
| 2020-08-04T01:00 | i7.1z | `add_column` | tmp_col_7_tmp | IDEMPIERE-3862 |

## Notes

<!-- ekos:manual id="table.ad_storageprovider.notes" -->
_Business notes about this table._
<!-- /ekos:manual -->
