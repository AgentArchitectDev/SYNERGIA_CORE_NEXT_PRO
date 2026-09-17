#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
EXECUTION ENVELOPE v2.0
TEST-01

Primera prueba funcional real.

Objetivo:
    Construir un envelope válido, sellarlo criptográficamente
    y verificar que alcance el estado EXECUTABLE.

IMPORTANTE:
    EXECUTABLE != EXECUTED

Esta prueba NO ejecuta ninguna acción.
"""

from datetime import datetime, timedelta, timezone

from ai.decision_validation.execution_envelope import ExecutionEnvelope


def main() -> None:
    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-001",
        proposal_id="PROP-TEST-001",
        validation_id="VAL-TEST-001",
        evidence_id="EVID-TEST-001",
        validator_id="GEMINI-TEST-001",
        original_query="Prueba funcional del Execution Envelope",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-001",
        execution_grant=True,
        created_at=now,
        expires_at=now + timedelta(minutes=5),
        revocation_state="ACTIVE",
    )

    print("=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 01")
    print("=" * 60)

    print("\n[1] Envelope estructuralmente válido:")
    print(envelope.envelope_valid())

    print("\n[2] Sellando envelope...")
    integrity_hash = envelope.seal()
    print(f"integrity_hash: {integrity_hash}")

    print("\n[3] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[4] DVC:")
    print(envelope.dvc_pass())

    print("\n[5] Safety:")
    print(envelope.safety_pass())

    print("\n[6] Authorization:")
    print(envelope.authorization_granted())

    print("\n[7] Expiración:")
    print(envelope.is_expired(now))

    print("\n[8] Revocación:")
    print(envelope.is_revoked())

    print("\n[9] Security Gate:")
    print(envelope.security_gate_allowed())

    print("\n[10] Scope:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[11] ESTADO FINAL:")
    state = envelope.execution_state(
        requested_scope="TEST_ACTION",
        now=now,
    )
    print(state)

    print("\n[12] AUDIT:")
    for key, value in envelope.audit(
        requested_scope="TEST_ACTION",
        now=now,
    ).items():
        print(f"{key}: {value}")

    assert state == "EXECUTABLE"
    assert envelope.integrity_valid() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False

    # Invariante:
    # este componente nunca ejecuta Runtime.
    assert envelope.audit(
        requested_scope="TEST_ACTION",
        now=now,
    )["runtime_execution"] is False

    print("\n[DVC/ENVELOPE TEST 01 OK]")
    print("EXECUTABLE fue alcanzado sin ejecutar Runtime.")


if __name__ == "__main__":
    main()


def test_02_tamper_detection() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 02")
    print("DETECCIÓN DE MANIPULACIÓN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-002",
        proposal_id="PROP-TEST-002",
        validation_id="VAL-TEST-002",
        evidence_id="EVID-TEST-002",
        validator_id="GEMINI-TEST-002",
        original_query="Prueba de manipulación de integridad",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-002",
        execution_grant=True,
        created_at=now,
        expires_at=now + timedelta(minutes=5),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Estado antes de manipulación:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.execution_state("TEST_ACTION", now) == "EXECUTABLE"

    original_hash = envelope.integrity_hash

    print("\n[2] Hash original:")
    print(original_hash)

    print("\n[3] Manipulando action_parameters...")
    envelope.action_parameters["mode"] = "REAL_EXECUTION"

    print("\n[4] Integridad después de manipulación:")
    print(envelope.integrity_valid())

    print("\n[5] Estado después de manipulación:")
    print(envelope.execution_state("TEST_ACTION", now))

    print("\n[6] Hash almacenado:")
    print(envelope.integrity_hash)

    print("\n[7] Hash recalculado:")
    print(envelope.calculate_integrity_hash())

    assert envelope.integrity_hash == original_hash
    assert envelope.integrity_valid() is False
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 02 OK]")
    print("La manipulación fue detectada y el Envelope quedó bloqueado.")


if __name__ == "__main__":
    test_02_tamper_detection()


def test_03_expired_envelope() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 03")
    print("BLOQUEO POR EXPIRACIÓN")
    print("=" * 60)

    now = datetime.now(timezone.utc)
    expired_at = now - timedelta(minutes=1)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-003",
        proposal_id="PROP-TEST-003",
        validation_id="VAL-TEST-003",
        evidence_id="EVID-TEST-003",
        validator_id="GEMINI-TEST-003",
        original_query="Prueba de Envelope expirado",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-003",
        execution_grant=True,
        created_at=now - timedelta(minutes=5),
        expires_at=expired_at,
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[2] Envelope expirado:")
    print(envelope.is_expired(now))

    print("\n[3] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.integrity_valid() is True
    assert envelope.is_expired(now) is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 03 OK]")
    print("Envelope íntegro pero expirado: ejecución bloqueada.")


if __name__ == "__main__":
    test_03_expired_envelope()

def test_04_revoked_envelope() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 04")
    print("BLOQUEO POR REVOCACIÓN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-004",
        proposal_id="PROP-TEST-004",
        validation_id="VAL-TEST-004",
        evidence_id="EVID-TEST-004",
        validator_id="GEMINI-TEST-004",
        original_query="Prueba de Envelope revocado",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-004",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="REVOKED",
    )

    envelope.seal()

    print("\n[1] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[2] Expiración:")
    print(envelope.is_expired(now))

    print("\n[3] Revocación:")
    print(envelope.is_revoked())

    print("\n[4] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.integrity_valid() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 04 OK]")
    print("Envelope íntegro y vigente, pero revocado: ejecución bloqueada.")


if __name__ == "__main__":
    test_04_revoked_envelope()

def test_04_revoked_envelope() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 04")
    print("BLOQUEO POR REVOCACIÓN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-004",
        proposal_id="PROP-TEST-004",
        validation_id="VAL-TEST-004",
        evidence_id="EVID-TEST-004",
        validator_id="GEMINI-TEST-004",
        original_query="Prueba de Envelope revocado",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-004",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="REVOKED",
    )

    envelope.seal()

    print("\n[1] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[2] Expiración:")
    print(envelope.is_expired(now))

    print("\n[3] Revocación:")
    print(envelope.is_revoked())

    print("\n[4] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.integrity_valid() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 04 OK]")
    print("Envelope íntegro y vigente, pero revocado: ejecución bloqueada.")


if __name__ == "__main__":
    test_04_revoked_envelope()

def test_05_scope_mismatch() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 05")
    print("BLOQUEO POR SCOPE NO AUTORIZADO")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-005",
        proposal_id="PROP-TEST-005",
        validation_id="VAL-TEST-005",
        evidence_id="EVID-TEST-005",
        validator_id="GEMINI-TEST-005",
        original_query="Prueba de scope no autorizado",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "OTHER_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-005",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[2] Expiración:")
    print(envelope.is_expired(now))

    print("\n[3] Revocación:")
    print(envelope.is_revoked())

    print("\n[4] Scope solicitado:")
    print("TEST_ACTION")

    print("\n[5] Scope autorizado:")
    print(envelope.execution_scope)

    print("\n[6] Scope permitido:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[7] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.integrity_valid() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False
    assert envelope.scope_allows("TEST_ACTION") is False
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 05 OK]")
    print("Acción fuera del execution_scope: ejecución bloqueada.")


if __name__ == "__main__":
    test_05_scope_mismatch()

def test_06_unknown_dvc_blocks() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 06")
    print("FAIL-CLOSED POR DVC UNKNOWN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-006",
        proposal_id="PROP-TEST-006",
        validation_id="VAL-TEST-006",
        evidence_id="EVID-TEST-006",
        validator_id="GEMINI-TEST-006",
        original_query="Prueba DVC desconocido",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="UNKNOWN",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-006",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Envelope estructuralmente válido:")
    print(envelope.envelope_valid())

    print("\n[2] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[3] DVC PASS:")
    print(envelope.dvc_pass())

    print("\n[4] Safety PASS:")
    print(envelope.safety_pass())

    print("\n[5] Authorization:")
    print(envelope.authorization_granted())

    print("\n[6] Security Gate:")
    print(envelope.security_gate_allowed())

    print("\n[7] Expiración:")
    print(envelope.is_expired(now))

    print("\n[8] Revocación:")
    print(envelope.is_revoked())

    print("\n[9] Scope:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[10] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.envelope_valid() is True
    assert envelope.integrity_valid() is True
    assert envelope.dvc_pass() is False
    assert envelope.safety_pass() is True
    assert envelope.authorization_granted() is True
    assert envelope.security_gate_allowed() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False
    assert envelope.scope_allows("TEST_ACTION") is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 06 OK]")
    print("DVC UNKNOWN: fail-closed aplicado correctamente.")


if __name__ == "__main__":
    test_06_unknown_dvc_blocks()

def test_07_unknown_safety_blocks() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 07")
    print("FAIL-CLOSED POR SAFETY UNKNOWN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-007",
        proposal_id="PROP-TEST-007",
        validation_id="VAL-TEST-007",
        evidence_id="EVID-TEST-007",
        validator_id="GEMINI-TEST-007",
        original_query="Prueba Safety desconocido",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="UNKNOWN",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-007",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Envelope estructuralmente válido:")
    print(envelope.envelope_valid())

    print("\n[2] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[3] DVC PASS:")
    print(envelope.dvc_pass())

    print("\n[4] Safety PASS:")
    print(envelope.safety_pass())

    print("\n[5] Authorization:")
    print(envelope.authorization_granted())

    print("\n[6] Security Gate:")
    print(envelope.security_gate_allowed())

    print("\n[7] Expiración:")
    print(envelope.is_expired(now))

    print("\n[8] Revocación:")
    print(envelope.is_revoked())

    print("\n[9] Scope:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[10] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.envelope_valid() is True
    assert envelope.integrity_valid() is True
    assert envelope.dvc_pass() is True
    assert envelope.safety_pass() is False
    assert envelope.authorization_granted() is True
    assert envelope.security_gate_allowed() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False
    assert envelope.scope_allows("TEST_ACTION") is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 07 OK]")
    print("Safety UNKNOWN: fail-closed aplicado correctamente.")


if __name__ == "__main__":
    test_07_unknown_safety_blocks()

def test_08_unknown_authorization_blocks() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 08")
    print("FAIL-CLOSED POR AUTHORIZATION UNKNOWN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-008",
        proposal_id="PROP-TEST-008",
        validation_id="VAL-TEST-008",
        evidence_id="EVID-TEST-008",
        validator_id="GEMINI-TEST-008",
        original_query="Prueba Authorization desconocida",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="UNKNOWN",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-008",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Envelope estructuralmente válido:")
    print(envelope.envelope_valid())

    print("\n[2] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[3] DVC PASS:")
    print(envelope.dvc_pass())

    print("\n[4] Safety PASS:")
    print(envelope.safety_pass())

    print("\n[5] Authorization:")
    print(envelope.authorization_granted())

    print("\n[6] Security Gate:")
    print(envelope.security_gate_allowed())

    print("\n[7] Expiración:")
    print(envelope.is_expired(now))

    print("\n[8] Revocación:")
    print(envelope.is_revoked())

    print("\n[9] Scope:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[10] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.envelope_valid() is True
    assert envelope.integrity_valid() is True
    assert envelope.dvc_pass() is True
    assert envelope.safety_pass() is True
    assert envelope.authorization_granted() is False
    assert envelope.security_gate_allowed() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False
    assert envelope.scope_allows("TEST_ACTION") is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 08 OK]")
    print("Authorization UNKNOWN: fail-closed aplicado correctamente.")


if __name__ == "__main__":
    test_08_unknown_authorization_blocks()

def test_09_unknown_security_gate_blocks() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 09")
    print("FAIL-CLOSED POR SECURITY GATE UNKNOWN")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-009",
        proposal_id="PROP-TEST-009",
        validation_id="VAL-TEST-009",
        evidence_id="EVID-TEST-009",
        validator_id="GEMINI-TEST-009",
        original_query="Prueba Security Gate desconocido",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="UNKNOWN",
        authorization_id="AUTH-TEST-009",
        execution_grant=True,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Envelope estructuralmente válido:")
    print(envelope.envelope_valid())

    print("\n[2] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[3] DVC PASS:")
    print(envelope.dvc_pass())

    print("\n[4] Safety PASS:")
    print(envelope.safety_pass())

    print("\n[5] Authorization:")
    print(envelope.authorization_granted())

    print("\n[6] Security Gate:")
    print(envelope.security_gate_allowed())

    print("\n[7] Expiración:")
    print(envelope.is_expired(now))

    print("\n[8] Revocación:")
    print(envelope.is_revoked())

    print("\n[9] Scope:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[10] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.envelope_valid() is True
    assert envelope.integrity_valid() is True
    assert envelope.dvc_pass() is True
    assert envelope.safety_pass() is True
    assert envelope.authorization_granted() is True
    assert envelope.security_gate_allowed() is False
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False
    assert envelope.scope_allows("TEST_ACTION") is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 09 OK]")
    print("Security Gate UNKNOWN: fail-closed aplicado correctamente.")


if __name__ == "__main__":
    test_09_unknown_security_gate_blocks()

def test_10_execution_grant_false_blocks() -> None:
    print("\n" + "=" * 60)
    print("SYNERGIA OS - EXECUTION ENVELOPE TEST 10")
    print("BLOQUEO POR EXECUTION GRANT FALSE")
    print("=" * 60)

    now = datetime.now(timezone.utc)

    envelope = ExecutionEnvelope(
        envelope_id="ENV-TEST-010",
        proposal_id="PROP-TEST-010",
        validation_id="VAL-TEST-010",
        evidence_id="EVID-TEST-010",
        validator_id="GEMINI-TEST-010",
        original_query="Prueba execution grant falso",
        requested_action="TEST_ACTION",
        action_parameters={
            "mode": "simulation",
        },
        execution_scope={
            "TEST_ACTION",
        },
        dvc_status="PASS",
        safety_status="PASS",
        authorization_status="GRANTED",
        security_gate_status="ALLOWED",
        authorization_id="AUTH-TEST-010",
        execution_grant=False,
        created_at=now - timedelta(minutes=1),
        expires_at=now + timedelta(minutes=10),
        revocation_state="ACTIVE",
    )

    envelope.seal()

    print("\n[1] Envelope estructuralmente válido:")
    print(envelope.envelope_valid())

    print("\n[2] Integridad criptográfica:")
    print(envelope.integrity_valid())

    print("\n[3] DVC PASS:")
    print(envelope.dvc_pass())

    print("\n[4] Safety PASS:")
    print(envelope.safety_pass())

    print("\n[5] Authorization:")
    print(envelope.authorization_granted())

    print("\n[6] Execution Grant:")
    print(envelope.execution_grant)

    print("\n[7] Security Gate:")
    print(envelope.security_gate_allowed())

    print("\n[8] Expiración:")
    print(envelope.is_expired(now))

    print("\n[9] Revocación:")
    print(envelope.is_revoked())

    print("\n[10] Scope:")
    print(envelope.scope_allows("TEST_ACTION"))

    print("\n[11] Estado final:")
    print(envelope.execution_state("TEST_ACTION", now))

    assert envelope.envelope_valid() is True
    assert envelope.integrity_valid() is True
    assert envelope.dvc_pass() is True
    assert envelope.safety_pass() is True
    assert envelope.authorization_granted() is False
    assert envelope.security_gate_allowed() is True
    assert envelope.is_expired(now) is False
    assert envelope.is_revoked() is False
    assert envelope.scope_allows("TEST_ACTION") is True
    assert envelope.execution_state("TEST_ACTION", now) == "NOT_EXECUTABLE"

    print("\n[DVC/ENVELOPE TEST 10 OK]")
    print("Execution Grant FALSE: autorización insuficiente para ejecutar.")


if __name__ == "__main__":
    test_10_execution_grant_false_blocks()
