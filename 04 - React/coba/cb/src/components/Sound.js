import useSound from 'use-sound'
import audio1 from './../Audio/audio1.mp3'

export default function Sound() {
    
    const [play] = useSound(audio1, { volume: 0.5 } );
    
    return (
        <button onClick={play}>
            Press the Button! 💖
        </button>
    )
}