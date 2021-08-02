import React from 'react'

const BookItem = ({book, authors}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.authors.map((authorId) => { return authors.find((author) => author.id == authorId ).last_name } )}</td>
        </tr>
    )
}

const BooksList = ({books, authors}) => {
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
            {books.map((book) => <BookItem book={book} authors={authors} />)}
        </table>
    )
}

export default BooksList
