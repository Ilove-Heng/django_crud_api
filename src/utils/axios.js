import axios from "axios";

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Authorization': 'Token d4966fa136f9ae1a43b979cc44609096fb7b6539',
        'Content-Type': 'application/json',
    }
});

export default instance;
