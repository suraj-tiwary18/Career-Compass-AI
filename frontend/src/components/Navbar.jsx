import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">

      <div className="logo">
        Career Compass AI
      </div>

      <div className="nav-links">

        <NavLink to="/">Home</NavLink>

        <NavLink to="/predict">Predict</NavLink>

        <NavLink to="/history">History</NavLink>

        <NavLink to="/about">About</NavLink>

      </div>

    </nav>
  );
}

export default Navbar;