import { useState } from "react";
import barkley from './assets/whpf.jpg';

function GameHome(){
    const [isStarted, setIsStarted] = useState(false);
    const [player, setPlayer] = useState({});

    async function beginGame(){

    }


    return (
    isStarted ?
    <p>game stuff will happen here</p>
    :
    <div>
        <p>Think you can match NBA legend Charles Barkley?</p>
        <img src={barkley}></img>
        <button>Play</button>
    </div>

    // :
    // <p>Loading ...</p>
    );
}

export default GameHome