import React, { useState, useEffect } from "react";
import WorkflowGraph from "./WorkflowGraph"; 

const Dashboard = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Relative path to your Flask backend
    fetch('/api/get-workflow')
      .then(res => res.json())
      .then(data => setData(data))
      .catch(err => console.error("Error loading workflow:", err));
  }, []);

  if (!data) return <div>Loading...</div>;

  return <WorkflowGraph graph={data} />;
};

export default Dashboard;
