import React, { useState } from "react";
import "./home.scss";
import Items from "../../components/Items";
import LeftBar from "../../components/LeftBar";

function Home() {
  return (
    <>
      <div className="wrapper">
        <div className="con">
          <LeftBar />
          <Items />
        </div>
      </div>
    </>
  );
}

export default Home;
