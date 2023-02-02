import {authAPI} from "../api/api";
import {getSidebarMenuList} from "./app-reducer";

const SET_USER_DATA = 'homeserver/auth/SET_USER_DATA';

let initialState = {
    id: null,
    username: null,
    isAuth: false,
    isSuper: false,
}

const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_USER_DATA:
            return {
                ...state, ...action.payload
            }
        default:
            return state;
    }
}

export const setAuthUserData = (id, username, isAuth, isSuper) => (
    { type: SET_USER_DATA, payload: { id, username, isAuth, isSuper } })

export const getAuthUserData = () => async dispatch => {
    const data = await authAPI.getUserData();
    if (data) dispatch(setAuthUserData(data.id, data.username, true, data.is_superuser));
}

export const login = data => async dispatch => {
    await authAPI.login(data);
    dispatch(getAuthUserData());
    dispatch(getSidebarMenuList());
}

export const logout = () => dispatch => {
    authAPI.logout();
    dispatch(setAuthUserData(null, null, false, false));
}

export default authReducer;