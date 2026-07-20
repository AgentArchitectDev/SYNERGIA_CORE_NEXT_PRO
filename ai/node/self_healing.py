"""
===============================================================================
 SYNERGIA CORE NEXT PRO
 Self Healing Engine
-------------------------------------------------------------------------------
 File        : self_healing.py
 Layer       : NODE
 Module      : Self Healing
 Version     : ACEA Enterprise 1.0
 Author      : SYNERGIA Engineering
-------------------------------------------------------------------------------

Descripción
-----------
Motor autónomo de autorrecuperación del clúster.

Responsabilidades:

- Monitoreo continuo de nodos
- Detección de fallas
- Predicción de incidentes
- Planificación de recuperación
- Ejecución automática
- Validación
- Reintegración al clúster

===============================================================================
"""

from __future__ import annotations

import logging
import threading
import time
import uuid

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import Dict
from typing import List
from typing import Optional
from typing import Any


# =============================================================================
# LOGGER
# =============================================================================

logger = logging.getLogger("SYNERGIA.SELF_HEALING")


# =============================================================================
# ENUMS
# =============================================================================


class NodeState(Enum):
    """Estado general del nodo."""

    ONLINE = auto()
    OFFLINE = auto()
    DEGRADED = auto()
    MAINTENANCE = auto()
    RECOVERING = auto()
    FAILED = auto()


class FailureSeverity(Enum):
    """Severidad detectada."""

    INFO = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class HealingStatus(Enum):
    """Estado del proceso de reparación."""

    IDLE = auto()
    ANALYZING = auto()
    PLANNING = auto()
    EXECUTING = auto()
    VALIDATING = auto()
    COMPLETED = auto()
    FAILED = auto()


class RepairAction(Enum):
    """Acciones posibles."""

    NONE = auto()

    RESTART_SERVICE = auto()

    RESTART_RUNTIME = auto()

    RESTART_NODE = auto()

    MIGRATE_TASKS = auto()

    CLEAR_MEMORY = auto()

    RESTART_MODEL = auto()

    RESTART_API = auto()

    ISOLATE_NODE = auto()

    REINTEGRATE_NODE = auto()

    SHUTDOWN_NODE = auto()


# =============================================================================
# CONFIGURACIÓN
# =============================================================================


@dataclass
class HealingConfiguration:
    """
    Configuración del sistema.
    """

    monitor_interval: int = 5

    heartbeat_timeout: int = 20

    cpu_limit: float = 90.0

    memory_limit: float = 90.0

    disk_limit: float = 95.0

    max_retry: int = 3

    prediction_enabled: bool = True

    auto_repair: bool = True

    validation_timeout: int = 60

    history_limit: int = 10000


# =============================================================================
# SNAPSHOT
# =============================================================================


@dataclass
class NodeSnapshot:
    """
    Fotografía instantánea del nodo.
    """

    node_id: str

    hostname: str

    cpu: float

    memory: float

    disk: float

    gpu: float

    latency: float

    heartbeat: datetime

    active_agents: int

    active_models: int

    active_tasks: int

    state: NodeState

    timestamp: datetime = field(default_factory=datetime.utcnow)


# =============================================================================
# INCIDENTE
# =============================================================================


@dataclass
class NodeIncident:

    incident_id: str

    node_id: str

    severity: FailureSeverity

    description: str

    created_at: datetime = field(default_factory=datetime.utcnow)

    snapshot: Optional[NodeSnapshot] = None


# =============================================================================
# PLAN
# =============================================================================


@dataclass
class RepairPlan:

    plan_id: str

    incident_id: str

    actions: List[RepairAction]

    priority: int = 1

    automatic: bool = True


# =============================================================================
# RESULTADO
# =============================================================================


@dataclass
class RepairResult:

    success: bool

    message: str

    duration: float

    repaired_at: datetime = field(default_factory=datetime.utcnow)


# =============================================================================
# MÉTRICAS
# =============================================================================


@dataclass
class HealingMetrics:

    repaired_nodes: int = 0

    failed_repairs: int = 0

    restarted_services: int = 0

    restarted_models: int = 0

    migrated_tasks: int = 0

    isolated_nodes: int = 0

    recovered_nodes: int = 0


# =============================================================================
# HISTORIAL
# =============================================================================


