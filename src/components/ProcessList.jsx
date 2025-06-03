// frontend/src/components/ProcessList.jsx

import React, { useEffect, useState } from 'react';
import { fetchProcesses, deleteProcess } from '../services/ProcessService';

function ProcessList() {
  const [processes, setProcesses] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);
  const [perPage] = useState(5);
  const [total, setTotal] = useState(0);

  const loadProcesses = async () => {
    setLoading(true);
    try {
      const data = await fetchProcesses(page, perPage);
      setProcesses(data.processes || []);
      setTotal(data.total || 0);
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
  }, [page]);

  const totalPages = Math.ceil(total / perPage);

  return (
    <div>
      <h2>Process List</h2>
      {loading ? (
        <p>Loading...</p>
      ) : processes.length === 0 ? (
        <p>No processes available.</p>
      ) : (
        <>
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
                  <td>{process.timestamp}</td>
                  <td>
                    <button onClick={() => handleDelete(process.id)}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          <div style={{ marginTop: '10px' }}>
            <button
              onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
              disabled={page === 1}
            >
              Previous
            </button>
            <span style={{ margin: '0 10px' }}>
              Page {page} of {totalPages}
            </span>
            <button
              onClick={() => setPage((prev) => Math.min(prev + 1, totalPages))}
              disabled={page === totalPages}
            >
              Next
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default ProcessList;
