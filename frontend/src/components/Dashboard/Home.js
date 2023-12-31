import React from "react";
import "./Home.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import NewShipment from "./pages/NewShipment";
import MyShipment from "./pages/MyShipment";
import DeviceData from "./pages/DeviceData";
import MyAccount from "./pages/MyAccount";
import Sidebar from "./Sidebar";
import { useContext } from "react";
import Login from "../Login/Login";
import { TokenProvider, TokenContext } from "../../context/context";

const Home = () => {
  const { state } = useContext(TokenContext);
  const { isLoggedIn } = state;
  console.log(isLoggedIn);
  return (
    <Router>
      {!isLoggedIn ? (
        <Login />
      ) : (
        <div className="App">
          <Sidebar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/newShipment" element={<NewShipment />} />
            <Route path="/myShipment" element={<MyShipment />} />
            <Route path="/deviceData" element={<DeviceData />} />
            <Route path="/myAccount" element={<MyAccount />} />
          </Routes>
        </div>
      )}
    </Router>
  );
};

export default Home;
