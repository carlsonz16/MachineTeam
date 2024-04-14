import React, { useState } from 'react';
import PlayerDropdown from './PlayerDropdown';
import SelectButton from './SelectButton';

const players = [
  { id: 1, name: 'Player 1' },
  { id: 2, name: 'Player 2' },
  { id: 3, name: 'Player 3' },
  // Add more players as needed
];

const PlayerSelectionPage = () => {
  const [selectedPlayer, setSelectedPlayer] = useState('');

  const handleSelect = (player) => {
    setSelectedPlayer(player);
  };

  return (
    <div className="container mx-auto mt-8">
      <h1 className="text-2xl font-bold mb-4">Select a Player</h1>
      <PlayerDropdown players={players} onSelect={handleSelect} />
      <div className="mt-4">
        <SelectButton disabled={!selectedPlayer} />
      </div>
    </div>
  );
};

export default PlayerSelectionPage;
