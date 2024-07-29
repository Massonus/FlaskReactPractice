import React from 'react';
import UserList from './components/UserList';
import AddUser from './components/AddUser';

const App = () => {
  return (
    <div>
      <h1>My App</h1>
      <UserList />
      <AddUser />
    </div>
  );
};

export default App;
