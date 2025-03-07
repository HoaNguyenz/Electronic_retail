import React from "react";
import ProductCard from "./ProductCard";

const BestSeller = () => {
  return (
    <div className="mx-[4vw] mt-5">
      <p className="text-xl font-bold text-primary">Các sản phẩm bán chạy</p>
      <div className="h-[100vh] flex justify-between mt-[2vh] border border-gray-300 px-[2vw]">
        <ProductCard></ProductCard>
        <ProductCard></ProductCard>
        <ProductCard></ProductCard>
        <ProductCard></ProductCard>
      </div>
    </div>
  );
};

export default BestSeller;
