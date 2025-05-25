import React, { useState, useEffect } from "react";
import logo from "../assets/logo.svg";
import { Link } from "react-router-dom";
import { PiShoppingCartSimple } from "react-icons/pi";
import { BiSearchAlt } from "react-icons/bi";
import { CiUser } from "react-icons/ci";
import { fetch_categories, get_cart_count } from "../services/api";
import { useNavigate } from "react-router-dom";


const Header = () => {
  const [showCategories, setShowCategories] = useState(false);
  const [categories, setCategories] = useState([]);
  const [user, setUser] = useState(null);
  const [cartCount, setCartCount] = useState(null);
  const navigate = useNavigate();
  

  useEffect(() => {
    const getCategories = async () => {
      try {
        const data = await fetch_categories();
        setCategories(data.categories);
      } catch (error) {
        setCategories([]);
      }
    };
    getCategories();

    // Check for user in localStorage
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      console.log("User found in localStorage:", storedUser);
      setUser(JSON.parse(storedUser));
    }
  }, []);

  useEffect(() => {
    // Fetch cart count if user is logged in
    const fetchCart = async () => {
      if (user?.customer_id) {
        const count = await get_cart_count({ customer_id: user.customer_id });
        setCartCount(count);
      } else {
        setCartCount(null);
      }
    };
    fetchCart();
  }, [user]);

  return (
    <div className="w-full h-[9vh] flex justify-between items-center px-[4vw] gap-[5vw] sticky z-10 top-0 border border-bottom border-gray-300 bg-white">
      <Link to="/">
        <img src={logo} alt="logo" className="w-[10rem]"></img>
      </Link>

      <div className="w-full h-full flex items-center">
        <div className="h-full flex justify-start gap-[3vw] items-center">
          <div
            className="font-semibold hover:text-primary cursor-pointer relative"
            onMouseEnter={() => {
              setShowCategories(true);
            }}
            onMouseLeave={() => {
              setShowCategories(false);
            }}
          >
            <div className="py-5">Danh mục hàng</div>
            {showCategories && (
              <ul className="absolute left-1/2 -translate-x-1/2 top-full w-[200px] bg-white border border-gray-300 shadow-lg rounded-md z-50">
                {categories.length > 0 ? (
                  categories.map((category, idx) => (
                    <li
                      key={idx}
                      className="p-2 hover:bg-gray-200 cursor-pointer"
                      onClick={() => navigate(`/ProductList?category=${encodeURIComponent(category)}`)}
                    >
                      {category}
                    </li>
                  ))
                ) : (
                  <li>Danh sách rỗng</li>
                )}
              </ul>
            )}
          </div>
          <div className="font-semibold hover:text-primary cursor-pointer">
            <Link to="/my-account">Tài khoản</Link>
          </div>
          {/* Conditionally render login/signup or user info */}
          {!user ? (
            <>
              <div className="font-semibold hover:text-primary cursor-pointer">
                <Link to="/login">Đăng nhập</Link>
              </div>
              <div className="font-semibold hover:text-primary cursor-pointer">
                <Link to="/sign-up">Đăng kí</Link>
              </div>
            </>
          ) : (
            <div className="font-semibold text-blue-800 underline flex items-center gap-2">
              <CiUser size={22} />
              <span>
                {user.name || user.username || user.email || "User"}
              </span>
            </div>

          )}
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
        <div className="relative">
          <PiShoppingCartSimple
            size={30}
            className="hover:text-primary cursor-pointer"
            onClick={() => navigate("/checkout")}
          />
          {cartCount !== null && cartCount > 0 && (
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full px-2 py-0.5 min-w-[20px] text-center">
              {cartCount}
            </span>
          )}
        </div>
      </div>
    </div>
  );
};

export default Header;