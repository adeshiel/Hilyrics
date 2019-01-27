import React, { Component } from 'react';
import logo from './assets/logo.png';
import './style/App.css';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class App extends Component {
    render() {
        return (
            <Router>
                <div>
                    <Route path='/' component={Application}/>

                </div>
            </Router>
        )
    }
}


class Application extends Component {

  constructor(props) {
    super(props);

    this.state = {
      email: "",
      song: ""
    }
    this.setData = this.setData.bind(this);
    this.changeSubject = this.changeSubject.bind(this);
  }

  setData(text) {
        let r = text;
        console.log(r);
        this.setState({
            "song":r,
          });

    }


  changeSubject(username) {
      this.setState({
          'username': username,
      });

      fetch("http://localhost:5000/" + username)
          .then(resp => this.setState({
            "song:": resp,
            })
          )
          // .then(resp => resp.json())
          // .then(json => {
          //     let r = json;
          //     this.setData(r);
          // });
  }

  render() {
    return (

        <div>
          <div class="flex_center">
            <img src={logo} class="logo" />
            <p class="fs_step" > To start, please login to your Spotify account. </p>
          </div>


          <div class="form_container">

              <UsernameBox changeSubject={this.changeSubject}/>

              <h3> {this.state.song} </h3>



          </div>
        </div>

    );
  }

}

class UsernameBox extends Component {
    constructor(props) {
        super(props);
        this.state = {
            "username": "",
        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.changeSubject(this.state.username);
    }

    handleInputChange(event) {
        this.setState({
            "username": event.target.value,
        });
    }

    render() {
        return (<div >
            <form onSubmit={this.handleSubmit} style={{flex: 1}}>

                    <input placeholder="@" value={this.state.username} onChange={this.handleInputChange} style={{
                        color: 'black',
                        fontSize: 30,
                        marginTop: 10,
                    }}/>
                </form>
        </div>);
      }
    }





// class Login extends Component{
//
//   render() {
//     return(
//       fetch("http://localhost:3000/");
//     )
//   }
//
// }


export default App;
