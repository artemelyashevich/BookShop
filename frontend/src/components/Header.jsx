import React from 'react'
import { NavLink, Link } from "react-router-dom";

function Header() {
  return (
    <>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <Link className='navbar-brand' to={"/"}>BookShop</Link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <NavLink className='nav-link' to={"/"}>Home</NavLink>
        </li>
        <li class="nav-item">
          <NavLink className='nav-link' to={"/about"}>About</NavLink>
        </li>
        <li class="nav-item">
          <NavLink className='nav-link' to={"/books"}>Books</NavLink>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
    </>
  )
}

export default Header