@dataclass
class RepairHistory:

    history: List[RepairResult] = field(default_factory=list)

    def add(self, result: RepairResult):

        self.history.append(result)

    def last(self) -> Optional[RepairResult]:

        if not self.history:
            return None

        return self.history[-1]


# =============================================================================
# BASE COMPONENT
# =============================================================================


class HealingComponent:
    """
    Clase base para todos los componentes del motor.
    """

    def __init__(self, manager: "SelfHealingManager"):

        self.manager = manager

        self.logger = logger
# =============================================================================
# HEARTBEAT MONITOR
# =============================================================================


class HeartbeatMonitor(HealingComponent):
    """
    Monitorea continuamente el estado de los nodos registrados.
    Detecta pérdida de heartbeat y degradación de recursos.
    """

    def __init__(self, manager: "SelfHealingManager"):

        super().__init__(manager)

        self.running = False

        self.thread = None

    # -------------------------------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._loop,
            daemon=True,
            name="HeartbeatMonitor"
        )

        self.thread.start()

        logger.info("Heartbeat Monitor iniciado.")

    # -------------------------------------------------------------------------

    def stop(self):

        self.running = False

        logger.info("Heartbeat Monitor detenido.")

    # -------------------------------------------------------------------------

    def _loop(self):

        while self.running:

            try:

                self.scan()

            except Exception as ex:

                logger.exception(ex)

            time.sleep(
                self.manager.config.monitor_interval
            )

    # -------------------------------------------------------------------------

    def scan(self):

        snapshots = self.manager.get_node_snapshots()

        for snapshot in snapshots:

            self.evaluate(snapshot)

    # -------------------------------------------------------------------------

    def evaluate(self, snapshot: NodeSnapshot):

        now = datetime.utcnow()

        elapsed = (

            now -

            snapshot.heartbeat

        ).total_seconds()

        if elapsed > self.manager.config.heartbeat_timeout:

            incident = NodeIncident(

                incident_id=str(uuid.uuid4()),

                node_id=snapshot.node_id,

                severity=FailureSeverity.CRITICAL,

                description=(
                    f"Heartbeat perdido "
                    f"hace {elapsed:.1f} segundos."
                ),

                snapshot=snapshot

            )

            self.manager.register_incident(
                incident
            )

            return

        self.check_cpu(snapshot)

        self.check_memory(snapshot)

        self.check_disk(snapshot)

    # -------------------------------------------------------------------------

    def check_cpu(self, snapshot):

        if snapshot.cpu < self.manager.config.cpu_limit:
            return

        self.manager.register_incident(

            NodeIncident(

                incident_id=str(uuid.uuid4()),

                node_id=snapshot.node_id,

                severity=FailureSeverity.HIGH,

                description=f"CPU crítica {snapshot.cpu:.1f}%",

                snapshot=snapshot

            )

        )

    # -------------------------------------------------------------------------

    def check_memory(self, snapshot):

        if snapshot.memory < self.manager.config.memory_limit:
            return

        self.manager.register_incident(

            NodeIncident(

                incident_id=str(uuid.uuid4()),

                node_id=snapshot.node_id,

                severity=FailureSeverity.HIGH,

                description=f"RAM crítica {snapshot.memory:.1f}%",

                snapshot=snapshot

            )

        )

    # -------------------------------------------------------------------------

    def check_disk(self, snapshot):

        if snapshot.disk < self.manager.config.disk_limit:
            return

        self.manager.register_incident(

            NodeIncident(

                incident_id=str(uuid.uuid4()),

                node_id=snapshot.node_id,

                severity=FailureSeverity.MEDIUM,

                description=f"Disco crítico {snapshot.disk:.1f}%",

                snapshot=snapshot

            )

        )

    # -------------------------------------------------------------------------

    def calculate_health_score(
        self,
        snapshot: NodeSnapshot
    ) -> float:

        score = 100.0

        score -= snapshot.cpu * 0.20

        score -= snapshot.memory * 0.20

        score -= snapshot.disk * 0.10

        score -= snapshot.latency * 0.05

        delta = (
            datetime.utcnow() -
            snapshot.heartbeat
        ).total_seconds()

        if delta > self.manager.config.heartbeat_timeout:

            score -= 50

        if score < 0:
            score = 0

        return round(score, 2)

    # -------------------------------------------------------------------------

    def summary(self):

        return {

            "running": self.running,

            "heartbeat_timeout":
                self.manager.config.heartbeat_timeout,

            "monitor_interval":
                self.manager.config.monitor_interval

        }
