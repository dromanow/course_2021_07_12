import React from 'react'


class BookForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '',
            'authors': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name] : event.target.value
        })
    }

    handleAuthorChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'authors' : []
            })
            return;
        }
        let authors = []
        for(let i=0; i < event.target.selectedOptions.length; i++) {
            authors.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'authors' : authors
        })
    }

    handleSubmit(event) {
        this.props.createBook(this.state.name, this.state.authors);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <input type="text" name="name" placeholder="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                <select multiple name="authors" onChange={(event)=>this.handleAuthorChange(event)} >
                    {this.props.authors.map((author) => <option value={author.id}>{author.first_name} {author.last_name}</option>)}
                </select>
                <input type="submit" value="Create" />
            </form>
        )
    }
}

export default BookForm
