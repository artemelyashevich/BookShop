import { BrowserRouter, Routes, Route } from "react-router-dom"
import Layout from "./components/Layout"
import './App.css';
import Home from "./pages/Home";
import About from "./pages/About";
import Books from "./pages/Books";

function App() {
  return (
    <>

    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout/>} >
        <Route index element={<Home/>}/>
        <Route path="about" element={<About/>}/>
        <Route path="books" element={<Books/>}/>
      </Route>
    </Routes>
    </BrowserRouter>

    </>
  );
}

export default App;
