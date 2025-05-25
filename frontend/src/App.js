import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage, LoginPage, SignUpPage, MyAccountPage,ProductList, ProductPage, CheckoutPage, AdminPage } from "./Routes";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/sign-up" element={<SignUpPage />} />
        <Route path="/my-account" element={<MyAccountPage />} />
        <Route path="/ProductList" element={<ProductList />} />
        <Route path="/product" element={<ProductPage />} />
        <Route path="/checkout" element={<CheckoutPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
