"""
graph_engine.py

Creates a workflow dependency graph for Mārga.
This graph is used by the frontend to visualize
government approval workflows.
"""


class WorkflowGraph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def build(self, workflow):

        self.nodes = []
        self.edges = []

        previous = None

        for step in workflow:

            node = {
                "id": step["id"],
                "label": step["name"],
                "status": step["status"],
                "department": step["department"]
            }

            self.nodes.append(node)

            if previous is not None:

                self.edges.append({
                    "from": previous,
                    "to": step["id"]
                })

            previous = step["id"]

        return {
            "nodes": self.nodes,
            "edges": self.edges
        }

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def adjacency_list(self):

        graph = {}

        for node in self.nodes:
            graph[node["id"]] = []

        for edge in self.edges:
            graph[edge["from"]].append(edge["to"])

        return graph

    def critical_path(self):

        return [
            node["label"]
            for node in self.nodes
        ]

    def bottlenecks(self):

        bottleneck_nodes = []

        for node in self.nodes:

            if node["status"] != "Completed":

                bottleneck_nodes.append(node["label"])

        return bottleneck_nodes