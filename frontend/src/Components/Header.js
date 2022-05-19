import Logo from '../Components/Logo';
import Menu from '../Components/Menu';
import Navbar from '../Components/Navbar';

const Header = () => {
    /*let menu = document.querySelector("menu-icon");
    menu.onClick = () =>{
        menu.classList.toggle("move");
    };*/
    
    return ( 
     <header>
           <div className="nav container">
            <Logo />
           <Navbar />
           <Menu />
       </div>
     </header>
    );
}
 
export default Header;