import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  Navbar,
  MobileNav,
  Typography,
  Menu,
  MenuList,
  MenuItem,
  Card,
  IconButton,
} from "@material-tailwind/react";
import {
  HomeIcon,
  LightBulbIcon,
  CalendarIcon,
  QuestionMarkCircleIcon,
  UserIcon,
  Bars2Icon,
} from "@heroicons/react/24/solid";

const NavListMenu = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  
  return (
    <React.Fragment>
      <Menu allowHover open={isMenuOpen} handler={setIsMenuOpen}>
        <MenuList className="hidden w-[36rem] grid-cols-7 gap-3 overflow-visible lg:grid">
          <Card
            color="blue"
            shadow={false}
            variant="gradient"
            className="col-span-3 grid h-full w-full place-items-center rounded-md"
          >
            <></>
          </Card>
          <ul className="col-span-4 flex w-full flex-col gap-1">
          </ul>
        </MenuList>
      </Menu>
      <ul className="ml-6 flex w-full flex-col gap-1 lg:hidden">
      </ul>
    </React.Fragment>
  );
};

const NavList = () => {
  const navListItems = [
    { label: "Home", icon: HomeIcon, to: "/" },
    { label: "Upcoming NBA Games", icon: CalendarIcon, to: "/upcoming-games" },
    { label: "Live Games and Predictions", icon: LightBulbIcon, to: "/predictions" },
    { label: "Statistics", icon: UserIcon, to: "/player-stats" },
    { label: "About", icon: QuestionMarkCircleIcon, to: "/about" },
  ];
  
  return (
    <ul className="mt-2 mb-4 flex flex-col gap-2 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center">
      <NavListMenu />
      {navListItems.map(({ label, icon: Icon, to }) => (
        <Typography key={label} as={Link} to={to} variant="small" color="gray" className="font-VarelaRound font-medium text-blue-gray-500">
          <MenuItem className="flex items-center gap-2 lg:rounded-full">
            <Icon className="h-[18px] w-[18px]" />
            <span className="text-gray-900">{label}</span>
          </MenuItem>
        </Typography>
      ))}
    </ul>
  );
};

const ComplexNavbar = () => {
  const [isNavOpen, setIsNavOpen] = useState(false);

  const toggleIsNavOpen = () => setIsNavOpen(prevState => !prevState);

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 960) {
        setIsNavOpen(false);
      }
    };
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <Navbar className="mx-auto max-w-screen-xl p-2 lg:rounded-full lg:pl-6">
      <div className="relative mx-auto flex items-center justify-between text-blue-gray-900 flex-col lg:flex-row lg:items-center">
        <img
          src="https://i.imgur.com/TOarfx0.png"
          alt="Logo"
          style={{ width: "50px", marginRight: "0" }} // Adjust margin-right as needed
        />
        <Typography
          as={Link}
          to="/"
          className="cursor-pointer py-1.5 font-VarelaRound text-2xl tracking-tighter lg:ml-4" // Adjust left margin for larger screens
        >
          PRECISE PICKS
        </Typography>
        <div className="hidden lg:flex flex-grow items-center justify-center">
          <NavList />
        </div>
        <IconButton
          size="sm"
          color="blue-gray"
          variant="text"
          onClick={toggleIsNavOpen}
          className="ml-auto mr-2 lg:hidden"
        >
          <Bars2Icon className="h-6 w-6" />
        </IconButton>
      </div>
      <MobileNav open={isNavOpen} className="overflow-scroll">
        <NavList />
      </MobileNav>
    </Navbar>
  );
};

export default ComplexNavbar;

