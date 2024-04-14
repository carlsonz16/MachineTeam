import React, { useState, useEffect } from 'react';
import { LineChart } from '@mui/x-charts/LineChart';
import CircularProgress from '@mui/material/CircularProgress';

const SinglePlayerStatsGraph = ({ playerName }) => {
  const [selectedStat, setSelectedStat] = useState('PTS');
  const [graphData, setGraphData] = useState({ xAxis: [], series: [] });
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchPlayerStats = async () => {
      setIsLoading(true);
      try {
        const response = await fetch(`/api/single-players-stats-graph?player=${playerName}&stat=${selectedStat}`);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        const xAxisData = Object.keys(data);
        const seriesData = Object.values(data).map(value => Number(value) || 0);

        setGraphData({
          xAxis: [{ scaleType: 'point', data: xAxisData }],
          series: [{ data: seriesData }],
        });
      } catch (error) {
        console.error("Failed to fetch player stats:", error);
      } finally {
        setIsLoading(false);
      }
    };

    if (playerName) {
      fetchPlayerStats();
    }
  }, [playerName, selectedStat]);

  const handleStatChange = (e) => {
    setSelectedStat(e.target.value);
  };

  return (
    <div className="relative w-full max-w-[500px]">
      {isLoading && (
        <div className="absolute top-0 left-0 right-0 bottom-0 flex justify-center items-center bg-black bg-opacity-50 text-white z-10">
          <CircularProgress color="inherit" />
        </div>
      )}
      <div className={`${isLoading ? 'opacity-50' : 'opacity-100'}`}>
        <select onChange={handleStatChange} value={selectedStat} className="mb-4 rounded-md px-3 py-2 border border-gray-300 focus:outline-none focus:border-blue-500">
          <option value="PTS">Points</option>
          <option value="REB">Rebounds</option>
          <option value="AST">Assists</option>
        </select>
        <LineChart
          xAxis={graphData.xAxis}
          series={graphData.series}
          width={500}
          height={300}
        />
      </div>
    </div>
  );
};

export default SinglePlayerStatsGraph;
