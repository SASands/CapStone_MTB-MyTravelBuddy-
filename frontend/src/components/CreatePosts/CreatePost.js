import axios from 'axios';
import React, { useEffect, useState } from 'react';
import useAuth from "../../hooks/useAuth";

//Add the Post request from Postman here to make the API request so you can make the GET request in the PostsHistory page.

const CreatePostForm= () => {
    const [user, token] = useAuth();
    const [destinantion, setDestination] = useState("");
    const [lodging, setLodging] = useState("");
    const [dining, setDining] = useState("");
    const [entertainment, setEntertainment] = useState("");
    const [mustsees, setMustSees] = useState("");
    const [experience, setExperience] = useState("");
    const [message, setMessage] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();
    };
    useEffect(() => {
        try {
            let response = await axios.post("http://127.0.0.1:8000/api/posts/create/", {
                headers: {
                    Authorization: "Bearer" + token,
                  },
                method: "POST",
                body: JSON.stringify({
                    destinantion: destinantion,
                    lodging: lodging,
                    dining: dining,
                    entertainment: entertainment,
                    mustsees: mustsees,
                    experience: experience,                 
                }),
            });
            let responseJson = await responseJson();
            if (response.status === 200) {
                setMessage("Your Travel Post created successfully!")
            } else{
                setMessage("An error occured while trying to create Post.")
            }
        } catch(error) {
            console.log(error);
        };
    handleSubmit();
}, [token]);

    return(
    <div className="postform">
        <h1>How was your trip {user}? Tell us all about it!</h1>
        <form>
            <fieldset>
                <div className='inputfield'>
                    <label>
                        <p>Destinantion</p>
                        <input destination=" " 
                        value={destinantion}
                        onChange={(event)=> setDestination(event.target.value)}/>
                    </label>

                    <label>
                        <p>Lodging Review</p>
                        <input lodging=" " 
                        value={lodging}
                        onChange={(event)=> setLodging(event.target.value)}/>
                    </label>

                    <label>
                        <p>Best Places to Dine</p>
                        <input dining=" " 
                        value={dining}
                        onChange={(event)=> setDining(event.target.value)}/>
                    </label>

                    <label>
                        <p>Entertainment I enjoyed</p>
                        <input entertainment=" " 
                        value={entertainment}
                        onChange={(event)=> setEntertainment(event.target.value)}/>
                    </label>

                    <label>
                        <p>Must See's at this location</p>
                        <input mustsees=" " 
                        value={mustsees}
                        onChange={(event)=> setMustSees(event.target.value)}/>
                    </label>
                </div>
                <label className='blabberbox'>
                    <p>Here's what I would say all together about this destination</p>
                    <input experience=" " 
                        value={experience}
                        onChange={(event)=> setExperience(event.target.value)}/>
                </label>
            </fieldset>
            <div className="message">{message ? <p>{message}</p> : null}</div>
            <button type="submit" onSubmit={handleSubmit}>Submit</button>
        </form>
    </div>
  )
}

export default CreatePostForm;