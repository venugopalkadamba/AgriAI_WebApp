import React, { useState } from 'react'
import { NavLink, useHistory } from "react-router-dom"
import { MenuList } from "./MenuList"
import "../styles/NavBar.css"
import 'font-awesome/css/font-awesome.min.css';

const Navbar = () => {
    const [clicked, setClicked] = useState(false);

    const history = useHistory()

    const menuList = MenuList.map(({ url, title }, index) => {
      return (
        <li key={index}>
          <NavLink exact to={url} activeClassName="active">
            {title}
          </NavLink>
        </li>
      );
    });
  
    const handleClick = () => {
      setClicked(!clicked);
    };

    const handleTitleClick = () => {
      history.push("/")
    }
  
    return (
      <nav>
        <div onClick={handleTitleClick} className="logo">
          Agri<font>AI</font>
        </div>
        <div className="menu-icon" onClick={handleClick}>
          <i className={clicked ? "fa fa-times" : "fa fa-bars"}></i>
        </div>
        <ul className={clicked ? "menu-list" : "menu-list close"}>{menuList}</ul>
      </nav>
    );
  };
  
  export default Navbar;
