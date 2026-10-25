---
title: "Area MFA"
order: 17
ekos_generated: true
ekos_estate_version: 1
---

# Area MFA

4 table(s), 4 in scope.

```mermaid
erDiagram
  MFA_METHOD ||--o{ MFA_REGISTRATION : ""
  MFA_METHOD ||--o{ MFA_RULE : ""
  MFA_REGISTEREDDEVICE {
  }
```

| table | class | scope | rows | description |
|---|---|---|---|---|
| [MFA_METHOD](../../data-model/mfa/mfa_method.md) | business | in | 2 |  |
| [MFA_REGISTEREDDEVICE](../../data-model/mfa/mfa_registereddevice.md) | business | in | 0 |  |
| [MFA_REGISTRATION](../../data-model/mfa/mfa_registration.md) | business | in | 0 |  |
| [MFA_RULE](../../data-model/mfa/mfa_rule.md) | business | in | 2 |  |
