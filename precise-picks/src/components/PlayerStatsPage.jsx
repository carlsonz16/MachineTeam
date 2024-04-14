import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom

const PlayerStatsPage = () => {
  const [playerStats, setPlayerStats] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [perGame, setPerGame] = useState(true);
  const [sortField, setSortField] = useState('PTS');
  const [sortDirection, setSortDirection] = useState('desc');
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedSeason, setSelectedSeason] = useState('2023-24');
  const itemsPerPage = 25;

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const first = (currentPage - 1) * itemsPerPage + 1;
        const last = first + itemsPerPage - 1;
        const url = `/api/players-stats?season=${selectedSeason}&stat=${sortField}&first=${first}&last=${last}&per_game=${perGame}&sort_direction=${sortDirection}`;
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setPlayerStats(data);
      } catch (error) {
        console.error('Error fetching data:', error);
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [selectedSeason, perGame, sortField, sortDirection, currentPage]);

  const handleToggle = () => {
    setPerGame(!perGame);
  };

  const handleHeaderClick = (field) => {
    if (sortField === field) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortDirection('asc');
    }
  };

  const renderSortHeader = (backendField, frontendLabel) => {
    return (
      <th
        onClick={() => handleHeaderClick(backendField)}
        className="cursor-pointer whitespace-nowrap"
      >
        {frontendLabel} {sortField === backendField && (sortDirection === 'asc' ? '↑' : '↓')}
      </th>
    );
  };

  const handleNextPage = () => {
    setCurrentPage(currentPage + 1);
  };

  const handlePreviousPage = () => {
    setCurrentPage((prevPage) => Math.max(prevPage - 1, 1));
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading player stats!</div>;

  return (
    <div className="m-5 font-VarelaRound">
      <h1 className="text-3xl font-bold mb-4">NBA Player Stats</h1>
      <div className="mb-4">
        <label htmlFor="season-selector" className="mr-2">Select Season:</label>
        <select
          id="season-selector"
          value={selectedSeason}
          onChange={(e) => setSelectedSeason(e.target.value)}
          className="form-select"
        >
          {seasonOptions.map((season) => (
            <option key={season} value={season}>
              {season}
            </option>
          ))}
        </select>
      </div>
      <div className="flex items-center mb-4">
        <input type="checkbox" checked={perGame} onChange={handleToggle} className="form-checkbox mr-2" />
        <label htmlFor="per-game-toggle">Per Game Stats</label>
      </div>
      {/* Key for the statistical data */}
      <div className="border rounded-lg shadow-md p-4 mb-8">
        <h2 className="text-xl font-semibold mb-2">Key</h2>
        <div className="grid grid-cols-3 gap-4">
          <div>
            <p><strong>GP:</strong> Games Played</p>
            <p><strong>MIN:</strong> Minutes Played</p>
            <p><strong>PTS:</strong> Points</p>
            <p><strong>AST:</strong> Assists</p>
            <p><strong>TOV:</strong> Turnovers</p>
          </div>
          <div>
            <p><strong>BLK:</strong> Blocks</p>
            <p><strong>STL:</strong> Steals</p>
            <p><strong>FGM:</strong> Field Goals Made (includes both 2 pointers and 3 pointers)</p>
            <p><strong>FG%:</strong> Field Goal Percentage</p>
            <p><strong>FG3M:</strong> Three-Point Field Goals Made</p>
          </div>
          <div>
            <p><strong>FTM:</strong> Free Throws Made</p>
            <p><strong>FT%:</strong> Free Throw Percentage</p>
            <p><strong>OREB:</strong> Offensive Rebounds</p>
            <p><strong>DREB:</strong> Defensive Rebounds</p>
          </div>
        </div>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full table-auto mb-4">
          <thead>
            <tr>
              <th className="px-4 py-2">Rank</th>
              <th className="px-4 py-2">Player</th>
              {renderSortHeader('GP', 'GP')}
              {renderSortHeader('MIN', 'MIN')}
              {renderSortHeader('PTS', 'PTS')}
              {renderSortHeader('FGM', 'FGM')}
              {renderSortHeader('FGA', 'FGA')}
              {renderSortHeader('FG_PCT', 'FG%')}
              {renderSortHeader('FG3M', '3PM')}
              {renderSortHeader('FG3A', '3PA')}
              {renderSortHeader('FG3_PCT', '3P%')}
              {renderSortHeader('FTM', 'FTM')}
              {renderSortHeader('FTA', 'FTA')}
              {renderSortHeader('FT_PCT', 'FT%')}
              {renderSortHeader('AST', 'AST')}
              {renderSortHeader('STL', 'STL')}
              {renderSortHeader('BLK', 'BLK')}
              {renderSortHeader('REB', 'REB')}
            </tr>
          </thead>
          <tbody>
            {playerStats.map((player, index) => (
              <tr key={index} className={index % 2 === 0 ? 'bg-gray-100' : ''}>
                <td className="px-4 py-2">{player.RANK}</td>
                <td className="px-4 py-2">
                <Link 
                      to={`/players/${player.PLAYER_NAME}`} // Pass player name as URL parameter
                      className="hover:text-blue-900 bold" // Apply blue color on hover
                    >
                      {player.PLAYER_NAME}
                    </Link>
                </td>
                <td className="px-4 py-2">{player.GP}</td>
                <td className="px-4 py-2">{player.MIN}</td>
                <td className="px-4 py-2">{player.PTS}</td>
                <td className="px-4 py-2">{player.FGM}</td>
                <td className="px-4 py-2">{player.FGA}</td>
                <td className="px-4 py-2">{player.FG_PCT}</td>
                <td className="px-4 py-2">{player.FG3M}</td>
                <td className="px-4 py-2">{player.FG3A}</td>
                <td className="px-4 py-2">{player.FG3_PCT}</td>
                <td className="px-4 py-2">{player.FTM}</td>
                <td className="px-4 py-2">{player.FTA}</td>
                <td className="px-4 py-2">{player.FT_PCT}</td>
                <td className="px-4 py-2">{player.AST}</td>
                <td className="px-4 py-2">{player.STL}</td>
                <td className="px-4 py-2">{player.BLK}</td>
                <td className="px-4 py-2">{player.REB}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="flex justify-between">
        <button onClick={handlePreviousPage} className="px-4 py-2 bg-gray-200 hover:bg-gray-300">← Previous Page</button>
        <button onClick={handleNextPage} className="px-4 py-2 bg-gray-200 hover:bg-gray-300">Next Page →</button>
      </div>
    </div>
  );
};

const seasonOptions = [
  "2023-24", "2022-23", "2021-22", "2020-21", "2019-20", 
  "2018-19", "2017-18", "2016-17", "2015-16", "2014-15", 
  "2013-14", "2012-13", "2011-12", "2010-11", "2009-10", 
  "2008-09", "2007-08", "2006-07", "2005-06", "2004-05"
];

export { PlayerStatsPage };
