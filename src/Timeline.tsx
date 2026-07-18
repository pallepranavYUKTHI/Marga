import React from "react";

interface Step {
  id: number;
  name: string;
  status: string;
  estimated_days: number;
  department: string;
}

interface Props {
  workflow: {
    steps: Step[];
    estimated_completion: number;
    current_stage: string;
  };
}

const Timeline: React.FC<Props> = ({ workflow }) => {
  const getColor = (status: string) => {
    switch (status) {
      case "Completed":
        return "bg-green-500";
      case "In Progress":
        return "bg-blue-500";
      default:
        return "bg-yellow-500";
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mt-6">

      <h2 className="text-xl font-bold mb-4">
        Workflow Timeline
      </h2>

      <div className="space-y-5">

        {workflow.steps.map((step) => (

          <div
            key={step.id}
            className="flex items-start gap-4"
          >

            <div
              className={`w-5 h-5 rounded-full mt-1 ${getColor(step.status)}`}
            />

            <div className="flex-1">

              <h3 className="font-semibold">
                {step.name}
              </h3>

              <p className="text-sm text-gray-600">
                Department: {step.department}
              </p>

              <p className="text-sm text-gray-500">
                Estimated: {step.estimated_days} days
              </p>

              <span
                className={`inline-block mt-2 px-3 py-1 rounded-full text-xs text-white ${
                  step.status === "Completed"
                    ? "bg-green-500"
                    : step.status === "In Progress"
                    ? "bg-blue-500"
                    : "bg-yellow-500"
                }`}
              >
                {step.status}
              </span>

            </div>

          </div>

        ))}

      </div>

      <div className="border-t mt-6 pt-4">

        <p>
          <strong>Current Stage:</strong>{" "}
          {workflow.current_stage}
        </p>

        <p>
          <strong>Estimated Completion:</strong>{" "}
          {workflow.estimated_completion} days
        </p>

      </div>

    </div>
  );
};

export default Timeline;
