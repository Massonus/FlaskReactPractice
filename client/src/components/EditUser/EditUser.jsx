import React, {useState, useEffect} from 'react';
import {updateUser} from '../../api/api';
import './EditUser.css';

const EditUser = ({user, onUpdate}) => {
    const [name, setName] = useState(user.name);

    const handleSubmit = async (e) => {
        e.preventDefault();
        await updateUser(user.id, {name});
        onUpdate();
    };

    return (
        <div>
            <h2>Edit User</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <button type="submit">Update</button>
            </form>
        </div>
    );
};

export default EditUser;
