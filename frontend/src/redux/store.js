import {configureStore} from "@reduxjs/toolkit";
import { reducer as formReducer } from 'redux-form'
import appReducer from "./app-reducer";
import authReducer from "./auth-reducer";
import nodeReducer from "./node-reducer";

let store = configureStore({
    reducer: {
        auth: authReducer,
        app: appReducer,
        node: nodeReducer,
        form: formReducer,
    },
});

export default store;