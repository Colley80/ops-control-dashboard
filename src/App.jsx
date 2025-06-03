// frontend/src/App.jsx

import React from 'react';
import Dashboard from './components/Dashboard';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './index.css';

function App() {
  return (
    <>
      <Dashboard />
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop />
    </>
  );
}

export default App;
