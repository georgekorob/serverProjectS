import {nodesAPI} from "../api/api";

const SET_NODES = 'homeserver/node/SET_NODES';

let initialState = {
    nodes: []
}

const nodeReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_NODES:
            return { ...state, nodes: action.nodes };
        default:
            return state;
    }
}

export const setNodeList = (nodes) => ({ type: SET_NODES, nodes})

export const getNodeList = () => dispatch => {
    nodesAPI.getNodes().then(data => {
        dispatch(setNodeList(data))
    }).catch(dispatch(setNodeList([])))
}

export const clickButtonNode = (id) => dispatch => {
    nodesAPI.clickNode(id).then(data => {
        console.log(data)
    }).catch(error => console.log(error))
}

export default nodeReducer;