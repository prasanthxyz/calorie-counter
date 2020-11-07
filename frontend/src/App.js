import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route } from 'react-router-dom';
import Navbar from './Navbar';
import Day from './Day';
import Foods from './Foods';
import Home from './Home';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Navbar />
        <Route exact path="/"><Home /></Route>
        <Route exact path="/day/"><Day /></Route>
        <Route exact path="/foods/"><Foods /></Route>
      </div>
    </BrowserRouter>
  );
}

export default App;
