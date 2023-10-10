import React, { useState, useCallback, useContext } from 'react';
import { Row, Col, Form, Button } from 'react-bootstrap';
import { NavLink, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { TokenContext } from '../context/context';


export const SignUp = () => {
    const { dispatch } = useContext(TokenContext);
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        fullname: '',
        email: '',
        password: '',
        dob: '',
        gender: '',
        country: '',
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

        axios
            .post('http://localhost:8000/user/sign-up', formData)
            .then((res) => {

                const statusCode = res.status; // Check the status code from the backend
                if (statusCode === 201) {
                    const token = res.data.token.access_token;
                    // Dispatch action to update token and login state
                    dispatch({ type: 'SET_TOKEN', payload: token });
                    dispatch({ type: 'SET_LOGGED_IN', payload: true });
                    navigate('/user/home'); // Navigate to user/home page
                } else {
                    // console.log(res); // Log the entire response object for debugging
                    alert('An error occurred. Please try again later.');
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

    }, [formData, dispatch, navigate]);




    return (
        <div className="container my-4">
            <Row className="justify-content-center">
                <Col xs={12} sm={10} md={8} lg={6}>
                    <h1>Sign up</h1>
                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="firstname">
                            <Form.Label>Full Name:</Form.Label>
                            <Form.Control
                                type="text"
                                name="fullname"
                                value={formData.fullname}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>


                        <Form.Group controlId="email">
                            <Form.Label>Email:</Form.Label>
                            <Form.Control
                                type="email"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>

                        <Form.Group controlId="password">
                            <Form.Label>Password:</Form.Label>
                            <Form.Control
                                type="password"
                                name="password"
                                value={formData.password}
                                onChange={handleChange}
                                required
                                minLength={8}
                            />
                        </Form.Group>

                        <Form.Group controlId="dob">
                            <Form.Label>Date of Birth:</Form.Label>
                            <Form.Control
                                type="date"
                                name="dob"
                                value={formData.dob}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>

                        <Form.Group controlId="dob">
                            <Form.Label>Gender:</Form.Label>
                            <Form.Control
                                as="select"
                                name="gender"
                                value={formData.gender}
                                onChange={handleChange}
                                required
                            >
                                <option value="">Select Gender</option>
                                <option value="male">Male</option>
                                <option value="female">Female</option>
                                <option value="not-specified">Prefer not to say</option>
                            </Form.Control>
                        </Form.Group>


                        <Form.Group controlId="country">
                            <Form.Label>Country:</Form.Label>
                            <Form.Control
                                type="text"
                                name="country"
                                value={formData.country}
                                onChange={handleChange}
                                required
                            />
                        </Form.Group>

                        <Button className='my-3' variant="primary" type="submit">
                            Sign up
                        </Button>
                    </Form>
                    <p className="text-center mt-4">Already a user?
                        <NavLink
                            className="nav-link"
                            activeclassname="active"
                            to="/user/sign-in"
                        >Log in
                        </NavLink>
                    </p>
                </Col>
            </Row>
        </div>
    );
}