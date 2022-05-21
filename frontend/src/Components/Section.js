
const Section = () => {
    return ( 
        <div className="home container home">
            <div className='home-content'>
                    <div className="home-img">
                        <img src="/kris.JPG" alt="" />
                    </div>
                    <div className="home-text">
                        <h3>Hello</h3>
                        <h2>I'm <span className="color">Krystian Maccs</span></h2>
                        <p>I'm Lorem ipsum, dolor sit amet consectetur adipisicing elit. Porro rerum ex sit deserunt quidem perferendis, molestiae eos vitae quisquam voluptate autem iure illo incidunt. Suscipit eaque veniam pariatur debitis ullam.</p>
                    </div>
                    <div className="social">
                        <a href="https://www.twitter.com/KrystianMaccs"><i class='bx bxl-twitter'></i></a>
                        <a href="https://www.linked.com/krystianmaccs"><i class='bx bxl-linkedin'></i></a>
                        <a href="https://www.github.com/KrystianMaccs"><i class='bx bxl-github'></i></a>
                    </div>
            </div>
        </div>
     );
}
 
export default Section;