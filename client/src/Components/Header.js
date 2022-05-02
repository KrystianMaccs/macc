import React, { Component } from 'react';
import './App.css';
import Logo from './Components/Header';
import Menu from './Components/Menu';

class Header extends Component (){
    render (){
        return (
          <header>
              <Logo />
              <Menu />
          </header>
        )
    }
}

export default Header