import React, { Component } from 'react';
import logo from './assets/logo.png';
import './style/App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: ""
    }
  }

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
            <form class="flex_center" onSubmit={this.Login}>
              <label>
                Username:
                <input type="text" name="name" />
              </label>
              <label>
                Password:
                <input type="Password" name="name" value={this.state.user}/>
              </label>

                <input type="submit" value="Login" value={this.state.pass}/>
            </form>

            <Route path='/' component={Login}/>

          </div>
        </div>
      </Router>
    );
  }

}

class Login extends Component{

  render() {
        return (3);
  }

}


export default App;
