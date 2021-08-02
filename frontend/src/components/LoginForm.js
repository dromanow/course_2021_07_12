import React from 'react'
//import axios from 'axios'
//import logo from './logo.svg';
//import './App.css';
//import AuthorList from './components/Authors.js'
//import BookList from './components/Books.js'
//import AuthorBooksList from './components/AuthorBooks.js'
//import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

//const Page404 = ({location}) => {
//    return <div>
//        Page {location.pathname} not found.
//    </div>
//}


class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'login': '',
            'password': ''
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name] : event.target.value
        })
    }

    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <input type="text" name="login" placeholder="login" value={this.state.login} onChange={(event)=>this.handleChange(event)} />
                <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event)=>this.handleChange(event)} />
                <input type="submit" value="Login" />
            </form>
        )
    }
}

export default LoginForm
