import React from 'react';
import { Link } from 'react-router-dom';
import { logo } from '../assets';

const Navbar = () => {
   return (
      <nav className="flex justify-between items-center p-5 bg-blue-500">
            <img src={logo} alt="Logo" className="h-10 w-auto mr-10" /> {/* Added margin to the logo */}
            <div className="flex gap-4">
               <Link to="/" className="text-white">Home</Link>
               <Link to="/about" className="text-white">About</Link>
               <Link to="/contact" className="text-white">Contact</Link>
            </div>
      </nav>
   );
}

export default Navbar;
