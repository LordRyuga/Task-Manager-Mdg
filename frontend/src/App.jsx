import React, { useState } from 'react'
import axios from 'axios'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Login from './features/auth/login'
// import Home from './features/home/home'
import Register from './features/auth/register'

import './App.css'


function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