# =============================================================================
# FAILURE ANALYZER
# =============================================================================


class FailureAnalyzer(HealingComponent):
    """
    Analiza los incidentes generados por HeartbeatMonitor y los clasifica
    para determinar la estrategia de recuperación más adecuada.
    """

    def __init__(self, manager: "SelfHealingManager"):

        super().__init__(manager)

    # ---------------------------------------------------------------------

    def analyze(self, incident: NodeIncident) -> Dict[str, Any]:

        snapshot = incident.snapshot

        analysis = {

            "incident": incident,

            "node_id": incident.node_id,

            "severity": incident.severity,

            "category": self.detect_category(incident),

            "health_score": self.calculate_health(snapshot),

            "recommendation": None,

            "risk": 0.0,

        }

        analysis["risk"] = self.calculate_risk(analysis)

        analysis["recommendation"] = self.recommend_action(
            analysis
        )

        return analysis

    # ---------------------------------------------------------------------

    def detect_category(
        self,
        incident: NodeIncident
    ) -> str:

        description = incident.description.lower()

        if "heartbeat" in description:
            return "HEARTBEAT"

        if "cpu" in description:
            return "CPU"

        if "ram" in description:
            return "MEMORY"

        if "memoria" in description:
            return "MEMORY"

        if "disk" in description:
            return "DISK"

        if "disco" in description:
            return "DISK"

        return "UNKNOWN"

    # ---------------------------------------------------------------------

    def calculate_health(
        self,
        snapshot: Optional[NodeSnapshot]
    ) -> float:

        if snapshot is None:
            return 0.0

        score = 100.0

        score -= snapshot.cpu * 0.20

        score -= snapshot.memory * 0.20

        score -= snapshot.disk * 0.10

        score -= snapshot.latency * 0.05

        return max(round(score, 2), 0.0)

    # ---------------------------------------------------------------------

    def calculate_risk(
        self,
        analysis: Dict[str, Any]
    ) -> float:

        severity = analysis["severity"]

        if severity == FailureSeverity.INFO:
            return 10

        if severity == FailureSeverity.LOW:
            return 25

        if severity == FailureSeverity.MEDIUM:
            return 50

        if severity == FailureSeverity.HIGH:
            return 75

        if severity == FailureSeverity.CRITICAL:
            return 100

        return 0

    # ---------------------------------------------------------------------

    def recommend_action(
        self,
        analysis: Dict[str, Any]
    ) -> RepairAction:

        category = analysis["category"]

        if category == "CPU":
            return RepairAction.MIGRATE_TASKS

        if category == "MEMORY":
            return RepairAction.CLEAR_MEMORY

        if category == "DISK":
            return RepairAction.RESTART_SERVICE

        if category == "HEARTBEAT":
            return RepairAction.RESTART_NODE

        return RepairAction.NONE


# =============================================================================
# PREDICTION ENGINE
# =============================================================================


class PredictionEngine(HealingComponent):
    """
    Estima la probabilidad de falla futura utilizando el estado actual del nodo.
    """

    def __init__(self, manager: "SelfHealingManager"):

        super().__init__(manager)

    # ---------------------------------------------------------------------

    def predict(
        self,
        snapshot: NodeSnapshot
    ) -> Dict[str, Any]:

        probability = self.failure_probability(snapshot)

        return {

            "node_id": snapshot.node_id,

            "hostname": snapshot.hostname,

            "probability": probability,

            "risk_level": self.risk_level(probability),

            "estimated_minutes": self.estimate_failure_time(
                probability
            ),

        }

    # ---------------------------------------------------------------------

    def failure_probability(
        self,
        snapshot: NodeSnapshot
    ) -> float:

        probability = 0.0

        probability += snapshot.cpu * 0.35

        probability += snapshot.memory * 0.30

        probability += snapshot.disk * 0.10

        probability += snapshot.latency * 0.25

        probability = probability / 100.0

        probability *= 100

        if probability > 100:
            probability = 100

        return round(probability, 2)

    # ---------------------------------------------------------------------

    def risk_level(
        self,
        probability: float
    ) -> str:

        if probability >= 90:
            return "CRITICAL"

        if probability >= 70:
            return "HIGH"

        if probability >= 50:
            return "MEDIUM"

        if probability >= 25:
            return "LOW"

        return "STABLE"

    # ---------------------------------------------------------------------

    def estimate_failure_time(
        self,
        probability: float
    ) -> Optional[int]:

        if probability >= 95:
            return 1

        if probability >= 85:
            return 5

        if probability >= 70:
            return 15

        if probability >= 50:
            return 30

        if probability >= 25:
            return 60

        return None
