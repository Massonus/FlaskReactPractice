import axios from 'axios';

// URL API бэкенда
const API_URL = 'http://localhost:5000';

// Функция для получения списка пользователей
export const getUsers = async () => {
    const response = await axios.get(`${API_URL}/users`);
    return response.data;
};

// Функция для добавления нового пользователя
export const addUser = async (user) => {
    const response = await axios.post(`${API_URL}/users`, user);
    return response.data;
};

// Функция для обновления пользователя
export const updateUser = async (userId, user) => {
    const response = await axios.put(`${API_URL}/users/${userId}`, user);
    return response.data;
};

// Функция для удаления пользователя
export const deleteUser = async (userId) => {
    const response = await axios.delete(`${API_URL}/users/${userId}`);
    return response.data;
};
