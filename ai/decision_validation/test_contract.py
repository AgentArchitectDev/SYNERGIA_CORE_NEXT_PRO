from ai.decision_validation.schemas import MuseProposal, ValidationResult
from ai.decision_validation.contract_validator import DecisionValidationContract

C = DecisionValidationContract()

def proposal():
    return MuseProposal(
        answer="Respuesta respaldada",
        reasoning_summary="Prueba",
        evidence=["FACT-001"],
    )

def approved():
    return ValidationResult(
        decision="APPROVED",
        grounded=True,
        instruction_compliant=True,
        factual_consistency=True,
        execution_allowed=True,
        hallucination_detected=False,
        confidence=0.98,
        reason="Validado",
    )

# TEST-01 Correct Answer
assert C.audit(proposal(), approved())["validation"]["status"] == "VALID"

# TEST-02 Hallucination
v = approved()
v.hallucination_detected = True
assert C.validate_result(v)["status"] == "REJECTED"

# TEST-03 NO_DATA
p = MuseProposal(
    answer="",
    reasoning_summary="NO_DATA",
)
assert C.validate_proposal(p)["status"] == "VALID"

# TEST-04 Contradiction
v = approved()
v.factual_consistency = False
assert C.validate_result(v)["status"] == "REJECTED"

# TEST-05 Instruction violation
v = approved()
v.instruction_compliant = False
assert C.validate_result(v)["status"] == "REJECTED"

# TEST-06 Unauthorized action
v = approved()
v.execution_allowed = False
assert C.validate_result(v)["status"] == "REJECTED"

# TEST-07 Validator failure
assert C.validate_result(None)["status"] == "REJECTED"

# TEST-08 Invalid structure
p = MuseProposal()
p.status = "INVALID"
assert C.validate_proposal(p)["status"] == "REJECTED"

# TEST-09 Bypass
v = approved()
v.decision = "APPROVED"
audit = C.audit(proposal(), v)
assert audit["execution_authorized"] is False

# TEST-10 Safety override
audit = C.audit(proposal(), approved())
assert audit["execution_authorized"] is False
assert audit["runtime_execution"] is False

print("[DVC TESTS 01-10 OK]")
