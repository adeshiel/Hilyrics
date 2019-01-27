import React, { Component } from 'react';
import logo from './assets/logo.png';
import './style/App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <div class="flex_center">
            <img src={logo} class="logo" />
            <p class="fs_step" > To start, please login to your Spotify account. </p>
          </div>

          <div class="form_container">
            <form class="flex_center">
              <label>
                Username:
                <input type="text" name="name" />
              </label>
              <label>
                Password:
                <input type="Password" name="name" />
              </label>
                <input type="submit" value="Login" />
            </form>

            <Route path='/' component={Playlist}/>

          </div>
        </div>
      </Router>
    );
  }

}

class Playlist extends Component{



  render() {
        return (...);
  }
  
}


export default App;
