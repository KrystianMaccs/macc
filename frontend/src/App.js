import './App.css';
import About from './Components/About';
import Contact from './Components/Contact';
import Footer from "./Components/Footer";
import Header from './Components/Header';
import Portfolio from './Components/Portfolio';
import Section from './Components/Section';
import Service from './Components/Service';

function App() {
  return (
    <div className="App">
        <Header />
        <Section />
        <About />
        <Service />
        <Portfolio />
        <Contact />
        <Footer />
    </div>
  );
}

export default App;
