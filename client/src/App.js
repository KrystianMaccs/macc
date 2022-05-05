import React, { Component } from 'react';
import './App.css';
import Logo from './Components/Logo';
import Menu from './Components/Menu';
import Projects from './Components/Projects';
import Section from './Components/Section';
import Skills from './Components/Skills';
class App extends Component {
  render(){
    return (
      <div className='App'>
        <Logo />
        <Menu />
        <Section />
        <Projects />
        <Skills />
      </div>
    )
  }
}

export default App;
