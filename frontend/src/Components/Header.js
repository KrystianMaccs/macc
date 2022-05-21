
const Header = (props) => {
    return ( 
     <header>
           <div className="nav container">
                <a href="www.facebook.com" className="logo">Krystian</a>
                <ul className='navbar'>
                  <li><a href="#home" className="nav-link">Home</a></li>
                  <li><a href="#about" className="nav-link">About</a></li>
                  <li><a href="#services" className="nav-link">Services</a></li>
                  <li><a href="#portfolio" className="nav-link">Portfolio</a></li>
                  <li><a href="#contact" className="nav-link">Contact</a></li>
               </ul>
               <div className="menu-icon">
                  <div className="line1"></div>
                  <div className="line2"></div>
                  <div className="line3"></div>
                </div>
       </div>
     </header>
    );
}
 
export default Header;