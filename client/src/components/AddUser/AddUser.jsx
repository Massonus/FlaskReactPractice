import React, { useState } from 'react';
import { addUser } from '../../api/api';
import './AddUser.css';

const AddUser = () => {
  const [name, setName] = useState('');

  // Функция для обработки отправки формы
  const handleSubmit = async (e) => {
    e.preventDefault();
    const newUser = await addUser({ name });
    console.log('New User:', newUser);
  };

  return (
    <div>
      <h2>Add User</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <button type="submit">Add</button>
      </form>
    </div>
  );
};

export default AddUser;
