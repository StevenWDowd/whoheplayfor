interface PlayerInterface{
  name: string,
  imageURL: string,
  team: string,
  season: string,
}

function checkAnswer(teamAnswer:string, player: PlayerInterface): boolean {
  return (teamAnswer === player.team ? true : false);
}

export {type PlayerInterface};