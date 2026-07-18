import React from "react";

interface Props {
  goal: string;
  department: string;
  approvals: string[];
  documents: string[];
  estimatedDays: number;
  confidence: number;
  nextStep: string;
}

const RoutePlanner: React.FC<Props> = ({
  goal,
  department,
  approvals,
  documents,
  estimatedDays,
  confidence,
  nextStep,
}) => {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mt-6">

      <h2 className="text-2xl font-bold mb-4">
        AI Route Planner
      </h2>

      <div className="space-y-4">

        <div>
          <p className="font-semibold">Goal</p>
          <p>{goal}</p>
        </div>

        <div>
          <p className="font-semibold">Responsible Department</p>
          <p>{department}</p>
        </div>

        <div>
          <p className="font-semibold mb-2">
            Recommended Approval Order
          </p>

          {approvals.map((approval, index) => (
            <div
              key={index}
              className="flex items-center mb-2"
            >
              <div className="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center mr-3">
                {index + 1}
              </div>

              <span>{approval}</span>
            </div>
          ))}
        </div>

        <div>
          <p className="font-semibold mb-2">
            Required Documents
          </p>

          <ul className="list-disc ml-6">
            {documents.map((doc, index) => (
              <li key={index}>{doc}</li>
            ))}
          </ul>
        </div>

        <div className="grid grid-cols-2 gap-4 mt-6">

          <div className="bg-blue-50 rounded-lg p-4">
            <p className="text-sm text-gray-500">
              Estimated Time
            </p>

            <p className="text-xl font-bold">
              {estimatedDays} Days
            </p>
          </div>

          <div className="bg-green-50 rounded-lg p-4">
            <p className="text-sm text-gray-500">
              AI Confidence
            </p>

            <p className="text-xl font-bold">
              {(confidence * 100).toFixed(0)}%
            </p>
          </div>

        </div>

        <div className="bg-yellow-50 border-l-4 border-yellow-500 p-4 mt-6 rounded">

          <p className="font-semibold">
            Suggested Next Action
          </p>

          <p>{nextStep}</p>

        </div>

      </div>

    </div>
  );
};

export default RoutePlanner;
