import React, {useState, useEffect} from 'react';
import UserList from '../UserList';
import AddUser from '../AddUser';
import EditUser from '../EditUser';
import './Home.css';
import {getUsers} from '../../api/api';

const Home = () => {
    const [editingUser, setEditingUser] = useState(null);
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        const usersData = await getUsers();
        setUsers(usersData);
    };

    const handleEdit = (user) => {
        setEditingUser(user);
    };

    const handleUpdate = () => {
        setEditingUser(null);
        fetchUsers();
    };

    return (
        <div className="home-container">
            <h1 className="home-title">My App</h1>
            <AddUser fetchUsers={fetchUsers}/>
            {editingUser ? (
                <EditUser user={editingUser} onUpdate={handleUpdate}/>
            ) : (
                <UserList users={users} onEdit={handleEdit}/>
            )}
        </div>
    );
};

export default Home;
