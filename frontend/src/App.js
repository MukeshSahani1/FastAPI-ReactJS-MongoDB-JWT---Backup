import './App.css';
import { Home } from './MyComponents/Home';
import { Header } from './MyComponents/Header';
import { LoggedInHeader } from './MyComponents/LoggedInHeader';
import { About } from './MyComponents/About';
import { Footer } from './MyComponents/Footer';
import { SignIn } from './MyComponents/SignIn';
import { SignUp } from './MyComponents/SignUp';
import { Welcome } from './MyComponents/Welcome';

import React, { useContext } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { TokenProvider, TokenContext } from './context/context';

function App() {

  const { state } = useContext(TokenContext);
  const { isLoggedIn } = state; // Access the token value from the state object


  return (
    <Router>
      {isLoggedIn ? <LoggedInHeader /> : <Header />}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/user/sign-in" element={<SignIn />}  />
        <Route path="/user/sign-up" element={<SignUp />} />
        <Route path="/user/home" element={<Welcome />} />
      </Routes>
      <Footer />
    </Router>
  );
}

function AppWrapper() {
  return (
    <TokenProvider>
      <App />
    </TokenProvider>
  );
}

export default AppWrapper;
