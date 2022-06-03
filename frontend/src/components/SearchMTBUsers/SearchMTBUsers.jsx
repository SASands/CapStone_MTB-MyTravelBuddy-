// import React, { useState, useEffect } from 'react';
// import "../../App.js";
// import axios from 'axios';
// import SearchBar from '../../components/SearchBar/SearchBar.jsx';


// function SearchMTBUsers(props){
// //Hooks
// const [searchResults, setSearchResults] = useState([])

// useEffect(() => {
//     getSearchResults()
    
// }, [])


// async function getSearchResults(SearchMTBUsers= 'KalToo'){
//     let response = await axios.get(`http://127.0.0.1:8000/api/users/get_users/search?=${SearchMTBUsers}`)
//     console.log(response.data.items)
//     setSearchResults(response.data.items)                    

// }

// const handleClick = (event, id,) => {
//     event.preventDefault();
//     props.setCurrentUserID(id)
// }



// //search logic

//     return(
//         <div className="searchResults">
//         {SearchBar}
//         <div className='SearchBar'>
//         <SearchBar getSearchResults={getSearchResults}/>
//         </div>
//             <div className="allSearchResults">
//                 {searchResults.map(MTBUser =>(
//                     <span>
//                         <div class = "SearchResult">
//                         <input type="image" 
//                                 onClick={(event) => handleClick(event, MTBUser.id.MTBUserID)}
//                                 src = {MTBUser.url}
//                                 />
//                         </div>
//                     </span>

//                 ))}
//             </div>
//         </div>
//     );


    
// }
// export default SearchMTBUsers;