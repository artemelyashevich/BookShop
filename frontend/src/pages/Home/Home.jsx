import React, { useState } from "react";
import "./home.css";
import Items from "../../components/Items"

function Home() {
  return (
    <>
      <div className="wrapper">
        <div className="con">
          <Items />
        </div>
      </div>
    </>
  );
}

export default Home;
