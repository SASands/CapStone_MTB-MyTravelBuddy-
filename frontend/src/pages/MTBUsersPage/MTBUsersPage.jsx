import React, { useState, useEffect } from 'react';
import useAuth from '../../hooks/useAuth';
import axios from 'axios';
import AddButton from '../../components/Buttons/AddButtons';
import FriendsButton from '../../components/Buttons/FriendsButton';
import PendingFriendsButton from '../../components/Buttons/PendingFriends';

const MTBUsersPage = () => {
    const [user, token] = useAuth();
    const [users, setUsers] = useState([]);

    useEffect(() => {
      
        const fetchUsers = async () => {
            try {
                let response = await axios.get("http://127.0.0.1:8000/api/users/get_users/",{
                    headers: {
                        Authorization: "Bearer" + token,
                    },
                });
                console.log(response.data)
                setUsers(response.data);
            } catch (error){
                console.log(error.response.data);
            }
        };
        
        fetchUsers();
    }, [token]);

    return (
        <div className='container'>
                                    {/* We need to link this button to all existing friends of the logged in user */}
            <h1><PendingFriendsButton/>  {user.username} <FriendsButton/></h1>
           
                {users.map((el) => (
                    <div>
                        <p key={el.id}>{el.first_name} {el.last_name}</p>
                        <AddButton/>
                    </div>
                    
                   
                    )
                    

                )}
        </div>

    );
};
export default MTBUsersPage;





