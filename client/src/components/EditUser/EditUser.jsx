import React, {useState} from 'react';
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
        <div className="edit-user-container">
            <h2>Edit User</h2>
            <form className="edit-user-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    className="edit-user-input"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <button type="submit" className="edit-user-button">Update</button>
            </form>
        </div>
    );
};

export default EditUser;
