import pypandoc, os, textwrap

content = """# SYNERGIA_CORE_NEXT_PRO
## CHECKPOINT STAGE 6.3.15.7.10.5
## Adaptive Router Compatibility Layer

Fecha: 2026-08-07

## Punto de retorno

Retomar:
`SYNERGIA_CORE_NEXT_PRO — STAGE 6.3.15.7.10.5 Adaptive Router Compatibility Layer`

## Estado anterior completado

STAGE 6.3.15.7.10.4
AUTONOMOUS LEARNING OPTIMIZER — COMPLETADO

Validaciones realizadas:

- Runtime Memory conectado
- Self Learning Loop activo
- Self Learning History activo
- Self Learning Feedback Engine activo
- Autonomous Learning Optimizer funcionando
- Success rate: 100%
- Strategy: KEEP_CURRENT_MODEL_STRATEGY
- Confidence: 1.0

## Problema actual detectado

Error:

`AdaptiveModelRouter.select_model() takes 2 positional arguments but 3 were given`

## Diagnóstico

Existe una diferencia de interfaz entre:

AdaptiveModelRouter

y

Business Generator + Task Engine

El flujo actual:

AdaptiveModelRouter
↓
Business Generator
↓
TaskEngine
↓
Runtime Memory
↓
Learning Loop

El Business Generator está enviando:

`select_model(task, requested_model)`

pero el Router actual espera:

`select_model(task)`

## Próxima acción

Implementar capa de compatibilidad:

Modificar:

`ai/business/adaptive_model_router.py`

para aceptar:

```python
def select_model(self, task, requested_model=None):

Mantener:

selección autónoma por aprendizaje
compatibilidad con modelos solicitados
integración con Runtime Memory
trazabilidad de decisiones
Próxima validación

Ejecutar:

PYTHONPATH=. python -c "from ai.business.adaptive_model_router import adaptive_model_router; print(adaptive_model_router.select_model('WEBSITE','llama3.2:3b'))"

Luego:

PYTHONPATH=. python tests/test_business_generator.py

Objetivo:

BUSINESS VALIDATION

STATUS: VALID

SCORE: 100%

APPROVED: 4/4

Checkpoint preparado para continuidad del proyecto SYNERGIA_CORE_NEXT_PRO.
"""

path = "/mnt/data/CHECKPOINT_STAGE_6_3_15_7_10_5_ADAPTIVE_ROUTER_COMPATIBILITY_LAYER.md"

pypandoc.convert_text(
content,
'md',
format='md',
outputfile=path,
extra_args=['--standalone']
)

path
