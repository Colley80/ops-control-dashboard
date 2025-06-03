// frontend/src/services/ProcessService.js

import { toast } from 'react-toastify';

const API_URL = 'http://127.0.0.1:5000';

export async function fetchProcesses() {
  try {
    const response = await fetch(`${API_URL}/processes`);
    if (!response.ok) throw new Error('Failed to fetch processes');
    return response.json();
  } catch (error) {
    toast.error(`Error loading processes: ${error.message}`);
    throw error;
  }
}

export async function addProcess(process) {
  try {
    const response = await fetch(`${API_URL}/processes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(process),
    });
    if (!response.ok) throw new Error('Failed to add process');
    toast.success('Process added successfully');
    return response.json();
  } catch (error) {
    toast.error(`Error adding process: ${error.message}`);
    throw error;
  }
}

export async function deleteProcess(id) {
  try {
    const response = await fetch(`${API_URL}/processes/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete process');
    toast.success('Process deleted successfully');
    return response.json();
  } catch (error) {
    toast.error(`Error deleting process: ${error.message}`);
    throw error;
  }
}
