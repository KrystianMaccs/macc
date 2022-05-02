import React, { Component } from 'react';
import './App.css';
import Header from './Components/Header';
import Projects from './Components/Projects';
import Section from './Components/Section';
import Skills from './Components/Skills';
class App extends Component {
  render(){
    return (
      <div className='App'>
        <Header />
        <Section />
        <Projects />
        <Skills />
      </div>
    )
  }
}

export default App;