# =============================================================================
# RECOVERY PLANNER
# =============================================================================


class RecoveryPlanner(HealingComponent):
    """
    Genera planes de recuperación inteligentes a partir del análisis de
    incidentes y la predicción de fallos.
    """

    def __init__(self, manager: "SelfHealingManager"):

        super().__init__(manager)

    # ---------------------------------------------------------------------

    def build_plan(
        self,
        analysis: Dict[str, Any]
    ) -> RepairPlan:

        category = analysis["category"]

        severity = analysis["severity"]

        actions = self.select_actions(
            category,
            severity
        )

        priority = self.calculate_priority(
            severity
        )

        return RepairPlan(

            plan_id=str(uuid.uuid4()),

            incident_id=analysis["incident"].incident_id,

            actions=actions,

            priority=priority,

            automatic=self.manager.config.auto_repair

        )

    # ---------------------------------------------------------------------

    def select_actions(

        self,

        category: str,

        severity: FailureSeverity

    ) -> List[RepairAction]:

        actions = []

        if category == "CPU":

            actions.extend([

                RepairAction.MIGRATE_TASKS,

                RepairAction.CLEAR_MEMORY

            ])

        elif category == "MEMORY":

            actions.extend([

                RepairAction.CLEAR_MEMORY,

                RepairAction.RESTART_SERVICE

            ])

        elif category == "DISK":

            actions.extend([

                RepairAction.RESTART_SERVICE

            ])

        elif category == "HEARTBEAT":

            actions.extend([

                RepairAction.ISOLATE_NODE,

                RepairAction.RESTART_NODE,

                RepairAction.REINTEGRATE_NODE

            ])

        else:

            actions.append(
                RepairAction.RESTART_SERVICE
            )

        if severity == FailureSeverity.CRITICAL:

            if RepairAction.RESTART_RUNTIME not in actions:

                actions.append(
                    RepairAction.RESTART_RUNTIME
                )

        return actions

    # ---------------------------------------------------------------------

    def calculate_priority(

        self,

        severity: FailureSeverity

    ) -> int:

        table = {

            FailureSeverity.INFO: 5,

            FailureSeverity.LOW: 4,

            FailureSeverity.MEDIUM: 3,

            FailureSeverity.HIGH: 2,

            FailureSeverity.CRITICAL: 1,

        }

        return table.get(severity, 5)

    # ---------------------------------------------------------------------

    def explain_plan(

        self,

        plan: RepairPlan

    ) -> Dict[str, Any]:

        return {

            "plan_id": plan.plan_id,

            "incident_id": plan.incident_id,

            "priority": plan.priority,

            "automatic": plan.automatic,

            "steps": [

                action.name

                for action in plan.actions

            ]

        }

    # ---------------------------------------------------------------------

    def validate_plan(

        self,

        plan: RepairPlan

    ) -> bool:

        if not plan.actions:

            return False

        if plan.priority < 1:

            return False

        return True

    # ---------------------------------------------------------------------

    def optimize_plan(

        self,

        plan: RepairPlan

    ) -> RepairPlan:

        unique_actions = []

        seen = set()

        for action in plan.actions:

            if action not in seen:

                unique_actions.append(action)

                seen.add(action)

        plan.actions = unique_actions

        return plan

    # ---------------------------------------------------------------------

    def emergency_plan(

        self,

        incident: NodeIncident

    ) -> RepairPlan:

        return RepairPlan(

            plan_id=str(uuid.uuid4()),

            incident_id=incident.incident_id,

            actions=[

                RepairAction.ISOLATE_NODE,

                RepairAction.RESTART_NODE,

                RepairAction.REINTEGRATE_NODE

            ],

            priority=1,

            automatic=True

        )
# =============================================================================
# REPAIR EXECUTOR
# =============================================================================


