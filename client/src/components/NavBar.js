
import { NavLink } from "react-router";

function NavBar() {

  return <nav>
    <NavLink to="/">Home</NavLink>
    <NavLink to="/owners">Owners</NavLink>
  </nav>
}

export default NavBar;