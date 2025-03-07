import React, { useState } from "react";
import bg from "../assets/bg.png";
import { LuEye, LuEyeClosed } from "react-icons/lu";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = (e) => {
    e.preventDefault();
    console.log("Email:", email);
    console.log("Password:", password);
    //API dang nhap
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
            <span onClick={() => setShowPassword(!showPassword)} className="absolute right-3 top-10 text-gray-500 hover:text-primary">
                {showPassword ? <LuEye size={20}></LuEye> : <LuEyeClosed size={20}></LuEyeClosed>}
            </span>
          </div>

          <button
            className="w-full bg-primary text-white p-2 rounded-md hover:bg-secondary transition"
            type="submit"
          >
            Đăng nhập
          </button>

          <div className="flex justify-between">
            <p className="justify-start">Chưa có tài khoản?</p>
            <a href="/sign-up" className="justify-end font-medium hover:text-primary">Đăng kí</a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
