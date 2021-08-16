import React from 'react'

const BookItem = ({book, authors, deleteBook}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.authors.map((authorId) => {
                let author = authors.find((author) => author.id == authorId )
                if (author) {
                    return author.last_name
                }
            } )}
            </td>
            <td><button onClick={() => deleteBook(book.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const BooksList = ({books, authors, deleteBook}) => {
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
            {books.map((book) => <BookItem book={book} authors={authors} deleteBook={deleteBook} />)}
        </table>
    )
}

export default BooksList
