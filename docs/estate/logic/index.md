---
title: "Logic"
order: 5
ekos_generated: true
ekos_estate_version: 1
---

# Logic

92 routine(s); a name defined in the database and in files is shown once, the database's first.

| routine | language | origin | fidelity | reads | writes |
|---|---|---|---|---|---|
| [acctBalance](../logic/acctbalance.md) | plsql | live | statements | c_elementvalue |  |
| [addDays](../logic/adddays.md) | plsql | live | statements |  |  |
| [add_missing_translations](../logic/add_missing_translations.md) | plpgsql | file | statements | ad_column, ad_table |  |
| [add_months](../logic/add_months.md) | plpgsql | file | statements |  |  |
| [adempiere.adddays](../logic/adempiere.adddays.md) | plpgsql | file | statements |  |  |
| [adempiere.altercolumn](../logic/adempiere.altercolumn.md) | plpgsql | file | statements | information_schema.role_table_grants, pg_attribute, pg_class, pg_depend, pg_namespace, pg_rewrite, pg_type |  |
| [adempiere.paymenttermduedate](../logic/adempiere.paymenttermduedate.md) | plpgsql | file | statements | c_paymentterm |  |
| [adempiere.subtractdays](../logic/adempiere.subtractdays.md) | plpgsql | file | statements |  |  |
| [AD_Column_Sync](../logic/ad_column_sync.md) | plsql | live | partial | ad_column, ad_table, user_tab_columns, user_tables | ad_pinstance |
| [AD_Sequence_Doc](../logic/ad_sequence_doc.md) | plsql | live | statements |  | ad_sequence |
| [AD_Sequence_DocType](../logic/ad_sequence_doctype.md) | plsql | live | statements | c_doctype | ad_sequence |
| [AD_Sequence_Next](../logic/ad_sequence_next.md) | plsql | live | statements |  | ad_sequence |
| [AD_Synchronize](../logic/ad_synchronize.md) | plsql | file | statements | ad_client, ad_column, ad_element, ad_element_trl, ad_field, ad_form, ad_form_trl, ad_language, ad_menu, ad_printformat, ad_printformatitem, ad_process, ad_process_para, ad_process_trl, ad_tab, ad_table, ad_task, ad_task_trl, ad_wf_node, ad_window, ad_window_trl, ad_workflow, ad_workflow_trl | ad_column, ad_column_trl, ad_element, ad_element_trl, ad_field, ad_field_trl, ad_menu, ad_menu_trl, ad_pinstance, ad_printformatitem, ad_printformatitem_trl, ad_process_para, ad_process_para_trl, ad_table, ad_table_trl, ad_wf_node, ad_wf_node_trl |
| [altercolumn](../logic/altercolumn.md) | plpgsql | file | statements | pg_attribute, pg_class, pg_depend, pg_rewrite, pg_type |  |
| [asu_get1099bucket](../logic/asu_get1099bucket.md) | plpgsql | file | statements | asu_1099box, c_doctype, c_invoice, c_invoiceline |  |
| [BOMPRICELIMIT](../logic/bompricelimit.md) | plsql | live | statements | m_productprice |  |
| [BOMPRICELIST](../logic/bompricelist.md) | plsql | live | statements | m_productprice |  |
| [BOMPRICESTD](../logic/bompricestd.md) | plsql | live | statements | m_productprice |  |
| [BOMQTYAVAILABLE](../logic/bomqtyavailable.md) | plsql | live | statements |  |  |
| [bomQtyAvailableASI](../logic/bomqtyavailableasi.md) | plpgsql | file | statements |  |  |
| [BOMQTYONHAND](../logic/bomqtyonhand.md) | plsql | live | statements | c_uom, m_locator, m_product, m_storageonhand |  |
| [BomqtyonhandASI](../logic/bomqtyonhandasi.md) | plpgsql | file | statements | c_uom, m_locator, m_product, m_storage, pp_product_bom, pp_product_bomline |  |
| [BOMQTYONHANDFORRESERVATION](../logic/bomqtyonhandforreservation.md) | plsql | live | statements | c_uom, m_locator, m_locatortype, m_product, m_storageonhand |  |
| [BOMQTYORDERED](../logic/bomqtyordered.md) | plsql | live | statements | c_uom, m_locator, m_product, m_storagereservation |  |
| [BomqtyorderedASI](../logic/bomqtyorderedasi.md) | plsql | file | statements | c_uom, m_locator, m_product, m_storage |  |
| [BOMQTYRESERVED](../logic/bomqtyreserved.md) | plsql | live | statements | c_uom, m_locator, m_product, m_storagereservation |  |
| [BomqtyreservedASI](../logic/bomqtyreservedasi.md) | plsql | file | statements | c_uom, m_locator, m_product, m_storage |  |
| [bpartnerRemitLocation](../logic/bpartnerremitlocation.md) | plsql | live | statements | c_bpartner_location |  |
| [charAt](../logic/charat.md) | plsql | live | statements |  |  |
| [Cleanup](../logic/cleanup.md) | plsql | file | statements |  | ad_find, ad_pinstance |
| [currencyBase](../logic/currencybase.md) | plsql | live | statements | ad_clientinfo, c_acctschema |  |
| [currencyConvert](../logic/currencyconvert.md) | plsql | live | statements |  |  |
| [currencyConvertInvoice](../logic/currencyconvertinvoice.md) | plsql | live | statements | ad_clientinfo, c_acctschema, c_invoice |  |
| [currencyConvertPayment](../logic/currencyconvertpayment.md) | plsql | live | statements | ad_clientinfo, c_acctschema, c_payment_v |  |
| [currencyRate](../logic/currencyrate.md) | plsql | live | statements | c_conversiontype, c_currency |  |
| [currencyRound](../logic/currencyround.md) | plsql | live | statements | c_currency |  |
| [C_AcctSchema_Default_Copy](../logic/c_acctschema_default_copy.md) | plsql | live | statements | c_bankaccount, c_bankaccount_acct, c_bp_employee_acct, c_bp_group, c_bp_group_acct, c_bpartner, c_cashbook, c_cashbook_acct, c_charge, c_charge_acct, c_project, c_project_acct, c_tax, c_tax_acct, c_withholding, c_withholding_acct, m_product_category, m_product_category_acct, m_warehouse, m_warehouse_acct | ad_pinstance, c_bankaccount_acct, c_bp_employee_acct, c_bp_group_acct, c_cashbook_acct, c_charge_acct, c_project_acct, c_tax_acct, c_withholding_acct, m_product_category_acct, m_warehouse_acct |
| [C_BP_Group_Acct_Copy](../logic/c_bp_group_acct_copy.md) | plsql | live | statements | c_bp_customer_acct, c_bp_vendor_acct, c_bpartner | ad_pinstance, c_bp_customer_acct, c_bp_vendor_acct |
| [C_ORDER_DRILLDOWN](../logic/c_order_drilldown.md) | plsql | live | statements |  | ad_pinstance, t_spool |
| [daysBetween](../logic/daysbetween.md) | plsql | live | statements |  |  |
| [DBA_AfterImport](../logic/dba_afterimport.md) | plsql | live | statements | user_tables |  |
| [DBA_Cleanup](../logic/dba_cleanup.md) | plsql | live | statements | ad_table, user_tab_cols, user_tables |  |
| [DBA_ConstraintCmd](../logic/dba_constraintcmd.md) | plsql | live | statements | user_cons_columns, user_constraints |  |
| [DBA_DisplayType](../logic/dba_displaytype.md) | plsql | live | statements |  |  |
| [DBA_Recompile](../logic/dba_recompile.md) | plsql | live | statements | user_objects | ad_pinstance |
| [delete_ad_archive_binary](../logic/delete_ad_archive_binary.md) | plpgsql | file | statements |  |  |
| [delete_ad_attachment_binary](../logic/delete_ad_attachment_binary.md) | plpgsql | file | statements |  |  |
| [delete_ad_image_binary](../logic/delete_ad_image_binary.md) | plpgsql | file | statements |  |  |
| [documentNo](../logic/documentno.md) | plsql | live | statements | c_order, dd_order, m_forecast, m_requisition, pp_mrp, pp_order |  |
| [Fact_Acct_Balance_Update](../logic/fact_acct_balance_update.md) | plsql | live | statements | fact_acct | fact_acct_balance |
| [firstOf](../logic/firstof.md) | plsql | live | statements |  |  |
| [forbid_multiple_rows_in_dbreplicasyncverifier](../logic/forbid_multiple_rows_in_dbreplicasyncverifier.md) | plpgsql | file | statements | dbreplicasyncverifier |  |
| [generate_insert_as](../logic/generate_insert_as.md) | plsql | file | statements | all_objects, all_tab_columns |  |
| [generate_uuid](../logic/generate_uuid.md) | plsql | live | statements |  |  |
| [get1099bucket](../logic/get1099bucket.md) | plsql | live | statements | c_1099box, c_doctype, c_invoice, c_invoiceline |  |
| [getdate](../logic/getdate.md) | plsql | live | statements |  |  |
| [get_Sysconfig](../logic/get_sysconfig.md) | plsql | live | statements | ad_sysconfig |  |
| [instr](../logic/instr.md) | plpgsql | file | statements |  |  |
| [invoiceDiscount](../logic/invoicediscount.md) | plsql | live | statements | ad_clientinfo, c_invoice, c_invoicepayschedule |  |
| [invoiceOpen](../logic/invoiceopen.md) | plsql | live | statements | c_currency, c_invoice_v, c_invoicepayschedule, dual |  |
| [InvoiceopenToDate](../logic/invoiceopentodate.md) | plsql | live | statements | c_currency, c_invoice_v, c_invoicepayschedule, dual |  |
| [invoicePaid](../logic/invoicepaid.md) | plsql | live | statements | c_currency, dual |  |
| [InvoicepaidToDate](../logic/invoicepaidtodate.md) | plsql | live | statements | c_currency, dual |  |
| [invoiceWriteOff](../logic/invoicewriteoff.md) | plsql | live | statements | c_invoice |  |
| [isIntersectCSV](../logic/isintersectcsv.md) | plsql | live | statements |  |  |
| [IsMemberOfAcctSchema](../logic/ismemberofacctschema.md) | plsql | live | statements | ad_org, ad_tree, ad_treenode, c_acctschema |  |
| [migr_fix_payment_cashline](../logic/migr_fix_payment_cashline.md) | plpgsql | file | statements | c_cash, c_cashline, c_payment | c_cashline |
| [M_PriceList_Create](../logic/m_pricelist_create.md) | plsql | file | statements | c_currency, m_pricelist, m_pricelist_version, m_product, m_product_po, m_productprice, t_selection | ad_pinstance, ad_pinstance_log, m_product_po, m_productprice, t_selection |
| [M_Product_BOM_Check](../logic/m_product_bom_check.md) | plsql | file | partial | m_product, m_product_bom, t_selection, t_selection2 | ad_pinstance, m_product, t_selection, t_selection2 |
| [M_Product_Category_Acct_Copy](../logic/m_product_category_acct_copy.md) | plsql | live | statements | m_product, m_product_acct | ad_pinstance, m_product_acct |
| [M_Product_Delete](../logic/m_product_delete.md) | plsql | live | statements | m_product |  |
| [nextBusinessDay](../logic/nextbusinessday.md) | plsql | live | statements | ad_client, ad_language, c_country, dual |  |
| [nextID](../logic/nextid.md) | plsql | live | statements | ad_sequence | ad_sequence |
| [NextIDByYear](../logic/nextidbyyear.md) | plsql | file | statements | ad_sequence_no | ad_sequence_no |
| [nextidfunc](../logic/nextidfunc.md) | plsql | live | statements |  |  |
| [nvl](../logic/nvl.md) | plpgsql | file | statements |  |  |
| [paymentAllocated](../logic/paymentallocated.md) | plsql | live | statements | c_currency, c_payment, dual |  |
| [paymentAvailable](../logic/paymentavailable.md) | plsql | live | statements | c_currency, c_payment, c_payment_v, dual |  |
| [paymentTermDiscount](../logic/paymenttermdiscount.md) | plsql | live | statements | ad_clientinfo, c_acctschema, c_currency, c_paymentterm, dual |  |
| [paymentTermDueDate](../logic/paymenttermduedate.md) | plsql | live | statements |  |  |
| [paymentTermDueDays](../logic/paymenttermduedays.md) | plsql | live | statements |  |  |
| [prodqtyordered](../logic/prodqtyordered.md) | plsql | live | statements | c_uom, m_locator, m_product, m_productionline |  |
| [prodqtyreserved](../logic/prodqtyreserved.md) | plsql | live | statements | c_uom, m_locator, m_product, m_productionline |  |
| [productAttribute](../logic/productattribute.md) | plsql | live | statements | m_attributeset, m_attributesetinstance |  |
| [register_migration_script](../logic/register_migration_script.md) | plsql | live | statements | ad_migrationscript, ad_system | ad_migrationscript, ad_system |
| [role_access_update](../logic/role_access_update.md) | plpgsql | file | statements | ad_role | ad_document_action_access, ad_form_access, ad_infowindow_access, ad_process_access, ad_window_access, ad_workflow_access |
| [round](../logic/round.md) | plpgsql | file | statements |  |  |
| [subtractdays](../logic/subtractdays.md) | plpgsql | file | statements |  |  |
| [torecordid](../logic/torecordid.md) | plsql | live | statements | ad_column, ad_table |  |
| [toTableOfVarchar2](../logic/totableofvarchar2.md) | plsql | live | statements |  |  |
| [trunc](../logic/trunc.md) | plpgsql | file | statements |  |  |
| [update_sequences](../logic/update_sequences.md) | plpgsql | file | statements | ad_column, ad_table |  |
