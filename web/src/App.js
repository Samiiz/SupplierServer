import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignUp from './components/SignUp';
import Login from './components/Login';
import Order from './components/Order';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" component={SignUp} />
        <Route path="/login" component={Login} />
        <Route path="/orders" component={Order} />
        <Route path="/" exact component={SignUp} />
      </Routes>
    </Router>
  );
}

export default App;
