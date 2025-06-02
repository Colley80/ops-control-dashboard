// frontend/src/components/Dashboard.jsx

import React from 'react';
import AddProcessForm from './AddProcessForm';
import ProcessList from './ProcessList';
import './Dashboard.css';

function Dashboard() {
  return (
    <div className="dashboard-container">
      <header>
        <h1>Ops Control Dashboard</h1>
      </header>
      <main className="dashboard-main">
        <section className="dashboard-form">
          <AddProcessForm onProcessAdded={() => window.location.reload()} />
        </section>
        <section className="dashboard-list">
          <ProcessList />
        </section>
      </main>
    </div>
  );
}

export default Dashboard;
