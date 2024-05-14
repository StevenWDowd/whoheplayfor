import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import GameHome from './GameHome'

function App() {
  //const [player, setPlayer] = useState();

  return (
    <>
    <div className='App'>
      <GameHome></GameHome>
    </div>
    </>
  )
}

export default App
