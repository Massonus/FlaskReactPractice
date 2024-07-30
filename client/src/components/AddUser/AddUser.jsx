import React, {useState} from 'react';
import {addUser} from '../../api/api';
import './AddUser.css';

const AddUser = ({fetchUsers}) => {
    const [name, setName] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await addUser({name});
        fetchUsers();
        setName('');
    };

    return (
        <div className="add-user-container">
            <h2>Add User</h2>
            <form className="add-user-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    className="add-user-input"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <button type="submit" className="add-user-button">Add</button>
            </form>
        </div>
    );
};

export default AddUser;
