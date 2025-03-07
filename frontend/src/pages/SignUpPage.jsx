import React, { useState } from "react";
import bg from "../assets/bg.png";
import { LuEye, LuEyeClosed } from "react-icons/lu";

const SignUpPage = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const handleSignUp = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError("Mật khẩu xác nhận không khớp!");
      return;
    }
    setError("");

    console.log("Email:", email);
    console.log("Password:", password);
    //API dang ki
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
            <label className="block mb-1 text-gray-500">Username</label>
            <input
              type="text"
              placeholder="Nhập tên người dùng của bạn..."
              value={username}
              required
              onChange={(e) => setUsername(e.target.value)}
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
              {showPassword ? (
                <LuEye size={20}></LuEye>
              ) : (
                <LuEyeClosed size={20}></LuEyeClosed>
              )}
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
