// frontend/src/services/ProcessService.js

const API_URL = 'http://127.0.0.1:5000';

export async function fetchProcesses(page = 1, perPage = 5) {
  const response = await fetch(`${API_URL}/processes?page=${page}&per_page=${perPage}`);
  if (!response.ok) throw new Error('Failed to fetch processes');
  return response.json();
}

export async function addProcess(process) {
  const response = await fetch(`${API_URL}/processes`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(process),
  });
  if (!response.ok) throw new Error('Failed to add process');
  return response.json();
}

export async function deleteProcess(id) {
  const response = await fetch(`${API_URL}/processes/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) throw new Error('Failed to delete process');
  return response.json();
}
