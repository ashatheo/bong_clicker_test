import './App.css'
import carrot from '../assets/carrot.png'
import { useState, useEffect } from 'react'
import request from '../api/request'

function App() {
  const [counter, setCounter] = useState<number>(0)
  
  function clickHandle() {
    setCounter(prev => prev +1)
    localStorage.setItem('counter', counter.toString())
  }

  useEffect(() => {
    async function getClicks() {
      const response = await request("get-clicks")
      
    }

    getClicks()
  },[])

  return (
    <>
    <span>{counter}</span>
    <div className='box'>
      
      <img src={carrot} alt="Carrot" className="foreground" width={256} height={256} onClick={clickHandle} />
      <img src={carrot} alt="Carrot" className="background" width={256} height={256}  />
    </div></>
  )
}

export default App
