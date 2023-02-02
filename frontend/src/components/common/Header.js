import React, {useEffect, useState} from 'react'
import {NavLink} from "react-router-dom";
import {connect} from "react-redux";
import {getSidebarMenuList} from "../../redux/app-reducer";
import {getAuthUserData, logout} from "../../redux/auth-reducer";

function MenuItem({item}) {
    return (
        <li>
            <NavLink className="nav-link" to={item.link}>{item.name}</NavLink>
        </li>
    )
}

const Header = (props) => {
    const [collapsed, setCollapse] = useState(false);
    const show = () => collapsed ? " show" : "";
    const logoutHandle = () => {
        props.logout()
    };
    useEffect(() => {
        props.getAuthUserData();
        props.getSidebarMenuList();
    },[props.getSidebarMenuList, props.getAuthUserData]);

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <a className="navbar-brand" href="/">JDI</a>
            <button className="navbar-toggler" type="button" onClick={() => setCollapse(!collapsed)}
                    data-toggle="collapse" data-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className={"collapse navbar-collapse" + show()} id="navbarCollapse">
                <ul className="navbar-nav col-lg-9">
                    {props.menu.map((link) => <MenuItem key={link.id} item={link}/>)}
                </ul>
                <ul className="navbar-nav justify-content-end col-lg-3">
                    {props.isSuper &&
                    <li><a className="nav-link" href='admin/'>Админка</a></li>}
                    <li>{ props.isAuth
                            ? <NavLink className="nav-link" to='/user/:id'>{props.username}</NavLink>
                            : <NavLink className="nav-link" to='/register'>Регистрация</NavLink>
                        }</li>
                    <li>{ props.isAuth
                            ? <NavLink className="nav-link" to='/' onClick={logoutHandle}>Выйти</NavLink>
                            : <NavLink className="nav-link" to='/login'>Войти</NavLink>
                        }</li>
                </ul>
            </div>
        </nav>
    )
}

let mapStateToProps = (state) => {
    return {
        menu: state.app.sidebar,
        username: state.auth.username,
        isAuth: state.auth.isAuth,
        isSuper: state.auth.isSuper,
    }
}

export default connect(mapStateToProps,
    { getSidebarMenuList, getAuthUserData, logout })(Header);
