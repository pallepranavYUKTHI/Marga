import React, { useState, useEffect } from "react";
import WorkflowGraph from "./WorkflowGraph";

const Dashboard = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // This fetches data from your backend logic
    fetch('/api/get-workflow') 
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(err => console.error("Error loading workflow:", err));
  }, []);

  if (loading) return <div>Loading your Mārga workflow...</div>;

  return <WorkflowGraph graph={data} />;
};

export default Dashboard;
