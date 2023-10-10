import React from 'react';
import { NavLink } from 'react-router-dom';

export const Header = () => {
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
                                to="/"
                            >
                                <b>Home</b>
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink
                                className="nav-link"
                                activeclassname="active"
                                to="/about"
                            >
                                <b>About</b>
                            </NavLink>
                        </li>
                    </ul>

                    <NavLink
                        className="btn btn-outline-primary my-2 mx-4 my-sm-0"
                        to="/user/sign-in"
                    >
                        Log In
                    </NavLink>

                </div>
            </nav>
        </div>
    );
};
