import React, { useState } from "react";
import logo from "../assets/logo.svg";
import { Link } from "react-router-dom";
import { PiShoppingCartSimple } from "react-icons/pi";
import { BiSearchAlt } from "react-icons/bi";
import { CiUser } from "react-icons/ci";

const Header = () => {
  const [showCategories, setShowCategories] = useState(false);
  const categories = ["Bàn phím", "Chuột", "Màn hình", "Sạc", "Tai nghe"];
  return (
    <div className="w-full h-[9vh] flex justify-between items-center px-[4vw] gap-[5vw] sticky z-10 top-0 border border-bottom border-gray-300 bg-white">
      <Link to="/">
        <img src={logo} alt="logo" className="w-[10rem]"></img>
      </Link>

      <div className=" w-full h-full flex items-center">
        <div className="h-full flex justify-start gap-[3vw] items-center">
          <div className="font-semibold hover:text-primary cursor-pointer relative"
              onMouseEnter={()=>{setShowCategories(true)}}
              onMouseLeave={()=>{setShowCategories(false)}}
          >
            <div className="py-5">Danh mục hàng</div>
            {showCategories && (
              <ul className="absolute left-1/2 -translate-x-1/2 top-full w-[200px] bg-white border border-gray-300 shadow-lg rounded-md z-50">
                {categories.length > 0 ? (
                  categories.map((category)=>(
                    <li key={category.id} className="p-2 hover:bg-gray-200 cursor-pointer">
                      {category}
                    </li>
                  ))
                ):(
                  <li>Danh sách rỗng</li>
                )}
              </ul>
            )

            }
          </div>
          <div className="font-semibold hover:text-primary cursor-pointer">
            <Link to="/my-account">Tài khoản</Link>
          </div>
          <div className="font-semibold hover:text-primary cursor-pointer">
            <Link to="/login">Đăng nhập</Link>
          </div>
          <div className="font-semibold hover:text-primary cursor-pointer">
            <Link to="/sign-up">Đăng kí</Link>
          </div>
        </div>
      </div>

      <div className="w-full h-full flex items-center justify-end gap-[2vw]">
        <div className="w-[70%] h-[80%] bg-white flex items-center gap-1 px-2 border border-gray-300 rounded-md">
          <input
            type="text"
            placeholder="Tìm kiếm sản phẩm..."
            className="w-full outline-none"
          />
          <BiSearchAlt size={25} className="text-primary"></BiSearchAlt>
        </div>
        <PiShoppingCartSimple
          size={30}
          className="hover:text-primary cursor-pointer"
        ></PiShoppingCartSimple>
      </div>
    </div>
  );
};

export default Header;
