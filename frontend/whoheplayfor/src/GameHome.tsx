import { useState } from "react";
import barkley from './assets/whpf.jpg';

function GameHome(){
    const [isStarted, setIsStarted] = useState(false);
    const [player, setPlayer] = useState({});

    return (
    isStarted ?
    <div>
        <p>Think you can match NBA legend Charles Barkley?</p>
        <img src={barkley}></img>
        <button>Play</button>
    </div>

    :
    <div></div>
    )
}

export default GameHome