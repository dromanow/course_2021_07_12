import React from 'react'
import { useParams } from 'react-router-dom'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const AuthorBooksList = ({books}) => {
    let { id } = useParams();
    let filtered_books = books.filter((book) => book.authors.includes(parseInt(id)));

    return (
        <table>
            <th>
                Id
            </th>
            <th>
                Name
            </th>
            <th>
                Authors
            </th>
            {filtered_books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default AuthorBooksList
