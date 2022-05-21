const About = (props) => {
    return ( 
        <section className='about container' id='about'>
            <h2 className='heading'>About</h2>
            <div className='about-content'>
                <div className='about-data'>
                    <span>About Me</span>
                    <h2>Web Developer, <br /> Data Scientist, Game Developer</h2>
                    <a href="www.twitter.com" className='btn'>Download CV
                    <i class='bx bx-download'></i></a>
                </div>
            </div>
            <div className='about-text'>
                <p>Hello, I'm Krystian Maccs. A web developer, Data Scientist and Game developer</p>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim voluptatem magnam illum tempore a perferendis reiciendis magni! Maiores quasi culpa maxime officia voluptatum in alias aliquam, optio esse! Autem, magnam?</p>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ducimus quia ab itaque vel deserunt earum aspernatur dolorum sequi neque pariatur error natus suscipit porro consequatur, libero aperiam officia eius officiis.</p>
            </div>
        </section>
     );
}
 
export default About;