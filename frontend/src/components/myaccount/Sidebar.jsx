import React , { useState } from "react";
import { BsBox2 } from "react-icons/bs";
import { IoInformationOutline, IoLocationOutline } from "react-icons/io5";
import { FiLogOut } from "react-icons/fi";

const Sidebar = ({ setSelectedTab }) => {
    const [activeTab, setActiveTab] = useState("Đơn hàng");

    const menuItems = [
        { name: "Đơn hàng", icon: <BsBox2 size={20}></BsBox2>},
        { name: "Cập nhật thông tin", icon: <IoInformationOutline size={20}></IoInformationOutline>},
        { name: "Địa chỉ", icon: <IoLocationOutline size={20}></IoLocationOutline>},
        { name: "Đăng xuất", icon: <FiLogOut size={20}></FiLogOut>}
    ]

    const handleTabClick = (name) => {
        setActiveTab(name);
        setSelectedTab(name);
    }
  return (
    <div className="w-1/4 rounded-sm">
      <ul>
        {menuItems.map((item) => (
          <li
            key={item}
            className={`flex items-center gap-3 p-3 rounded-sm cursor-pointer  transition
                ${activeTab === item.name ? "bg-primary text-white" : "hover:bg-primary hover:text-white"}`}
            onClick={() => handleTabClick(item.name)}
          >
            {item.icon}
            {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
