import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import SinglePlayerStatsTable from './subcomponents/SinglePlayerStatsTable';
import SinglePlayerStatsGraph from './subcomponents/SinglePlayerStatsGraph';
import teamLogos from './teamLogos';

const SinglePlayerPage = () => {
  const { playerName } = useParams();
  const [playerStats, setPlayerStats] = useState(null);

  useEffect(() => {
    const fetchPlayerStats = async () => {
      const url = `/api/single-players-stats?player=${encodeURIComponent(playerName)}`;

      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setPlayerStats(data);
      } catch (error) {
        console.error('Failed to fetch player stats:', error);
      }
    };

    fetchPlayerStats();
  }, [playerName]);

  return (
   <div className="container mx-auto px-4 py-8">
      <div className="flex items-center mb-4">
         {playerStats && 
            <img 
               src={teamLogos[playerStats.resultSets[0].rowSet[playerStats.resultSets[0].rowSet.length - 1][4]]} 
               alt={`${playerStats.resultSets[0].rowSet[playerStats.resultSets[0].rowSet.length - 1][4]} logo`}
               className="w-24 h-24 mr-4" // Adjust size and margin as needed
            />
         }
         <h1 className="text-3xl font-semibold">{playerName}</h1>
      </div>
      <div className="flex flex-wrap mb-8">
         <div className="w-full md:w-1/3 pr-4 mb-4 md:mb-0">
            <div className="border rounded-lg shadow-md p-4">
            <h2 className="text-xl font-semibold mb-2"></h2>
            {playerStats && <img src={playerStats.image_url} alt={playerName} />}
            </div>
         </div>
         <div className="w-full md:w-1/2">
            <div className="border rounded-lg shadow-md p-4">
            <h2 className="text-xl font-semibold mb-2">Last 30 Games</h2>
            <SinglePlayerStatsGraph playerName={playerName}/>
            </div>
         </div>
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
      <div className="border rounded-lg shadow-md p-4">
        <h2 className="text-xl font-semibold mb-2">Career Stats</h2>
        {playerStats ? <SinglePlayerStatsTable stats={playerStats} /> : <div>Loading...</div>}
      </div>
    </div>
  );
};
export { SinglePlayerPage };
