# SYNERGIA OS — DVC → AUTHORIZATION → RUNTIME

## FASE 4.102 — CRYPTOGRAPHIC INTEGRITY CONTRACT v1.0

Estado: DISEÑO CONGELADO / NO IMPLEMENTADO

### 1. Algoritmo

SHA-256 sobre representación UTF-8 determinista del material protegido del Envelope.

### 2. Canonicalización

La representación canónica utilizará JSON de la biblioteca estándar de Python.

Parámetros normativos:
- sort_keys=True
- separators=(,, :)
- ensure_ascii=False

### 3. Material protegido

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

### 4. Regla del hash

integrity_hash = SHA256(canonical_json(protected_fields).encode(\"utf-8\")).hexdigest()

El campo integrity_hash NO forma parte del material utilizado para calcularse a sí mismo.

### 5. Verificación

El receptor debe reconstruir exactamente el material protegido, canonicalizarlo y calcular nuevamente SHA-256.

Si el hash calculado no coincide exactamente con integrity_hash, el Envelope es INVALID y la ejecución debe ser BLOCKED.

### 6. Separación de dominios

Los hashes existentes de especificaciones de seguridad e identidad de nodo no se reutilizan como integrity_hash del Envelope.

SHA-256 es reutilizado como algoritmo criptográfico, pero el dominio y material protegido del Envelope son independientes.

### 7. Fail-Closed

Ausencia, modificación, inconsistencia, corrupción o imposibilidad de verificar cualquier campo protegido produce BLOCKED.

### 8. Replay / temporalidad

created_at y expires_at forman parte del material protegido. Un Envelope expirado no puede ejecutarse aunque su integrity_hash sea válido.

La protección contra replay requerirá además una política de unicidad/revocación asociada a envelope_id y authorization_id.

### 9. Estado

Contrato criptográfico diseñado para Envelope v2.0. No modifica código ni Runtime.
