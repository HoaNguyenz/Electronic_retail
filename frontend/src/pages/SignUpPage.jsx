import React, { useState } from "react";
import bg from "../assets/bg.png";
import { LuEye, LuEyeClosed } from "react-icons/lu";
import { register_user } from "../services/auth";
import { useNavigate } from "react-router-dom";

const SignUpPage = () => {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [user_type, setUserType] = useState("Customer");
  const [error, setError] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const navigate = useNavigate();

  // Optional fields for demo, you can add more as needed
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [zip_code, setZipCode] = useState("");

  const handleSignUp = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError("Mật khẩu xác nhận không khớp!");
      return;
    }
    setError("");
    try {
      const userData = {
        first_name,
        last_name,
        email,
        password,
        user_type,
        phone,
        address,
        city,
        state,
        zip_code,
      };
      const response = await register_user(userData);
      if (response?.message === "User registered successfully") {
        localStorage.setItem("user", JSON.stringify(response));
        navigate("/");
      } else {
        setError(response?.error || response?.message || "Đăng ký thất bại!");
      }
    } catch (err) {
      const errorMsg =
        err.response?.data?.error ||
        err.response?.data?.message ||
        "Đăng ký thất bại!";
      setError(errorMsg);
    }
  };

  return (
    <div
      className="w-full h-screen flex justify-center items-center bg-cover bg-center"
      style={{ backgroundImage: `url(${bg})` }}
    >
      <div className="w-[400px] bg-white p-6 rounded-lg shadow-lg">
        <h2 className="text-xl font-bold text-center text-primary">
          Tạo tài khoản mới
        </h2>

        <form onSubmit={handleSignUp} className="flex flex-col gap-4">
          <div>
            <label className="block mb-1 text-gray-500">Họ</label>
            <input
              type="text"
              placeholder="Nhập họ của bạn..."
              value={first_name}
              required
              onChange={(e) => setFirstName(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Tên</label>
            <input
              type="text"
              placeholder="Nhập tên của bạn..."
              value={last_name}
              required
              onChange={(e) => setLastName(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Email</label>
            <input
              type="email"
              placeholder="Nhập email của bạn..."
              value={email}
              required
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Số điện thoại</label>
            <input
              type="text"
              placeholder="Nhập số điện thoại..."
              value={phone}
              required
              onChange={(e) => setPhone(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Địa chỉ</label>
            <input
              type="text"
              placeholder="Nhập địa chỉ..."
              value={address}
              required
              onChange={(e) => setAddress(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Thành phố</label>
            <input
              type="text"
              placeholder="Nhập thành phố..."
              value={city}
              required
              onChange={(e) => setCity(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Tỉnh/Thành</label>
            <input
              type="text"
              placeholder="Nhập tỉnh/thành..."
              value={state}
              required
              onChange={(e) => setState(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          <div>
            <label className="block mb-1 text-gray-500">Mã bưu điện</label>
            <input
              type="text"
              placeholder="Nhập mã bưu điện..."
              value={zip_code}
              required
              onChange={(e) => setZipCode(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
          </div>
          {/* <div>
            <label className="block mb-1 text-gray-500">Loại tài khoản</label>
            <select
              value={user_type}
              onChange={(e) => setUserType(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md"
            >
              <option value="Customer">Khách hàng</option>
              <option value="Admin">Quản trị viên</option>
            </select>
          </div> */}
          <div className="relative">
            <label className="block mb-1 text-gray-500">Mật khẩu</label>
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Nhập mật khẩu của bạn..."
              value={password}
              required
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
            <span
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-2 top-10 cursor-pointer text-gray-500 hover:text-primary"
            >
              {showPassword ? <LuEye size={20} /> : <LuEyeClosed size={20} />}
            </span>
          </div>
          <div className="relative">
            <label className="block mb-1 text-gray-500">
              Xác nhận mật khẩu
            </label>
            <input
              type={showConfirmPassword ? "text" : "password"}
              placeholder="Nhập lại mật khẩu..."
              value={confirmPassword}
              required
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:border-secondary hover:border-primary"
            />
            <span
              className="absolute right-3 top-10 cursor-pointer text-gray-500 hover:text-primary"
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
            >
              {showConfirmPassword ? (
                <LuEye size={20}></LuEye>
              ) : (
                <LuEyeClosed size={20}></LuEyeClosed>
              )}
            </span>
          </div>

          {error && <p className="text-red-500 text-sm">{error}</p>}

          <button
            className="w-full bg-primary text-white p-2 rounded-md hover:bg-secondary transition"
            type="submit"
          >
            Đăng kí
          </button>

          <div className="flex justify-between">
            <p className="justify-start">Đã có tài khoản?</p>
            <a
              href="/login"
              className="justify-end font-medium hover:text-primary"
            >
              Đăng nhập
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUpPage;