import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginScreen from './components/LoginScreen';
import MainScreen from './components/MainScreen';
import PaymentScreen from './components/PaymentScreen';
import PaymentRegister from './components/PaymentRegister';
import LoanReportForm from './components/LoanReportForm';

const App = () => {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<LoginScreen />} />
          <Route path="/MainScreen" element={<MainScreen />} />
          <Route path="/PaymentScreen" element={<PaymentScreen />} />
          <Route path="/PaymentRegister" element={<PaymentRegister />} />
          <Route path="/LoanReportForm" element={<LoanReportForm />} />
        </Routes>
      </Router>
    </div>
  );
};

export default App;
