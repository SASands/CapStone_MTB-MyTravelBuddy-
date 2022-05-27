import React, { useState } from 'react';





// add form below that is one input "search" you will need to save its on change in a hook
// this will also need a button, type submit, this means form needs on submit setup
// on submit should call getSearchResults and pass in the value from the hook string are input value

const SearchBar = (props) => {
    const [searchRequest, setSearchRequest] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(searchRequest)
        props.getSearchResults(searchRequest);
    }   
    
    return(
        <form onSubmit={handleSubmit}>
            <div className='SearchBar' >
                <input type='text' placeholder='Search MTB' value= {searchRequest} onChange={(event) => setSearchRequest(event.target.value)}/>
            </div>
            <div className='SearchButton'>
            <button type="submit">Search</button>
            </div>
        </form>



    )

}

export default SearchBar;