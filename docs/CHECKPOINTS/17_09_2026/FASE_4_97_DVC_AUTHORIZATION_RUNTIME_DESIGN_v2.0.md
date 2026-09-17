# SYNERGIA OS — DVC → AUTHORIZATION → RUNTIME

## FASE 4.97 — CONTRACT DESIGN v2.0

Estado: DISEÑO / NO IMPLEMENTADO

### Principio

THINK ≠ VERIFY ≠ AUTHORIZE ≠ EXECUTE

### DecisionValidationEnvelope v2.0

- envelope_id
- proposal_id
- validation_id
- evidence_id
- validator_id
- requested_action
- action_parameters
- execution_scope
- dvc_status
- safety_status
- authorization_status
- created_at
- expires_at
- authorization_id
- execution_grant
- integrity_hash

### Regla de autorización

DVC_PASS AND SAFETY_PASS AND AUTHORIZATION_GRANTED AND ENVELOPE_VALID AND INTEGRITY_VALID AND NOT_EXPIRED AND SECURITY_GATE_ALLOWED

### Fail-Closed

Cualquier campo ausente, inválido, inconsistente, expirado, revocado o con integridad no verificable produce BLOCKED.

### Separación de responsabilidades

DVC valida.
Safety bloquea o permite desde seguridad.
Human Administrator autoriza.
Envelope transporta evidencia verificable del permiso.
Runtime ejecuta únicamente después de verificar todas las condiciones.

### Estado

Este documento es diseño arquitectónico. No modifica código ni runtime.
