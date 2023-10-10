import React, { useContext } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { TokenContext } from '../context/context';

export const LoggedInHeader = ({ handleLogin }) => {

    const navigate = useNavigate();

    const { dispatch } = useContext(TokenContext);
    const { state } = useContext(TokenContext);
    const { token } = state; // Access the token value from the state object

    const handleLogout = (e) => {
        e.preventDefault();

        axios
            .post('http://localhost:8000/token/blacklist', {
                "token": token
            })
            .then((res) => {
                // Check the status code from the backend
                const statusCode = res.status;
                if (statusCode === 200) {
                    dispatch({ type: 'SET_LOGGED_IN', payload: false });
                    navigate('/'); // Navigate to home page
                } else {
                    console.log(res); // Log the entire response object for debugging
                    alert('An error occurred. Please try again later.');
                }
            })
            .catch((error) => {
                if (error.response) {

                    const statusCode = error.response.status;
                    const errorMessage = error.response.data.detail;
                    alert(`Error: ${statusCode} - ${errorMessage}`);
                } else if (error.request) {
                    // The request was made but no response was received
                    alert('No response received from the server');
                } else {
                    // Something happened in setting up the request that triggered an error
                    alert('Error: ' + error.message);
                }
            });

    };

    return (
        <div className="contain">
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                {/* <Link className="navbar-brand" to="/">
                    Navbar
                </Link> */}
                <button
                    className="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse justify-content-between mx-3" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <NavLink
                                className="nav-link"
                                activeclassname="active"
                                to="#"
                            >
                                <b>Home</b>
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink
                                className="nav-link"
                                activeclassname="active"
                                to="#"
                            >
                                <b>Account</b>
                            </NavLink>
                        </li>
                    </ul>

                    <NavLink
                        className="btn btn-outline-primary my-2 mx-4 my-sm-0"
                        onClick={handleLogout}
                    >
                        Logout
                    </NavLink>

                </div>
            </nav>
        </div>
    );
}
