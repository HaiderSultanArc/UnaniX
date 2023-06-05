import {BrowserRouter, Route, Routes} from "react-router-dom";
import './App.css';
import CDSS from "./CDSS.tsx";
import Home from './Home.tsx';
import Treatments from "./Treatments.tsx";

function App() {
  return (
    <>
    <BrowserRouter>
    <Routes>
      <Route path='/' exact element={<Home />}></Route>
      <Route path='/CDSS' exact element={<CDSS />}></Route>
      <Route path='/Treatments' exact element={<Treatments />}></Route>
    </Routes>
    </BrowserRouter>
    <div className="App">
      
     
    </div>
    </>
  )
}

export default App
