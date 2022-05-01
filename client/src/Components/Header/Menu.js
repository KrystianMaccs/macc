import React, { Component } from "react";
import "../navbar.css";

class Menu extends Component() {
  render (){
    return (
      <div className="navigation">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Info</a>
        <a href="#">Service</a>
        <a href="#">Contact</a>
      </div>
    )
  }
}

export default Menu