class RepairExecutor(HealingComponent):
    """
    Ejecuta los planes de recuperación generados por RecoveryPlanner.

    Capa responsable de transformar decisiones cognitivas en acciones reales
    sobre nodos, servicios y runtime.
    """

    def __init__(
        self,
        manager: "SelfHealingManager"
    ):

        super().__init__(manager)


        self.execution_history = []


    # ---------------------------------------------------------------------

    async def execute(
        self,
        plan: RepairPlan
    ) -> Dict[str, Any]:

        result = {

            "plan_id": plan.plan_id,

            "incident_id": plan.incident_id,

            "started": datetime.utcnow(),

            "success": True,

            "executed_actions": [],

            "errors": []

        }


        for action in plan.actions:


            try:

                response = await self.execute_action(
                    action,
                    plan
                )


                result["executed_actions"].append(

                    {

                        "action": action.name,

                        "result": response

                    }

                )


            except Exception as error:


                result["success"] = False


                result["errors"].append(

                    {

                        "action": action.name,

                        "error": str(error)

                    }

                )


                if plan.priority == 1:

                    break



        result["finished"] = datetime.utcnow()


        self.execution_history.append(
            result
        )


        return result



    # ---------------------------------------------------------------------

    async def execute_action(

        self,

        action: RepairAction,

        plan: RepairPlan

    ) -> str:


        handlers = {


            RepairAction.CLEAR_MEMORY:

                self.clear_memory,


            RepairAction.RESTART_SERVICE:

                self.restart_service,


            RepairAction.RESTART_NODE:

                self.restart_node,


            RepairAction.ISOLATE_NODE:

                self.isolate_node,


            RepairAction.REINTEGRATE_NODE:

                self.reintegrate_node,


            RepairAction.MIGRATE_TASKS:

                self.migrate_tasks,


            RepairAction.RESTART_RUNTIME:

                self.restart_runtime,


        }


        handler = handlers.get(action)


        if handler is None:

            return "ACTION_NOT_IMPLEMENTED"


        return await handler()



    # ---------------------------------------------------------------------

    async def clear_memory(self):

        """
        Limpieza controlada de memoria del nodo.
        """

        await asyncio.sleep(0)

        return "MEMORY_CLEAN_COMPLETED"



    # ---------------------------------------------------------------------

    async def restart_service(self):

        """
        Reinicio controlado de servicios internos.
        """

        await asyncio.sleep(0)

        return "SERVICE_RESTART_COMPLETED"



    # ---------------------------------------------------------------------

    async def restart_node(self):

        """
        Reinicio lógico del nodo SYNERGIA.
        """

        await asyncio.sleep(0)

        return "NODE_RESTART_REQUESTED"



    # ---------------------------------------------------------------------

    async def isolate_node(self):

        """
        Aislamiento preventivo de nodo fallando.
        """

        await asyncio.sleep(0)

        return "NODE_ISOLATED"



    # ---------------------------------------------------------------------

    async def reintegrate_node(self):

        """
        Reincorporación del nodo al cluster.
        """

        await asyncio.sleep(0)

        return "NODE_REINTEGRATED"



    # ---------------------------------------------------------------------

    async def migrate_tasks(self):

        """
        Migración de cargas hacia otros nodos disponibles.
        """

        await asyncio.sleep(0)

        return "TASKS_MIGRATED"



    # ---------------------------------------------------------------------

    async def restart_runtime(self):

        """
        Reinicio del Runtime Manager.
        """

        await asyncio.sleep(0)

        return "RUNTIME_RESTART_REQUESTED"



    # ---------------------------------------------------------------------

    def history(self) -> List[Dict[str, Any]]:

        """
        Devuelve historial de reparaciones.
        """

        return self.execution_history



    # ---------------------------------------------------------------------

    def last_execution(self):

        if not self.execution_history:

            return None


        return self.execution_history[-1]
# =============================================================================
# VALIDATION ENGINE
# =============================================================================


class ValidationEngine(HealingComponent):
    """
    Valida si una reparación aplicada logró recuperar correctamente
    el estado saludable del nodo.
    """

    def __init__(
        self,
        manager: "SelfHealingManager"
    ):

        super().__init__(manager)


        self.validation_history = []


    # ---------------------------------------------------------------------

    async def validate(

        self,

        execution_result: Dict[str, Any],

        snapshot: Optional[NodeSnapshot]

    ) -> Dict[str, Any]:


        validation = {


            "execution_id":

                execution_result.get(
                    "plan_id"
                ),


            "timestamp":

                datetime.utcnow(),


            "healthy":

                False,


            "checks": [],


            "errors": []

        }



        try:


            health = await self.check_health(
                snapshot
            )


            validation["checks"].append(

                {

                    "name": "node_health",

                    "value": health

                }

            )



            if health >= 70:


                validation["healthy"] = True



            else:


                validation["errors"].append(

                    "Node health below threshold"

                )



        except Exception as error:


            validation["errors"].append(

                str(error)

            )



        self.validation_history.append(
            validation
        )


        return validation



    # ---------------------------------------------------------------------

    async def check_health(

        self,

        snapshot: Optional[NodeSnapshot]

    ) -> float:


        if snapshot is None:

            return 0



        score = 100



        score -= snapshot.cpu * 0.20

        score -= snapshot.memory * 0.20

        score -= snapshot.disk * 0.10


        return max(score,0)



    # ---------------------------------------------------------------------

    def history(self):

        return self.validation_history



