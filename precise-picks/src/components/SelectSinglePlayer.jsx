import React, { useState } from 'react';
import { Link } from 'react-router-dom';


const SelectButton = ({ disabled }) => {
    return (
      <Link
        to="/selected-player"
        className={`bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${
          disabled && 'opacity-50 cursor-not-allowed'
        }`}
      >
        Select
      </Link>
    );
  };

const PlayerDropdown = ({ players, onSelect }) => {
  const [selectedPlayer, setSelectedPlayer] = useState('');

  const handleSelect = (player) => {
    setSelectedPlayer(player);
    onSelect(player);
  };

  return (
    <div className="relative inline-block">
      <select
        value={selectedPlayer}
        onChange={(e) => handleSelect(e.target.value)}
        className="block appearance-none bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
      >
        <option value="">Select a player</option>
        {players.map((player) => (
          <option key={player.id} value={player.name}>
            {player.name}
          </option>
        ))}
      </select>
      <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
        <svg
          className="fill-current h-4 w-4"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <path
            fillRule="evenodd"
            d="M9.293 13.707a1 1 0 011.414 0l5 5a1 1 0 01-1.414 1.414l-4.293-4.293a1 1 0 00-1.414 0L3.293 20.121a1 1 0 01-1.414-1.414l5-5a1 1 0 011.414 0zM4 8a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1z"
            clipRule="evenodd"
          />
        </svg>
      </div>
    </div>
  );
};

export default PlayerDropdown;
