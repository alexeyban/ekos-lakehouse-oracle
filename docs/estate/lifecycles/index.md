---
title: "Document lifecycles"
order: 4
ekos_generated: true
ekos_estate_version: 1
---

# Document lifecycles

26 document type(s) whose business class implements iDempiere's `DocAction` interface, with the line where each action's method starts — the place to read what that action does for this document. Which statuses an action sets is not recovered yet.

| table | class | Prepare | Approve | Reject | Complete | Void | Close | Reverse – correct | Reverse – accrual | Re-activate | Invalidate | Unlock |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [A_ASSET_ADDITION](../data-model/a/a_asset_addition.md) | `org.compiere.model.MAssetAddition` | ✓ 558 | ✓ 642 | ✓ 650 | ✓ 658 | ✓ 802 | ✓ 913 | ✓ 921 | ✓ 927 | ✓ 933 | ✓ 551 | ✓ 544 |
| [A_ASSET_DISPOSED](../data-model/a/a_asset_disposed.md) | `org.compiere.model.MAssetDisposed` | ✓ 180 | ✓ 217 | ✓ 225 | ✓ 233 | ✓ 319 | ✓ 325 | ✓ 332 | ✓ 338 | ✓ 344 | ✓ 174 | ✓ 167 |
| [A_ASSET_REVAL](../data-model/a/a_asset_reval.md) | `org.compiere.model.MAssetReval` | ✓ 105 | ✓ 93 | ✓ 274 | ✓ 174 | ✓ 298 | ✓ 99 | ✓ 286 | ✓ 280 | ✓ 268 | ✓ 254 | ✓ 292 |
| [A_ASSET_TRANSFER](../data-model/a/a_asset_transfer.md) | `org.compiere.model.MAssetTransfer` | ✓ 161 | ✓ 107 | ✓ 275 | ✓ 221 | ✓ 295 | ✓ 112 | ✓ 285 | ✓ 280 | ✓ 270 | ✓ 156 | ✓ 290 |
| [A_DEPRECIATION_ENTRY](../data-model/a/a_depreciation_entry.md) | `org.compiere.model.MDepreciationEntry` | ✓ 250 | ✓ 274 | ✓ 282 | ✓ 290 | ✓ 355 | ✓ 361 | ✓ 368 | ✓ 374 | ✓ 380 | ✓ 244 | ✓ 237 |
| [C_ALLOCATIONHDR](../data-model/c/c_allocationhdr.md) | `org.compiere.model.MAllocationHdr` | ✓ 411 | ✓ 493 | ✓ 505 | ✓ 517 | ✓ 566 | ✓ 646 | ✓ 669 | ✓ 693 | ✓ 717 | ✓ 399 | ✓ 387 |
| [C_BANKSTATEMENT](../data-model/c/c_bankstatement.md) | `org.compiere.model.MBankStatement` | ✓ 321 | ✓ 370 | ✓ 382 | ✓ 394 | ✓ 505 | ✓ 606 | ✓ 628 | ✓ 649 | ✓ 670 | ✓ 309 | ✓ 297 |
| [C_BANKTRANSFER](../data-model/c/c_banktransfer.md) | `org.compiere.model.MBankTransfer` | ✓ 202 | ✓ 217 | ✓ 223 | ✓ 229 | ✓ 322 | ✓ 348 | ✓ 363 | ✓ 386 | ✓ 409 | ✓ 196 | ✓ 189 |
| [C_CASH](../data-model/c/c_cash.md) | `org.compiere.model.MCash` | ✓ 379 | ✓ 438 | ✓ 450 | ✓ 462 | ✓ 593 | ✓ 704 | ✓ 726 | ✓ 752 | ✓ 773 | ✓ 368 | ✓ 356 |
| [C_DEPOSITBATCH](../data-model/c/c_depositbatch.md) | `org.compiere.model.MDepositBatch` | ✓ 427 | ✓ 466 | ✓ 472 | ✓ 478 | ✓ 201 | ✓ 533 | ✓ 551 | ✓ 557 | ✓ 563 | ✓ 187 | ✓ 175 |
| [C_INVOICE](../data-model/c/c_invoice.md) | `org.compiere.model.MInvoice` | ✓ 1698 | ✓ 1923 | ✓ 1935 | ✓ 1947 | ✓ 2462 | ✓ 2558 | ✓ 2581 | ✓ 2821 | ✓ 2848 | ✓ 1686 | ✓ 1674 |
| [C_ORDER](../data-model/c/c_order.md) | `org.compiere.model.MOrder` | ✓ 1537 | ✓ 2107 | ✓ 2119 | ✓ 2131 | ✓ 2703 | ✓ 2904 | ✓ 3027 | ✓ 3047 | ✓ 3067 | ✓ 1525 | ✓ 1513 |
| [C_PAYMENT](../data-model/c/c_payment.md) | `org.compiere.model.MPayment` | ✓ 1923 | ✓ 2032 | ✓ 2044 | ✓ 2056 | ✓ 2593 | ✓ 2675 | ✓ 2697 | ✓ 2883 | ✓ 2919 | ✓ 1911 | ✓ 1899 |
| [C_PROJECTISSUE](../data-model/c/c_projectissue.md) | `org.compiere.model.MProjectIssue` | ✓ 376 | ✓ 381 | ✓ 386 | ✓ 391 | ✓ 396 | ✓ 401 | ✓ 406 | ✓ 411 | ✓ 419 | ✓ 371 | ✓ 366 |
| [DD_ORDER](../data-model/dd/dd_order.md) | `org.eevolution.model.MDDOrder` | ✓ 786 | ✓ 940 | ✓ 951 | ✓ 963 | ✓ 1016 | ✓ 1138 | ✓ 1176 | ✓ 1196 | ✓ 1216 | ✓ 774 | ✓ 763 |
| [GL_JOURNAL](../data-model/gl/gl_journal.md) | `org.compiere.model.MJournal` | ✓ 462 | ✓ 615 | ✓ 627 | ✓ 639 | ✓ 703 | ✓ 749 | ✓ 781 | ✓ 857 | ✓ 931 | ✓ 451 | ✓ 439 |
| [GL_JOURNALBATCH](../data-model/gl/gl_journalbatch.md) | `org.compiere.model.MJournalBatch` | ✓ 312 | ✓ 415 | ✓ 427 | ✓ 439 | ✓ 539 | ✓ 559 | ✓ 616 | ✓ 702 | ✓ 787 | ✓ 301 | ✓ 289 |
| [M_INOUT](../data-model/m/m_inout.md) | `org.compiere.model.MInOut` | ✓ 1421 | ✓ 1590 | ✓ 1602 | ✓ 1614 | ✓ 2586 | ✓ 2672 | ✓ 2695 | ✓ 2922 | ✓ 2951 | ✓ 1409 | ✓ 1397 |
| [M_INOUTCONFIRM](../data-model/m/m_inoutconfirm.md) | `org.compiere.model.MInOutConfirm` | ✓ 329 | ✓ 369 | ✓ 381 | ✓ 393 | ✓ 691 | ✓ 752 | ✓ 775 | ✓ 796 | ✓ 817 | ✓ 317 | ✓ 305 |
| [M_INVENTORY](../data-model/m/m_inventory.md) | `org.compiere.model.MInventory` | ✓ 389 | ✓ 456 | ✓ 468 | ✓ 480 | ✓ 944 | ✓ 1027 | ✓ 1048 | ✓ 1172 | ✓ 1199 | ✓ 377 | ✓ 365 |
| [M_MOVEMENT](../data-model/m/m_movement.md) | `org.compiere.model.MMovement` | ✓ 289 | ✓ 384 | ✓ 396 | ✓ 408 | ✓ 851 | ✓ 930 | ✓ 953 | ✓ 1089 | ✓ 1116 | ✓ 277 | ✓ 265 |
| [M_MOVEMENTCONFIRM](../data-model/m/m_movementconfirm.md) | `org.compiere.model.MMovementConfirm` | ✓ 312 | ✓ 362 | ✓ 374 | ✓ 386 | ✓ 626 | ✓ 674 | ✓ 697 | ✓ 718 | ✓ 739 | ✓ 300 | ✓ 288 |
| [M_PRODUCTION](../data-model/m/m_production.md) | `org.compiere.model.MProduction` | ✓ 594 | ✓ 726 | ✓ 731 | ✓ 152 | ✓ 736 | ✓ 816 | ✓ 834 | ✓ 998 | ✓ 1020 | ✓ 587 | ✓ 580 |
| [M_REQUISITION](../data-model/m/m_requisition.md) | `org.compiere.model.MRequisition` | ✓ 259 | ✓ 317 | ✓ 329 | ✓ 341 | ✓ 400 | ✓ 425 | ✓ 479 | ✓ 500 | ✓ 521 | ✓ 248 | ✓ 236 |
| [M_RMA](../data-model/m/m_rma.md) | `org.compiere.model.MRMA` | ✓ 346 | ✓ 416 | ✓ 428 | ✓ 440 | ✓ 680 | ✓ 748 | ✓ 768 | ✓ 789 | ✓ 810 | ✓ 335 | ✓ 323 |
| [S_TIMEEXPENSE](../data-model/s/s_timeexpense.md) | `org.compiere.model.MTimeExpense` | ✓ 313 | ✓ 368 | ✓ 380 | ✓ 392 | ✓ 432 | ✓ 458 | ✓ 479 | ✓ 501 | ✓ 523 | ✓ 301 | ✓ 289 |

The number is the method's line in the class's source file.
