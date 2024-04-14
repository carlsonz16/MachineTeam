import React, { useState, useEffect } from 'react';
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

const PlayByPlay = ({ plays }) => {
  return (
    <div className="overflow-auto max-h-32 mt-4 bg-gray-100 dark:bg-gray-700 p-2 text-sm text-gray-900 dark:text-gray-200">
      {plays.map((play, index) => (
        <div key={index} className="mb-1">
          {play}
        </div>
      ))}
    </div>
  );
};

const PreGamePredictionExplanation = () => (
   <div className="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 mb-4 rounded" role="alert">
     <p className="font-bold">How the "Pre-game Prediction" AI Model Works:</p>
     <p className="text-sm">
     Our predictions are generated by an advanced Long Short-Term Memory (LSTM) neural network, a type of machine learning model specifically designed to understand and forecast outcomes based on the sequential nature of game events. This model meticulously processes the scores of home and away teams, alongside the remaining game time, to identify underlying patterns. Utilizing PyTorch, a cutting-edge deep learning framework, our model undergoes rigorous training phases. It learns from a wealth of historical game data, adjusting and improving through a process called optimization, where it minimizes prediction errors over multiple iterations. This sophisticated technique ensures our predictions are both precise and reliable, offering you a deep dive into the future of games based on real-time data.
     </p>
   </div>
 );

 const PredictionsPage = () => {
   const [currentGames, setCurrentGames] = useState([]);
   const [predictionsData, setPredictionsData] = useState([]);
   const [predictionsResult, setPredictionsResult] = useState({});
   const [loadingStatus, setLoadingStatus] = useState('loading'); // 'loading', 'noGames', 'error', or 'loaded'
 
   useEffect(() => {
     fetchCurrentGames().then(data => {
       setCurrentGames(data);
       setLoadingStatus(data.length ? 'loaded' : 'noGames');
     }).catch(() => {
       setLoadingStatus('error');
     });
 
     fetch('/src/components/matchups.csv')
       .then(response => response.text())
       .then(responseText => {
         Papa.parse(responseText, {
           header: true,
           complete: (results) => {
             setPredictionsData(results.data);
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
 
   const getPrediction = async (gameId, homeTeam, awayTeam) => {
     const apiUrl = '/api/get-prediction';
     try {
       const response = await fetch(apiUrl, {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json',
         },
         body: JSON.stringify({ gameId, homeTeam }),
       });
       if (!response.ok) {
         throw new Error(`Network response was not ok, status: ${response.status}`);
       }
       const data = await response.json();
       setPredictionsResult(prev => ({
         ...prev,
         [gameId]: { homeTeam, awayTeam, scores: data, fetched: true }
       }));
     } catch (error) {
       console.error('There has been a problem with your fetch operation:', error.message);
       alert('Failed to get prediction');
     }
   };
 
   if (loadingStatus === 'loading') {
     return (
       <div className="flex justify-center items-center h-screen">
         <h1 className="text-3xl font-bold">Loading Current Games...</h1>
       </div>
     );
   }
   const content = loadingStatus === 'noGames' ? (
      <div className="flex justify-center items-center h-auto">
         <h1 className="text-3xl font-bold">Sorry, come back later when there’s a game on!</h1>
      </div>
    ) : (
      <div className="flex flex-wrap justify-center gap-4">
        {currentGames.map((game, index) => (
          <div key={index} className="w-full max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
            <div className="p-5">
              <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{game.homeTeam} vs {game.awayTeam}</h5>
              <PlayByPlay plays={game.playByPlayData} />
              <p>Pre-game Prediction: <strong>{getPredictionFromData(game.homeTeam, game.awayTeam)}</strong></p>
              <button className={`mt-4 px-4 py-2 text-white font-bold py-2 px-4 rounded ${predictionsResult[game.gameId]?.fetched ? 'bg-gray-500' : 'bg-blue-500 hover:bg-blue-700'}`} onClick={() => getPrediction(game.gameId, game.homeTeam, game.awayTeam)} disabled={predictionsResult[game.gameId]?.fetched}>
                Get Predicted Score
              </button>
              {predictionsResult[game.gameId]?.fetched && (
                <p className="mt-2">
                  Predicted Score - {game.homeTeam}: {predictionsResult[game.gameId].scores[0]}, {game.awayTeam}: {predictionsResult[game.gameId].scores[1]}
                </p>
              )}
            </div>
          </div>
        ))}
      </div>
    );
  
    return (
     <div className="font-VarelaRound p-4">
       <h1 className="text-3xl font-bold mb-4 text-left">Live Games</h1>
       <PreGamePredictionExplanation />
       {content}
     </div>
    );
  };
  
  export { PredictionsPage };

 

