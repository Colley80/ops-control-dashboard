import React, { useState } from 'react';
import { addProcess } from '../services/ProcessService';

function AddProcessForm({ onProcessAdded }) {
  const [name, setName] = useState('');
  const [priority, setPriority] = useState('Medium');
  const [timestamp, setTimestamp] = useState('');
  const [loading, setLoading] = useState(false);   // NEW: loading state

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);  // Disable button while adding

    try {
      await addProcess({ name, priority, timestamp });
      setName('');
      setPriority('Medium');
      setTimestamp('');
      onProcessAdded();
    } catch (error) {
      console.error('Error adding process:', error);
    } finally {
      setLoading(false);  // Re-enable button
    }
  };

  return (
    <div>
      <h2>Add New Process</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Priority:</label>
          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
          >
            <option value="High">High</option>
            <option value="Medium">Medium</option>
            <option value="Low">Low</option>
          </select>
        </div>
        <div>
          <label>Timestamp (UTC):</label>
          <input
            type="datetime-local"
            value={timestamp}
            onChange={(e) => setTimestamp(e.target.value)}
            required
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Adding...' : 'Add Process'}
        </button>
      </form>
    </div>
  );
}

export default AddProcessForm;
