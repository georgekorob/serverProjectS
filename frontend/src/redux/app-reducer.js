import {menuAPI} from "../api/api";

const SET_SIDEBAR = 'homeserver/app/SET_SIDEBAR';

let initialState = {
    sidebar: [
        {'id': 20, 'name': 'Контакты', 'link': '/contacts'},
        {'id': 21, 'name': 'О нас', 'link': '/about'}
    ]
}

const appReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_SIDEBAR:
            return { ...state, sidebar: [...action.menulist, ...initialState.sidebar] };
        default:
            return state;
    }
}

export const setSidebarMenuList = (menulist) => ({ type: SET_SIDEBAR, menulist})

export const getSidebarMenuList = () => async dispatch => {
    const data = await menuAPI.getMenu();
    dispatch(setSidebarMenuList(data));
}

export default appReducer;