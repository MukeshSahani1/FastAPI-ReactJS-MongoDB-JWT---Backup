import React, { useCallback, useContext, useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { TokenContext } from '../context/context';

export const SignIn = () => {

    const { dispatch } = useContext(TokenContext);
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const handleChange = useCallback((e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    }, []);

    const handleSubmit = useCallback((e) => {
        e.preventDefault();
        if (!formData.email || !formData.password) {
            alert("Email or Password cannot be blank..!!")
        }
        else {

            axios.post('http://localhost:8000/user/sign-in', formData)
                .then((res) => {

                    const statusCode = res.data.status_code; // Check the status code from the backend
                    if (statusCode === 200) {
                        const token = res.data.token.access_token;
                        // Dispatch action to update token and login state
                        dispatch({ type: 'SET_TOKEN', payload: token });
                        dispatch({ type: 'SET_LOGGED_IN', payload: true });
                        navigate('/user/home'); // navigate to user/home page

                    } else {
                        alert('Response from the backend API: ' + JSON.stringify(res.data.detail));
                        console.log(res);
                    }

                })
                .catch((error) => {
                    if (error.response) {
                        const statusCode = error.response.status;
                        const errorMessage = error.response.data.detail;
                        alert(`Error: ${statusCode} - ${errorMessage}`);
                    } else if (error.request) {
                        alert('No response received from the server'); // The request was made but no response was received
                    } else {
                        // Something happened in setting up the request that triggered an error
                        alert('Error: ' + error.message);
                    }
                });
        }
    }, [formData, dispatch, navigate]);


    return (

        <div className="container my-4">
            <div className="row justify-content-center">
                <div className="col-sm-6 col-md-4">
                    <h1 className="text-center mb-4">Welcome back</h1>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="email" className="form-label">Email address</label>
                            <input type="email" className="form-control" id="email" name='email' value={formData.email} onChange={handleChange} placeholder="Enter your email" required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="password" className="form-label">Password</label>
                            <input type="password" className="form-control" id="password" name='password' value={formData.password} onChange={handleChange} placeholder="Enter your password" minLength={8} required />
                        </div>
                        <button type="submit" className="btn btn-primary btn-full-width">Login</button>
                    </form>
                    <p className="text-center mt-4">Don't have an account?
                        <NavLink
                            className="nav-link"
                            activeclassname="active"
                            to="/user/sign-up"
                        >Sign up
                        </NavLink>
                    </p>
                </div>
            </div>
        </div>
    )
}



