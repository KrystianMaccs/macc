import PortfolioContent from '../Components/PortfolioContent';
import PortfolioHead from '../Components/PortfolioHead';

const Portfolio = () => {
    return ( 
        <section className='portfolio container' id='portfolio'>
            <PortfolioHead />
            <PortfolioContent />
        </section>
     );
}
 
export default Portfolio;