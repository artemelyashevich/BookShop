import { BrowserRouter, Routes, Route } from "react-router-dom"
import Layout from "./components/Layout"
import './App.css';
import Home from "./pages/Home/Home";
import About from "./pages/About/About";
import Books from "./pages/Books/Books";
import NotFound from "./pages/NotFound/NotFound";

function App() {
  return (
    <>

    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout/>} >
        <Route index element={<Home/>}/>
        <Route path="about" element={<About/>}/>
        <Route path="books" element={<Books/>}/>
        <Route path="*" element={<NotFound/>}/>
      </Route>
    </Routes>
    </BrowserRouter>

    </>
  );
}

export default App;
