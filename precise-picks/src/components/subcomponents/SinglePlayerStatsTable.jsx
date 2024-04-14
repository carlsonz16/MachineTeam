import React, { useState, useMemo } from 'react';
import teamLogos from '../teamLogos';

const SinglePlayerStatsTable = ({ stats }) => {
  // State for toggling between per game stats and total stats
  const [perGame, setPerGame] = useState(false);

  // Memoized stats to display based on the toggled state
  const statsToDisplay = useMemo(() => {
    const resultSet = stats.resultSets.find(dict => dict.name === "SeasonTotalsRegularSeason");
    const headersToRemove = ['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID', 'REB', 'PF'];

    // Calculate indexes to remove
    const indexesToRemove = resultSet.headers.reduce((acc, header, index) => {
      if (headersToRemove.includes(header)) {
        acc.push(index);
      }
      return acc;
    }, []);
    
    // Transform rowSet arrays
    const newRowSet = resultSet.rowSet.map(row => {
      const newRow = {};
      resultSet.headers.forEach((header, index) => {
        if (!indexesToRemove.includes(index)) {
          // Check if per game toggle is active and the stat should be divided by GP
          if (perGame && header !== 'SEASON_ID' && header !== 'TEAM_ABBREVIATION' && !header.includes('PCT') && header !== 'GP') {
            const perGameValue = parseFloat((row[index] / row[resultSet.headers.indexOf('GP')]).toFixed(1));
            newRow[header] = perGameValue;
          } else {
            newRow[header] = row[index];
          }
        }
      });
      return newRow;
    });
    
    // Adjust headers
    const newHeaders = resultSet.headers.filter(header => !headersToRemove.includes(header));
    
    return {
      ...resultSet,
      headers: newHeaders,
      rowSet: newRowSet,
    };
  }, [stats, perGame]);

  // Handler for toggling between per game and total stats
  const handlePerGameToggle = () => {
    setPerGame(!perGame);
  };

  return (
    <>
      <div>
        <label>
          <input
            type="checkbox"
            checked={perGame}
            onChange={handlePerGameToggle}
          />
          Per Game Stats
        </label>
      </div>
      <table className="table-auto w-full">
        <thead>
          <tr>
            <th className="text-left">Year</th>
            <th className="text-left">Team</th>
            <th className="text-left">GP</th>
            <th className="text-left">MIN</th>
            <th className="text-left">PTS</th>
            <th className="text-left">AST</th>
            <th className="text-left">TOV</th>
            <th className="text-left">BLK</th>
            <th className="text-left">STL</th>
            <th className="text-left">FGM</th>
            <th className="text-left">FG%</th>
            <th className="text-left">FG3M</th>
            <th className="text-left">FG3%</th>
            <th className="text-left">FTM</th>
            <th className="text-left">FT%</th>
            <th className="text-left">OREB</th>
            <th className="text-left">DREB</th>
            {/* Add more columns as needed */}
          </tr>
        </thead>
        <tbody>
          {statsToDisplay.rowSet.slice().reverse().map((stat, index) => (
            <tr key={index} className={index % 2 === 0 ? 'bg-gray-100' : 'bg-white'}>
              <td>{stat.SEASON_ID}</td>
              <td className="flex items-center">
                <span className="mr-2">{stat.TEAM_ABBREVIATION}</span>
                <img 
                  src={teamLogos[stat.TEAM_ABBREVIATION]} 
                  alt={`${stat.TEAM_ABBREVIATION} logo`} 
                  className="w-6 align-middle"
                />
              </td>
              <td>{stat.GP}</td>
              <td>{stat.MIN}</td>
              <td>{stat.PTS}</td>
              <td>{stat.AST}</td>
              <td>{stat.TOV}</td>
              <td>{stat.BLK}</td>
              <td>{stat.STL}</td>
              <td>{stat.FGM}</td>
              <td>{stat.FG_PCT}</td>
              <td>{stat.FG3M}</td>
              <td>{stat.FG3_PCT}</td>
              <td>{stat.FTM}</td>
              <td>{stat.FT_PCT}</td>
              <td>{stat.OREB}</td>
              <td>{stat.DREB}</td>
              {/* Add more data cells as needed */}
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default SinglePlayerStatsTable;
