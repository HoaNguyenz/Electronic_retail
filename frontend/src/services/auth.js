import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000'

// Pass email and password as arguments
export const login_user = async (email, password) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/login`, {
            email,
            password
        });
        console.log(response.data);
        return response.data;
    } catch (error){
        console.error('Error logging in:', error);
        throw error;
    }
}

export const register_user = async (userData) => {
    // userData should be an object with all required fields:
    // first_name, last_name, email, phone, address, city, state, zip_code, password, user_type
    try {
        const response = await axios.post(`${API_BASE_URL}/register`, userData);
        return response.data;
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
}