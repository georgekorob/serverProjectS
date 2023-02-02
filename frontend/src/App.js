import React from 'react';
import './App.css';
import {Route, BrowserRouter, Routes, Navigate} from "react-router-dom";
import NotFound404 from "./components/common/NotFound404";
import LoginForm from "./components/LoginForm";
import MainPage from './components/Main';
import ContactsPage from "./components/Contacts";
import AboutPage from "./components/About";
import Footer from './components/common/Footer';
import NodeList from "./components/Nodes";
import {compose} from "redux";
import {Provider} from "react-redux";
import store from "./redux/store";
import Header from "./components/common/Header";
import withRouter from "./hoc/withRouter";

const App = (props) => {
    return (
        <div>
            <Header/>
            <Routes>
                <Route exact path='/' element={<MainPage/>}></Route>
                <Route exact path='/home' element={<NodeList/>}></Route>
                <Route exact path='/contacts' element={<ContactsPage/>}></Route>
                <Route exact path='/about' element={<AboutPage/>}></Route>
                <Route exact path='/login' element={<LoginForm/>}></Route>
                <Route exact path='/redirect' element={<Navigate to='/'/>}></Route>
                <Route element={NotFound404}/>
            </Routes>
            <Footer/>
        </div>
    )
}

let AppContainer = compose(withRouter)(App);

let MainApp = () => {
    return <BrowserRouter>
        <Provider store={store}>
            <AppContainer/>
        </Provider>
    </BrowserRouter>
}

export default MainApp;
