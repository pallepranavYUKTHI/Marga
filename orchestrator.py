from ai_reasoner import AIReasoner
from workflow_engine import WorkflowEngine


class WorkflowOrchestrator:
    """
    Central orchestrator for Mārga.

    Receives a citizen request and generates
    an optimized government workflow.
    """

    def __init__(self):
        self.reasoner = AIReasoner()
        self.workflow = WorkflowEngine()

    def process_request(self, request: dict):
        """
        Main orchestration pipeline.
        """

        goal = request.get("goal", "")
        state = request.get("state", "Kerala")
        business_type = request.get("business_type", "")

        analysis = self.reasoner.analyze(
            goal=goal,
            state=state,
            business_type=business_type,
        )

        workflow = self.workflow.generate_workflow(
            analysis
        )

        return {
            "success": True,
            "goal": goal,
            "business": business_type,
            "analysis": analysis,
            "workflow": workflow,
        }