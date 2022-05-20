import AboutContent from "../Components/AboutContent";
import AboutHeading from "../Components/AboutHeading";
import AboutText from "../Components/AboutText";
const About = () => {
    return ( 
        <section className='about container' id='about'>
            <AboutHeading />
            <AboutContent />
            <AboutText />
        </section>
     );
}
 
export default About;