import React, { Component } from 'react';
import './App.css';
import Hello from './Components/Navbar';
import Projects from './Components/Projects';
import Section from './Components/Section';
import Skills from './Components/Skills';
class App extends Component {
  render(){
    return (
      <div className='App'>
        <Hello />
        <Section />
        <Projects />
        <Skills />
      </div>
    )
  }
}

export default App;
