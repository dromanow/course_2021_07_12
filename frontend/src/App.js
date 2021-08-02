import React from 'react'
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Authors.js'
import BookList from './components/Books.js'
import AuthorBooksList from './components/AuthorBooks.js'
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'

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
            'books': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
        .then(
            response => {
                const authors = response.data
                this.setState({
                    'authors': authors
                })
            }
        ).catch(
            error => console.log(error)
        )

        axios.get('http://127.0.0.1:8000/api/books/')
        .then(
            response => {
                const books = response.data
                this.setState({
                    'books': books
                })
            }
        ).catch(
            error => console.log(error)
        )
    }

// http://localhost:3000/books

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
                </ul>
            </nav>
            <Switch>
                <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                <Route exact path='/books' component={() => <BookList books={this.state.books} authors={this.state.authors} />} />
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
