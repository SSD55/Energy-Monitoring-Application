import React, { useEffect, useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";
import "bootstrap/dist/css/bootstrap.min.css";

// Register required chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Dashboard = () => {
  const [energyData, setEnergyData] = useState([]);
  const [deviceId, setDeviceId] = useState("A001"); // Default device
  const [budget, setBudget] = useState(0);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetchEnergyData();
  }, [deviceId]);

  const fetchEnergyData = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/energy-data");
      const filteredData = response.data.filter(entry => entry.device_id === deviceId);
      setEnergyData(filteredData);
    } catch (error) {
      console.error("Error fetching energy data:", error);
    }
  };


  const chartData = {
    labels: energyData.map((entry) => new Date(entry.timestamp).toLocaleTimeString()),
    datasets: [
      {
        label: "Energy Consumption (kWh)",
        data: energyData.map((entry) => entry.energy_kwh),
        borderColor: "#007bff",
        fill: false,
      },
    ],
  };

  return (
    <div className="container mt-4">
      <h2 className="text-center">Smart Home Energy Dashboard</h2>
      <div className="mb-3">
        <label>Select Device:</label>
        <select className="form-control" value={deviceId} onChange={(e) => setDeviceId(e.target.value)}>
          <option value="A001">Refrigerator(A001)</option>
          <option value="A002">Washing Machine(A002)</option>
          <option value="A003">Air Conditioner(A003)</option>
          <option value="A004">TV(A004)</option>
          <option value="A005">Heater(A005)</option>
          <option value="A006">Microwave(A006)</option>
        </select>
      </div>


      <div className="card p-3">
        <Line data={chartData} />
      </div>
      </div>
  );
};

export default Dashboard;
