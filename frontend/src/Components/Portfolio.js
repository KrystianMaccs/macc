
const Portfolio = () => {
    return ( 
        <section className='portfolio container' id='portfolio'>
            <h2 className='heading'>Portfolio</h2>
            <div className='portfolio-content'>
                <div className='portfolio-box'>
                    <img src="web.jpg" alt="" className="portfolio-img" />
                    <div className="portfolio-overlay">
                        <h2>Web Development</h2>
                        <a href="img.png">
                            <i class='bx bx-link-alt'></i>
                        </a>
                    </div>
                </div>

                <div className='portfolio-box'>
                    <img src="data.jpg" alt="" className="portfolio-img" />
                    <div className="portfolio-overlay">
                        <h2>Data Science</h2>
                        <a href="img.png">
                            <i class='bx bx-link-alt'></i>
                        </a>
                    </div>
                </div>

                <div className='portfolio-box'>
                    <img src="game.jpg" alt="" className="portfolio-img" />
                    <div className="portfolio-overlay">
                        <h2>Game Development</h2>
                        <a href="www.twitter.com">
                            <i class='bx bx-link-alt'></i>
                        </a>
                    </div>
                </div>
            </div>
        </section>
     );
}
 
export default Portfolio;