import axios from "axios";
import Cookies from "universal-cookie";

let baseURL = window.location.href;
if (window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1') {
    baseURL = `http://127.0.0.1:8000/`;
}
baseURL += 'backend/';

const axiosInstance = axios.create({baseURL});

export const authAPI = {
    getUserData() {
        const username = tokenAPI.getUserName()
        const headers = tokenAPI.getHeaders()
        if (username) {
            return axiosInstance
                .get(`user/${username}/`, {headers})
                .then(response => response.data)
        }
    }
    ,
    login(data) {
        return axiosInstance
            .post('api/token/', data)
            .then(response => {
                tokenAPI.setUserName(data.username);
                return response.data
            })
            .then(data => this.setToken(data.access, data.refresh))
            .catch(error => alert('Неверный логин или пароль'))
    },
    setToken(access, refresh) {
        return tokenAPI.setToken(access, refresh)
    },
    logout() {
        tokenAPI.setUserName('')
        return this.setToken('', '')
    },
    verifyToken() {
        const accessObj = tokenAPI.getAccessToken();
        if (accessObj) {
            return axiosInstance
                .post('api/token/verify/', accessObj)
                .then(response => response.data)
                .catch(error => this.refreshToken())
        } else {

        }
    },
    refreshToken() {
        const refreshObj = tokenAPI.getRefreshToken();
        return axiosInstance
            .post('api/token/refresh/', refreshObj)
            .then(response => response.data)
            .then(data => this.setToken(data.access, data.refresh))
            .catch(error => this.setToken('',''))
    }
}

export const menuAPI = {
    getMenu() {
        const headers = tokenAPI.getHeaders()
        return axiosInstance
            .get(`api/menus/`, {headers})
            .then(response => response.data)
            .catch(error => authAPI.verifyToken())
    },
}

export const nodesAPI = {
    getNodes() {
        const headers = tokenAPI.getHeaders()
        return axiosInstance
            .get(`api/nodemcus/`, {headers})
            .then(response => response.data)
            .catch(error => authAPI.verifyToken())
    },
    clickNode(id) {
        const headers = tokenAPI.getHeaders()
        return axiosInstance
            .get(`api/nodemcus/${id}/?version=click`, {headers})
            .then(response => response.data)
    }
}

const cookies = new Cookies()

export const tokenAPI = {
    setToken (access, refresh) {
        cookies.set('access', access)
        cookies.set('refresh', refresh)
        return cookies
    },
    setUserName(username) {
        cookies.set('username', username)
        return cookies
    },
    getUserName() {
        const username = cookies.get('username');
        if (username) return username;
        return undefined
    },
    getHeaders() {
        const access = cookies.get('access')
        let headers = {'Content-Type': 'application/json'}
        if (access != null && access !== "") {
            headers['Authorization'] = `Bearer ${access}`
        }
        return headers
    },
    getRefreshToken() {
        const refresh = cookies.get('refresh');
        if (refresh) return {'refresh': refresh};
        return undefined
    },
    getAccessToken() {
        const access = cookies.get('access');
        if (access) return {'token': access};
        return undefined
    }
}