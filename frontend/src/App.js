import React from 'react'
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Authors.js'
import BookList from './components/Books.js'
import AuthorBooksList from './components/AuthorBooks.js'
import LoginForm from './components/LoginForm.js'
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import Cookies from 'universal-cookie'


const Page404 = ({location}) => {
    return <div>
        Page {location.pathname} not found.
    </div>
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }

    is_auth() {
        return !!this.state.token
    }

    get_token_from_storage() {
        const cookie = new Cookies()
        this.setState({'token': cookie.get('token')}, this.get_data)
    }

    get_headers() {
        let header = {
            'Content-Type': 'application/json'
        }
        const cookie = new Cookies()
//        cookie.set('token', response.data.token)
//                console.log(cookie.get('token'))

        header['Authorization'] = 'Token ' + cookie.get('token')

        return header;
    }

    get_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
        .then(
            response => {
                const authors = response.data
                this.setState({
                    'authors': authors
                })
            }
        ).catch(
            error => {
                this.setState({
                    'authors': []
                })
                console.log(error)
            }
        )

        axios.get('http://127.0.0.1:8000/api/books/', {headers})
        .then(
            response => {
                const books = response.data
                this.setState({
                    'books': books
                })
            }
        ).catch(
            error => {
                this.setState({
                    'books': []
                })
                console.log(error)
            }
        )
    }

    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/',
        {
            "username": login,
            "password": password
        })
        .then(
            response => {
                const cookie = new Cookies()
                cookie.set('token', response.data.token)
                this.setState({'token': response.data.token}, this.get_data)
//                this.get_data()
//                console.log(cookie.get('token'))
            }
        ).catch(
            error => console.log(error)
        )
    }

    logout() {
        const cookie = new Cookies()
        cookie.set('token', '')
        this.setState({'token': ''}, this.get_data)
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
        <div>
            <HashRouter>
            <nav>
                <ul>
                    <li>
                        <Link to='/'>Authors</Link>
                    </li>
                    <li>
                        <Link to='/books'>Books</Link>
                    </li>
                    <li>
                        {this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link> }
                    </li>
                </ul>
            </nav>
            <Switch>
                <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                <Route exact path='/books' component={() => <BookList books={this.state.books} authors={this.state.authors} />} />
                <Route exact path='/login' component={() => <LoginForm get_token={(login, password) => this.get_token(login, password)} />} />
                <Redirect from='/authors' to='/' />
                <Route path='/author/:id'>
                    <AuthorBooksList books={this.state.books} />
                </Route>
                <Route component={Page404} />
            </Switch>
            </HashRouter>
        </div>
        )
    }
}

export default App;
