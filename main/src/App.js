import React, { Component } from 'react';
import logo from './assets/logo.png';
import './style/App.css';
import {
    BrowserRouter as Router,
    Route,
    Link
} from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <router>
      <div class="flex_center">
      <img src={logo} class="logo" />
      <p class="fs_step" > To start, please login to your Spotify account. </p>
      <p class="fs_step" > Choose your desired playlist.</p>
      </div>
      </router>
    );
  }
}

export default App;
