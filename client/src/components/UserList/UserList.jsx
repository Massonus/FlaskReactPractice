import React, {useEffect, useState} from 'react';
import {getUsers} from '../../api/api';
import './UserList.css';

const UserList = () => {
    const [users, setUsers] = useState([]);

    // useEffect для загрузки списка пользователей при монтировании компонента
    useEffect(() => {
        const fetchUsers = async () => {
            const usersData = await getUsers();
            setUsers(usersData);
        };

        fetchUsers();
    }, []);

    return (
        <div>
            <h2>User List</h2>
            <ul>
                {users.map((user) => (
                    <li key={user.id}>{user.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default UserList;
