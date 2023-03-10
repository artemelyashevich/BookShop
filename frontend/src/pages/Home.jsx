import React, { useState } from "react";
import "./static/home.css";

function Home() {
  const [book, setBook] = useState();

  function getBook() {
    fetch("http://127.0.0.1:5000//book/1", {
      method: "Get",
    })
      .then((response) => response.json())
      .then((data) => {
        setBook(data["img"]);
        console.log(book);
      });
  }

  return (
    <>
      <div className="wrapper">
        <div className="con">
          
        </div>
      </div>
    </>
  );
}

export default Home;
