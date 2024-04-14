//import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ComplexNavbar from "./components/Navbar";
import {HomePage} from "./components/HomePage";
import {PlayerStatsPage} from "./components/PlayerStatsPage";
import {UpcomingGamesPage} from "./components/UpcomingGamesPage";
import {PredictionsPage} from "./components/PredictionsPage";
import {AboutPage} from "./components/AboutPage";
import { SinglePlayerPage } from './components/SinglePlayerPage';


function App() {
  return (
    <BrowserRouter>
      <ComplexNavbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upcoming-games" element={<UpcomingGamesPage />} />
        <Route path="/predictions" element={<PredictionsPage />} />
        <Route path="/player-stats" element={<PlayerStatsPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/players/:playerName" element={<SinglePlayerPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
