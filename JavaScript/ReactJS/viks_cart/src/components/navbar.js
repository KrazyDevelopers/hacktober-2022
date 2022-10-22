import React from 'react';

class Navbar extends React.Component {
  state = {};
  render() {
    return (
      <nav style={{backgroundColor:"#A85CF9"}} className="navbar navbar-expand-lg navbar-dark ">
        <div title="Navbar is not functional yet!" className="container-fluid">
          <a className="navbar-brand" href="#">
           <h2 id ="viklogo" className='me-3'>Vik's Cart</h2> 
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li id ="btnhover" className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">
                  Home
                </a>
              </li>
              <li id ="btnhover" className="nav-item">
                <a className="nav-link active" href="#">
                  Bestsellers
                </a>
              </li>
              <li id ="btnhover" className="nav-item">
                <a className="nav-link active" href="#">
                  Today's deal
                </a>
              </li>
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Category
                </a>
                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li>
                    <a className="dropdown-item" href="#">
                      Mobile phones
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Earphones
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Kitchen Electronics
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Laptops
                    </a>
                  </li>
                  <li>
                    <hr className="dropdown-divider" />
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Grocery
                    </a>
                  </li>
                </ul>
              </li>
            </ul>
            <form className="d-flex" role="search">
              <div id ="btnhover" className='me-3'>
              <input
                className="form-control me-3"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              </div>
              <div id ="btnhover">
              <button className="btn btn-outline-dark" type="submit">
                Search
              </button>
              </div>
            </form>
          </div>
        </div>  
      </nav>
    );
  }
}

export default Navbar;
