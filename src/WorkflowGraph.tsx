import React from "react";

interface Node {
  id: number;
  label: string;
  status: string;
  department: string;
}

interface Edge {
  from: number;
  to: number;
}

interface Props {
  graph: {
    nodes: Node[];
    edges: Edge[];
  };
}

const WorkflowGraph: React.FC<Props> = ({ graph }) => {
  return (
    <div className="bg-white rounded-xl shadow-md p-6 mt-6">
      <h2 className="text-xl font-bold mb-4">
        Workflow Graph
      </h2>

      {graph.nodes.map((node) => (
        <div
          key={node.id}
          className="border rounded-lg p-4 mb-3 bg-gray-50"
        >
          <div className="font-semibold">
            {node.label}
          </div>

          <div className="text-sm text-gray-600">
            Department: {node.department}
          </div>

          <div
            className={`text-sm mt-2 ${
              node.status === "Completed"
                ? "text-green-600"
                : "text-orange-600"
            }`}
          >
            {node.status}
          </div>
        </div>
      ))}

      <div className="mt-6">
        <h3 className="font-semibold mb-2">
          Dependencies
        </h3>

        {graph.edges.map((edge, index) => (
          <div key={index}>
            Step {edge.from} → Step {edge.to}
          </div>
        ))}
      </div>
    </div>
  );
};

export default WorkflowGraph;
