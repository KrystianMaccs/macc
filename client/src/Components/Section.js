import React, { Component } from "react";
class Section extends Component {
  render(){
    return (
      <div className='Section'>
          <div className="Greeting">
              <h1>Hi. I am Krystian Maccs</h1>
              <h3>And I am a Fullstack Web Developer</h3>
          </div>
          <div className="Image">
              <img src="krystian.jpg" alt="A photo of Krystian Maccs" />
          </div>
      
      </div>
    )
  }
}

export default Section