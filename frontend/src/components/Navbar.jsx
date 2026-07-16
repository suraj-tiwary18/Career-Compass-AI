import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">

      <div className="logo">
       🧭 Career Compass AI
      </div>

      <ul className="nav-links">

        <li>
          <NavLink to="/">Home</NavLink>
        </li>

        <li>
          <NavLink to="/predict">Predict</NavLink>
        </li>

        <li>
          <NavLink to="/history">History</NavLink>
        </li>

        <li>
          <NavLink to="/about">About</NavLink>
        </li>

      </ul>

    </nav>
  );
}

export default Navbar;