# =============================================================================
# REINTEGRATION MANAGER
# =============================================================================


class ReintegrationManager(HealingComponent):
    """
    Controla el retorno seguro de nodos recuperados
    al SYNERGIA Cluster.
    """

    def __init__(
        self,
        manager: "SelfHealingManager"
    ):

        super().__init__(manager)


        self.reintegrated_nodes = []



    # ---------------------------------------------------------------------

    async def reintegrate(

        self,

        node_id: str,

        validation: Dict[str, Any]

    ) -> Dict[str, Any]:


        result = {


            "node_id": node_id,


            "timestamp":

                datetime.utcnow(),


            "status":

                "FAILED"


        }



        if not validation.get(
            "healthy",
            False
        ):


            result["reason"] = (

                "Validation failed"

            )


            return result



        try:


            await self.enable_node(
                node_id
            )


            self.reintegrated_nodes.append(

                node_id

            )


            result["status"] = (

                "ONLINE"

            )


        except Exception as error:


            result["error"] = str(error)



        return result



    # ---------------------------------------------------------------------

    async def enable_node(

        self,

        node_id: str

    ):


        """
        Punto de integración futura con:

        - node_manager.py
        - node_registry.py
        - cluster_manager.py
        """


        await asyncio.sleep(0)


        return True



    # ---------------------------------------------------------------------

    def is_reintegrated(

        self,

        node_id:str

    )->bool:


        return node_id in self.reintegrated_nodes
# =============================================================================
# SELF HEALING MANAGER
# =============================================================================


class SelfHealingManager:
    """
    Controlador principal del sistema Self Healing ACEA.

    Coordina detección, análisis, planificación,
    reparación, validación y reintegración.
    """


    def __init__(
        self,
        config: Optional[SelfHealingConfig] = None
    ):


        self.config = config or SelfHealingConfig()



        # Estado interno

        self.active = False


        self.incidents = []


        self.repair_reports = []



        # Componentes ACEA


        self.heartbeat_monitor = HeartbeatMonitor(
            self
        )


        self.failure_analyzer = FailureAnalyzer(
            self
        )


        self.prediction_engine = PredictionEngine(
            self
        )


        self.recovery_planner = RecoveryPlanner(
            self
        )


        self.repair_executor = RepairExecutor(
            self
        )


        self.validation_engine = ValidationEngine(
            self
        )


        self.reintegration_manager = ReintegrationManager(
            self
        )



    # -----------------------------------------------------------------

    async def start(self):

        """
        Inicia el ciclo autónomo de Self Healing.
        """


        self.active = True


        return {

            "status": "ONLINE",

            "module":

                "SELF_HEALING_ACEA"

        }



    # -----------------------------------------------------------------

    async def stop(self):

        """
        Detiene el sistema de autocuración.
        """


        self.active = False


        return {

            "status": "OFFLINE"

        }



    # -----------------------------------------------------------------

    async def process_incident(

        self,

        incident: NodeIncident

    ) -> Dict[str,Any]:


        """
        Pipeline completo ACEA.
        """


        self.incidents.append(
            incident
        )



        # 1 - Análisis cognitivo


        analysis = self.failure_analyzer.analyze(

            incident

        )



        # 2 - Predicción


        prediction = None


        if incident.snapshot:


            prediction = self.prediction_engine.predict(

                incident.snapshot

            )



        # 3 - Crear plan


        plan = self.recovery_planner.build_plan(

            analysis

        )



        plan = self.recovery_planner.optimize_plan(

            plan

        )



        # 4 - Ejecutar reparación


        execution = await self.repair_executor.execute(

            plan

        )



        # 5 - Validar


        validation = await self.validation_engine.validate(

            execution,

            incident.snapshot

        )



        # 6 - Reintegrar


        reintegration = None


        if validation["healthy"]:


            reintegration = await self.reintegration_manager.reintegrate(

                incident.node_id,

                validation

            )



        report = {


            "incident":

                incident.incident_id,


            "analysis":

                analysis,


            "prediction":

                prediction,


            "plan":

                plan,


            "execution":

                execution,


            "validation":

                validation,


            "reintegration":

                reintegration,


            "timestamp":

                datetime.utcnow()

        }



        self.repair_reports.append(

            report

        )



        return report



    # -----------------------------------------------------------------

    def status(self)->Dict[str,Any]:


        return {


            "active":

                self.active,


            "incidents":

                len(self.incidents),


            "repairs":

                len(self.repair_reports),


            "reintegrated_nodes":

                len(

                    self.reintegration_manager.reintegrated_nodes

                )

        }



    # -----------------------------------------------------------------

    def reports(self):


        return self.repair_reports



    # -----------------------------------------------------------------

    async def emergency_healing(

        self,

        incident: NodeIncident

    ):


        """
        Modo emergencia para fallas críticas.
        """


        plan = self.recovery_planner.emergency_plan(

            incident

        )


        return await self.repair_executor.execute(

            plan

        )
