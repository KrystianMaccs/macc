import React, { Component } from 'react';
import './App.css';
import Logo from './Components/Header/Logo';
import Menu from './Components/Header/Menu';

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