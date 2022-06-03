// General Imports
import { Routes, Route } from "react-router-dom";
import "./App.css";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";
import MTBUsersPage from "./pages/MTBUsersPage/MTBUsersPage";
import PostForm from "./pages/PostsPage/Posts";
// import FriendsPage from "./pages/FriendsPage/FriendList";

// Component Imports
import Navbar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";
// import SearchMTBUsers from "./components/SearchMTBUsers/SearchMTBUsers";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";
import { useState } from "react";


function App() {



  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<PrivateRoute><HomePage /></PrivateRoute>}/>
        <Route path="/users" element={<PrivateRoute><MTBUsersPage /></PrivateRoute>}/>
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/createpost" element={<PrivateRoute><PostForm/></PrivateRoute>} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