# =============================================================================
# OMEGA SELF HEALING INTEGRATION LAYER
# =============================================================================


class OmegaSelfHealingController:
    """
    Capa superior de integración entre Self Healing ACEA
    y el ecosistema SYNERGIA OMEGA.
    """

    def __init__(

        self,

        runtime=None,

        node_manager=None,

        cluster_manager=None

    ):


        self.runtime = runtime

        self.node_manager = node_manager

        self.cluster_manager = cluster_manager



        self.self_healing = SelfHealingManager()



        self.running = False



        self.cycles = 0



        self.events = []



    # -----------------------------------------------------------------

    async def initialize(self):

        """
        Inicialización del sistema OMEGA.
        """


        await self.self_healing.start()



        self.running = True



        return {


            "system":

                "OMEGA_SELF_HEALING_ACEA",


            "status":

                "READY"


        }



    # -----------------------------------------------------------------

    async def monitor_cycle(self):

        """
        Ciclo autónomo de supervisión.

        Este método será llamado por:

        - omega_runtime_controller
        - autonomous_repair_loop
        """


        if not self.running:

            return None



        self.cycles += 1



        health = await self.collect_health()



        self.events.append(

            {

                "cycle":

                    self.cycles,


                "health":

                    health,


                "timestamp":

                    datetime.utcnow()

            }

        )


        return health



    # -----------------------------------------------------------------

    async def collect_health(self):

        """
        Recolección unificada de estado.
        """


        result = {


            "runtime":

                "UNKNOWN",


            "nodes":

                "UNKNOWN",


            "cluster":

                "UNKNOWN"


        }



        if self.runtime:


            result["runtime"] = (

                await self.runtime.health()

                if hasattr(

                    self.runtime,

                    "health"

                )

                else "AVAILABLE"

            )



        if self.cluster_manager:


            result["cluster"] = (

                "AVAILABLE"

            )



        if self.node_manager:


            result["nodes"] = (

                "AVAILABLE"

            )



        return result



    # -----------------------------------------------------------------

    async def receive_cluster_event(

        self,

        event: Dict[str,Any]

    ):


        """
        Entrada de eventos desde Cluster Manager.
        """


        self.events.append(

            event

        )


        if event.get(

            "severity"

        ) == "CRITICAL":


            incident = NodeIncident(

                incident_id=str(uuid.uuid4()),

                node_id=event.get(

                    "node_id",

                    "unknown"

                ),

                category="CLUSTER_FAILURE",

                severity=FailureSeverity.CRITICAL,

                snapshot=None,

                timestamp=datetime.utcnow()

            )



            return await self.self_healing.emergency_healing(

                incident

            )



        return {


            "status":

                "EVENT_ACCEPTED"

        }



    # -----------------------------------------------------------------

    async def shutdown(self):

        """
        Apagado seguro.
        """


        self.running = False


        await self.self_healing.stop()



        return {


            "status":

                "STOPPED"

        }



    # -----------------------------------------------------------------

    def status(self):


        return {


            "running":

                self.running,


            "cycles":

                self.cycles,


            "events":

                len(self.events),


            "self_healing":

                self.self_healing.status()

        }
