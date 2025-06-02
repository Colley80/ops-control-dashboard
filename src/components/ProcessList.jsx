// frontend/src/components/ProcessList.jsx

import React, { useEffect, useState } from 'react';
import { fetchProcesses, deleteProcess } from '../services/ProcessService';

function ProcessList() {
  const [processes, setProcesses] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadProcesses = async () => {
    setLoading(true);
    try {
      const data = await fetchProcesses();
      setProcesses(data.processes || []); // In case API returns { processes: [] }
    } catch (error) {
      console.error('Error loading processes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteProcess(id);
      await loadProcesses();
    } catch (error) {
      console.error('Error deleting process:', error);
    }
  };

  useEffect(() => {
    loadProcesses();
  }, []);

  return (
    <div>
      <h2>Process List</h2>
      {loading ? (
        <p>Loading...</p>
      ) : processes.length === 0 ? (
        <p>No processes available.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Priority</th>
              <th>Timestamp</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {processes.map((process) => (
              <tr key={process.id}>
                <td>{process.id}</td>
                <td>{process.name}</td>
                <td>{process.priority}</td>
                <td>{process.timestamp ? process.timestamp : 'N/A'}</td> {/* Safe fallback */}
                <td>
                  <button onClick={() => handleDelete(process.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ProcessList;
