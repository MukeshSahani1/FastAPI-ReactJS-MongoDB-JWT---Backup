import './App.css'
import Login from './components/Login/Login';
import Home from './components/Dashboard/Home';
import React, { useContext } from 'react';
import { BrowserRouter as Router, Route,Routes,Navigate} from 'react-router-dom';
import { TokenProvider, TokenContext } from './context/context';
function App() {
  const { state } = useContext(TokenContext);
  const { isLoggedIn } = state;
  console.log(isLoggedIn);
  return (
    
      // <Router>
      //   {isLoggedIn?<Home/>:<Login/>}
      //   <Routes path='/' element={isLoggedIn?<Home/>:<Login/>}/>
      //   {/* <Routes exact path='/home' element={<Home/>}/> */}
      // </Router>
      <Router>
        <Routes>
          <Route
            exact path=""
            element={isLoggedIn ? <Home /> : <Login />}
          />
        </Routes>
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
