import React, { useState } from "react";
import Header from "../components/Header";
import Sidebar from "../components/myaccount/Sidebar";
import Order from "../components/myaccount/Order";
import Profile from "../components/myaccount/Profile";
import Address from "../components/myaccount/Address";

const MyAccountPage = () => {
  const [selectedTab, setSelectedTab] = useState("Đơn hàng");

  const renderContent = () => {
    switch (selectedTab) {
      case "Đơn hàng":
        return <Order></Order>;
      case "Cập nhật thông tin":
        return <Profile></Profile>;
      case "Địa chỉ":
        return <Address></Address>;
      case "Đăng xuất":
        // Clear localStorage and redirect to home
          localStorage.clear();
          window.location.href = "/";
          return null;
      default:
        return <Order></Order>;
    }
  };
  return (
    <div>
      <Header></Header>
      <div className="mx-[13vw] mt-5 border border-gray-300 flex">
        <Sidebar setSelectedTab={setSelectedTab}></Sidebar>
        <div className="w-3/4 pl-2">{renderContent()}</div>
      </div>
    </div>
  );
};

export default MyAccountPage;
