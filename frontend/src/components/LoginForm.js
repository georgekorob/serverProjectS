import React from "react";
import {Field, reduxForm} from "redux-form";
import {login} from "../redux/auth-reducer";
import {compose} from "redux";
import {connect} from "react-redux";
import {Navigate} from "react-router-dom";

const Login = ({handleSubmit, isAuth}) => {
    return <div>
        {!isAuth && <form onSubmit={handleSubmit}>
            <h5>Пользователь</h5>
            <Field component='input' type="text" name="username" placeholder="username"/>
            <h5>Пароль</h5>
            <Field component='input' type="password" name="password" placeholder="password"/>
            <div>
                <button onClick={() => {
                }}>Login
                </button>
            </div>
        </form>}
        {isAuth && <Navigate to='/'/>}
    </div>
}

const onSubmit = (formData, dispatch) => {
    dispatch(login(formData));
}

let mapStateToProps = (state) => {
    return {
        isAuth: state.auth.isAuth,
    }
}

export default compose(reduxForm({form: 'login', onSubmit}),
    connect(mapStateToProps))(Login)
