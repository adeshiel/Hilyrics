import React, { Component } from 'react';
import logo from './assets/logo.png';
import './style/App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: "",
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

          <div class="form_container">
            <form class="flex_center" onSubmit={this.Login}>

              <label>
                Username: &nbsp;
                <input type="Password" name="name" value={this.state.email}/>
              </label>

                <input type="submit" value="Login"/>
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
