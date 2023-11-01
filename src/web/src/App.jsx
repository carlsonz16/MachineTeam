import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navbar } from './components'
import './App.css'

const Home = () => <div>Home Page</div>;
const About = () => <div>About Page</div>;
const Contact = () => <div>Contact Page</div>;

function App() {
   return (
       <Router>
           <div>
               <Navbar />
               <Routes>
                   <Route path="/" exact component={Home} />
                   <Route path="/about" component={About} />
                   <Route path="/contact" component={Contact} />
               </Routes>
           </div>
       </Router>
   );
}

export default App
