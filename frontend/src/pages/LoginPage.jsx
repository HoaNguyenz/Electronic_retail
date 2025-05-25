import React, { useState } from "react";
import bg from "../assets/bg.png";
import { LuEye, LuEyeClosed } from "react-icons/lu";
import { login_user } from "../services/auth";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await login_user(email, password);
      if (response?.message === "Login successful") {
        localStorage.setItem("user", JSON.stringify(response));
        navigate("/");
      } else {
        setError(response?.message || "Đăng nhập thất bại!");
      }
    } catch (err) {
      const errorMsg =
        err.response?.data?.message ||
        err.response?.data?.error ||
        "Đăng nhập thất bại!";
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
          Đăng nhập
        </h2>

        <form onSubmit={handleLogin} className="flex flex-col gap-4">
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
              className="absolute right-3 top-10 text-gray-500 hover:text-primary cursor-pointer"
            >
              {showPassword ? <LuEye size={20} /> : <LuEyeClosed size={20} />}
            </span>
          </div>

          <button
            className="w-full bg-primary text-white p-2 rounded-md hover:bg-secondary transition"
            type="submit"
          >
            Đăng nhập
          </button>

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded relative text-center">
              {error}
            </div>
          )}

          <div className="flex justify-between text-sm">
            <p>Chưa có tài khoản?</p>
            <a href="/sign-up" className="font-medium hover:text-primary">
              Đăng kí
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
