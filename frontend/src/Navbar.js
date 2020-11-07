import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <Link to="/">Home</Link>
        <Link to="/day/">Daily Log</Link>
        <Link to="/foods/">Food Manager</Link>
      </ul>
    </nav>
  );
}

export default Navbar;
