
import { NavLink } from "react-router";
import "./NavBar.css";

function NavBar() {

  return <nav>
    <NavLink to="/" className={"nav-link"}>Home</NavLink>
    <NavLink to="/owners" className={"nav-link"}>Owners</NavLink>
  </nav>
}

export default NavBar;