import React from "react";
import { Link } from "react-router-dom";

function Footer() {
  return (
  <>
  <div class="container">
  <footer class="py-3 my-4">
    <ul class="nav justify-content-center border-bottom pb-3 mb-3">
      <li class="nav-item"><Link to={"/"} class="nav-link px-2 text-muted " color="white">Home</Link></li>
      <li class="nav-item"><Link to={"/about"} class="nav-link px-2 text-muted">About</Link></li>
      <li class="nav-item"><Link to={"/profile"} class="nav-link px-2 text-muted">Profile</Link></li>
      <li class="nav-item"><a href="/https://github.com/artemelyashevich" class="nav-link px-2 text-muted">GitHub</a></li>
    </ul>
    <p class="text-center text-muted">© 2023 Company, Inc</p>
  </footer>
</div>
  </>
  );
}

export default Footer;
