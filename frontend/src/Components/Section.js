import Greet from '../Components/Greeting';
import ProfileImg from '../Components/ProfileImage';
import Social from '../Components/Social';

const Section = () => {
    return ( 
        <div className='home container'>
            <div className='home-content'>
                <ProfileImg />
                <Greet />
                <Social />
            </div>
        </div>
     );
}
 
export default Section;