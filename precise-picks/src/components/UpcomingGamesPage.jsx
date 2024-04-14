import { useState, useEffect } from 'react';
import teamLogos from './teamLogos';
import * as Papa from 'papaparse';

const fetchCurrentGames = async () => {
  const apiUrl = '/api/predictions-games';
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`Network response was not ok, status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('There has been a problem with your fetch operation:', error.message);
    return [];
  }
};

const PreGamePredictionExplanation = () => (
  <div className="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 mb-4 rounded" role="alert">
    <p className="font-bold">How the "Pre-game Prediction" AI Model Works:</p>
    <p className="text-sm">
      Our AI Model processes historical NBA game data to predict future game outcomes using a RidgeClassifier model. Initially, it cleans and prepares the data, sorting by date and removing irrelevant columns. It then generates a 'target' column to represent future game outcomes, applying group-specific calculations to account for team performance trends. Feature engineering includes scaling numeric data and handling categorical variables. The model uses Sequential Feature Selector with time series cross-validation to identify significant predictors. It undergoes backtesting, where the model is trained on historical data and tested on subsequent seasons to ensure predictive reliability. Model accuracy is evaluated, and final predictions are merged with game information to provide context-rich insights. This workflow embodies a comprehensive approach to predictive analytics in sports, leveraging machine learning for data-driven decision-making.
    </p>
  </div>
);

const UpcomingGamesPage = () => {
  const [data, setData] = useState([]);
  const [bettingLines, setBettingLines] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [predictionsData, setPredictionsData] = useState([]);

  useEffect(() => {
    fetchCurrentGames().then(gamesData => {
      setData(gamesData);
      setIsLoading(false);
    });

    fetch('/src/components/matchups.csv')
      .then(response => response.text())
      .then(responseText => {
        Papa.parse(responseText, {
          header: true,
          complete: (results) => {
            setPredictionsData(results.data); // Store the parsed data in state
          }
        });
      });
  }, []);

  const getPredictionFromData = (team1, team2) => {
    const predictionRow = predictionsData.find(row => 
      (row['Team_x'] === team1 && row['Team_y'] === team2) ||
      (row['Team_x'] === team2 && row['Team_y'] === team1)
    );
    return predictionRow ? predictionRow['Prediction'] : 'No prediction found';
  };

  useEffect(() => {
   const fetchData = async () => {
     setIsLoading(true);
     try {
       const today = new Date();
       const selectedDateUTC = today.toISOString().split('T')[0];
       const gamesUrl = `/api/current-games?date=${selectedDateUTC}`;
       const gamesResponse = await fetch(gamesUrl);
       if (!gamesResponse.ok) throw new Error('Data could not be fetched!');
       const gamesData = await gamesResponse.json();
       
       // Only update the games data if it actually contains games
       if (Array.isArray(gamesData) && gamesData.length > 0) {
         setData(gamesData);
       }
 
       const bettingLinesUrl = `/api/betting-lines`;
       const bettingLinesResponse = await fetch(bettingLinesUrl);
       if (!bettingLinesResponse.ok) throw new Error('Betting lines data could not be fetched!');
       const linesData = await bettingLinesResponse.json();
       // Ensure linesData is not null and is an array
       setBettingLines(Array.isArray(linesData) ? linesData : []);
 
     } catch (error) {
       console.error("Error fetching data:", error);
       // Consider setting an error state here to display a message to the user
     } finally {
       setIsLoading(false);
     }
   };
 
   fetchData();
 }, []);

  // Utility function to get the last word of a team's full name
  const getLastWord = (fullName) => {
    const words = fullName.trim().split(" ");
    return words[words.length - 1];
  };

  return (
    <div className="m-5 w-auto font-VarelaRound">
      <h1 className="text-3xl font-bold mb-4">Upcoming Games</h1>
      <PreGamePredictionExplanation />
      {isLoading ? (
        <div className="animate-pulse">
          <p className="text-gray-600 mb-4">Loading games...</p>
        </div>
      ) : data.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-4 gap-4 justify-center">
          {data.map((game, index) => {
             const awayTeamBettingLine = bettingLines.find(line => getLastWord(line['participant full name']) === game.awayTeam);
             const homeTeamBettingLine = bettingLines.find(line => getLastWord(line['participant full name']) === game.homeTeam);
            const prediction = getPredictionFromData(game.homeTeam, game.awayTeam);
            const predictedTeamLogo = teamLogos[prediction];
            return (
              <div key={index} className="rounded-lg overflow-hidden shadow-lg bg-white p-6 text-center">
                <div className="flex justify-between mb-4">
                  <div>
                    <img src={teamLogos[game.awayTeam]} alt={`${game.awayTeam} logo`} className="inline-block h-8 w-8 mx-2" />
                    <span className="font-semibold">{game.awayTeam}</span>
                  </div>
                  <div>
                    <span className="font-semibold">at</span>
                  </div>
                  <div>
                    <img src={teamLogos[game.homeTeam]} alt={`${game.homeTeam} logo`} className="inline-block h-8 w-8 mx-2" />
                    <span className="font-semibold">{game.homeTeam}</span>
                  </div>
                </div>
                <p className="text-gray-700 text-base mb-2">Time: {new Date(game.gameTimeLTZ).toLocaleString()}</p>
                <p className="text-gray-700 text-base mb-2">Status: {game.gameStatusText}</p>
                <p className="text-gray-700 text-base mb-2">Score: {game.awayTeam}: {game.awayTeamScore} - {game.homeTeam}: {game.homeTeamScore}</p>
                <p className="mb-1">Moneyline for {game.awayTeam}: {awayTeamBettingLine ? awayTeamBettingLine['american odds'] : 'N/A'}</p>
                <p className="mb-1">Moneyline for {game.homeTeam}: {homeTeamBettingLine ? homeTeamBettingLine['american odds'] : 'N/A'}</p>
                <div className="border border-gray-300 p-2">
                  <h2 className="font-bold mb-1">Pre-game Prediction:</h2>
                  <div className="flex items-center justify-center rounded-lg p-2">
                    {predictedTeamLogo && <img src={predictedTeamLogo} alt={`${prediction} logo`} className="inline-block h-8 w-8 mx-2" />}
                    <p className="font-bold">{prediction}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      ) : (
        <p>No games today.</p>
      )}
    </div>
  );
};

export { UpcomingGamesPage };
