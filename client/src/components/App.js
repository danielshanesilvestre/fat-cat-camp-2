import React, { useEffect, useState } from "react";
import { Outlet } from "react-router";
import NavBar from "./NavBar";


function App() {
  return <>
    <header>
      <NavBar />
    </header>
    <main>
      <h1>Project Client</h1>
      <Outlet context={{}} />
    </main>
  </>
}

export default App;
