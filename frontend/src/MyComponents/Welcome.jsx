import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { TokenContext } from '../context/context';

export const Welcome = () => {

    const [users, setUsers] = useState([{}])

    const { state } = useContext(TokenContext);
    const { token } = state; // Access the token value from the state object


    // Read all Todos
    useEffect(() => {
        axios.get('http://localhost:8000/test/users/all', {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        }).then(res => {
            setUsers(res.data)
        })
    }, [token]);

    return (
        <div className="container my-3">
            <h1>Welcome User . Login Succesfull .!!</h1>
            <ul>
                {users.map(user => (
                    <li key={user.email}>
                        <p>Name: {user.First_name}</p>
                        <p>Email: {user.email}</p>
                        {/* Add additional user information here */}
                    </li>
                ))}
            </ul>
        </div>
    )
}
