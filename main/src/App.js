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

          userName = "";
          password = "";

          <div class="form_container">
            <form class="flex_center" onSubmit={this.Login(userName.state.value, password.state.value)}>
              <label>
                Username:
                <input type="text" name="name" />
              </label>
              <label>
                Password:
                <input type="Password" name="name" value={userName.state.value}/>
              </label>

                <input type="submit" value="Login" value={password.state.value}/>
            </form>

            <Route path='/' component={Login}/>

          </div>
        </div>
      </Router>
    );
  }

}

class Login extends Component{

  Username(user, pass){

  }

  render() {
        return (...);
  }

}


export default App;
