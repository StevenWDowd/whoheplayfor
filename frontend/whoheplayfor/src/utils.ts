const BASE_URL = 'http://127.0.0.1:5000';

interface PlayerInterface{
  name: string,
  imageURL: string,
  team: string,
  season: string,
}

function checkAnswer(teamAnswer:string, player: PlayerInterface): boolean {
  return (teamAnswer === player.team ? true : false);
}

async function generateQuestionData(): Promise<PlayerInterface>{
  const res = await fetch(`${BASE_URL}/player`);
  const player = await res.json();
  return player;
}

export {type PlayerInterface, generateQuestionData, checkAnswer};