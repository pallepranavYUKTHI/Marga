"""
workflow_engine.py

Creates an optimized government workflow from the
AI reasoning output.
"""

from graph_engine import WorkflowGraph


class WorkflowEngine:

    def __init__(self):
        self.graph = WorkflowGraph()

    def generate_workflow(self, analysis):

        approvals = analysis.get("approvals", [])

        workflow = []

        previous = None

        for index, approval in enumerate(approvals):

            step = {
                "id": index + 1,
                "name": approval,
                "status": "Pending",
                "depends_on": previous,
                "estimated_days": 3,
                "department": analysis.get("department")
            }

            workflow.append(step)

            previous = approval

        graph = self.graph.build(workflow)

        return {
            "steps": workflow,
            "graph": graph,
            "total_steps": len(workflow),
            "estimated_completion": analysis.get("estimated_days"),
            "current_stage":
                workflow[0]["name"] if workflow else "Completed"
        }

    def next_step(self, workflow):

        for step in workflow["steps"]:
            if step["status"] == "Pending":
                return step

        return None

    def complete_step(self, workflow, step_id):

        for step in workflow["steps"]:

            if step["id"] == step_id:
                step["status"] = "Completed"

                break

        next_step = self.next_step(workflow)

        workflow["current_stage"] = (
            next_step["name"]
            if next_step
            else "Completed"
        )

        return workflow