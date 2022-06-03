import axios from 'axios';
import React, { useState } from 'react';

function CreatePostForm() {
    // const [submitting, setSubmitting] = useState(false);
    let handleSubmit = async (event) => {
        event.preventDefault();
        try {
            let response = await axios.post("http://127.0.0.1:8000/api/posts/create/", {
                method: "POST",
                body: JSON.stringify({
                    name: username,
                }),
            });
            let responseJson = await responseJson();
            if (response.status === 200) {
                setUserName("");
                setMessage("Your Travel Post created successfully!")
            } else{
                setMessage("An error occured while trying to create Post.")
            }
        } catch(error) {
            console.log(error);
        }


            //Add the Post request from Postman here to make the API request so you can make the GET request in the PostsHistory page.

}

    return(
    <div className="postform">
        <h1>How was your trip? Tell us all about it!</h1>
        {submitting &&
        <div>Submtting Form...</div>
    }
        <form onSubmit={handleSubmit}>
            <fieldset>
                <div className='inputfield'>
                    <label>
                        <p>Destinantion</p>
                        <input destination=" " />
                    </label>

                    <label>
                        <p>Lodging Review</p>
                        <input lodging=" " />
                    </label>

                    <label>
                        <p>Best Places to Dine</p>
                        <input dining=" " />
                    </label>

                    <label>
                        <p>Entertainment I enjoyed</p>
                        <input entertainment=" " />
                    </label>

                    <label>
                        <p>Must See's at this location</p>
                        <input sites=" " />
                    </label>
                </div>
                <label className='blabberbox'>
                    <p>Here's what I would say all together about this destination</p>
                    <input overall=" " />
                </label>
            </fieldset>
            <button type="submit">Submit</button>
        </form>
    </div>
  )
}

export default CreatePostForm;