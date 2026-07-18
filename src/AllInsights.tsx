import React from "react";

interface Props {
  department: string;
  confidence: number;
  estimatedDays: number;
  approvals: string[];
  documents: string[];
  nextStep: string;
}

const AIInsights: React.FC<Props> = ({
  department,
  confidence,
 estimatedDays,
  approvals,
  documents,
  nextStep,
}) => {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mt-6">

      <h2 className="text-2xl font-bold mb-6">
        AI Insights
      </h2>

      <div className="grid grid-cols-2 gap-4">

        <div className="bg-blue-50 rounded-lg p-4">
          <p className="text-sm text-gray-500">
            Assigned Department
          </p>

          <p className="text-xl font-bold">
            {department}
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

        <div className="bg-purple-50 rounded-lg p-4">
          <p className="text-sm text-gray-500">
            Estimated Processing Time
          </p>

          <p className="text-xl font-bold">
            {estimatedDays} Days
          </p>
        </div>

        <div className="bg-orange-50 rounded-lg p-4">
          <p className="text-sm text-gray-500">
            Total Approvals
          </p>

          <p className="text-xl font-bold">
            {approvals.length}
          </p>
        </div>

      </div>

      <div className="mt-6">

        <h3 className="font-semibold mb-3">
          Required Approvals
        </h3>

        <ul className="list-disc ml-6">

          {approvals.map((approval, index) => (

            <li key={index}>
              {approval}
            </li>

          ))}

        </ul>

      </div>

      <div className="mt-6">

        <h3 className="font-semibold mb-3">
          Required Documents
        </h3>

        <ul className="list-disc ml-6">

          {documents.map((doc, index) => (

            <li key={index}>
              {doc}
            </li>

          ))}

        </ul>

      </div>

      <div className="mt-6 bg-yellow-50 border-l-4 border-yellow-500 p-4 rounded">

        <h3 className="font-semibold">
          Recommended Next Step
        </h3>

        <p>{nextStep}</p>

      </div>

    </div>
  );
};

export default AIInsights;
