import { Link, Router } from '@reach/router';

import About from '../About/About'
import Contact from '../Contact/Contact'
import Home from "../Home/Home"
import Post from '../Post/Post';
import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {
    return (
        <React.StrictMode>
            <header className="bg-black-90 fixed w-100 ph3 pv3 pv4-ns ph4-m ph5-l">
                <nav className="f6 fw6 ttu tracked">
                    <Link to="/">Home</Link>
                    <Link to="/about">About</Link>
                    <Link to="/contact">Contact</Link>
                </nav>
            </header>
            <Router>
                <Home path="/" />
                <About path="/about" />
                <Contact path="/contact" />
            </Router>
            <footer>
                <h1>Footer</h1>
            </footer>
        </React.StrictMode>
    )
}

ReactDOM.render(<App />, document.querySelector('#root'));