import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import { get_product_detail, add_to_cart } from "../services/api";
import { useSearchParams} from "react-router-dom";


const ProductImage = ({ imgPath }) => (
  <div className="flex-1 flex items-center justify-center bg-gray-50 p-6">
    {imgPath ? (
      <img
        src={imgPath}
        alt="Product"
        className="max-h-[60vh] max-w-full object-contain rounded-lg shadow"
      />
    ) : (
      <div className="text-gray-400">No image available</div>
    )}
  </div>
);

const ProductDetailPanel = ({ product }) => {
  const [quantity, setQuantity] = useState(1);

  // Get customer_id from localStorage (or your auth context)
  const storedUserStr = localStorage.getItem("user");
  const storedUser = storedUserStr ? JSON.parse(storedUserStr) : null;
  const customer_id = storedUser?.customer_id;

  const handleAddToCart = async () => {
    console.log("Add to cart button clicked", { customer_id, productID: product?.ProductID, quantity });
    if (!customer_id || !product?.ProductID) {
      alert("Vui lòng đăng nhập.");
      return;
    }
    try {
      await add_to_cart({
        customer_id,
        order_id: null,
        product_id: product.ProductID,
        quantity: Number(quantity)
      });
      console.log("Add to cart API call successful");
      alert("Đã thêm vào giỏ hàng!");
    } catch (err) {
      console.error("Add to cart error", err);
      alert("Không thể thêm vào giỏ hàng: " + (err?.response?.data?.error || "Lỗi không xác định"));
    }
  };

  return (
    <div className="flex-1 flex flex-col h-[70vh] bg-white rounded-lg shadow p-6">
      <div className="overflow-y-auto flex-1 pr-2">
        <h2 className="text-2xl font-bold mb-2">{product?.Name}</h2>
        <div className="text-gray-700 mb-2">{product?.Description}</div>
        <div className="text-blue-600 font-semibold mb-2">
          {product?.Price?.toLocaleString()}₫
        </div>
        <div className="text-sm text-gray-500 mb-2">
          Rating: {product?.AvgRating ?? "N/A"}
        </div>
        <div className="mt-2">
          <div className="font-semibold mb-1">Số lượng:</div>
          <input
            type="number"
            min={1}
            max={99}
            value={quantity}
            onChange={e => setQuantity(e.target.value)}
            className="border rounded px-2 py-1 w-24"
          />
        </div>
      </div>
      <div className="flex justify-end gap-4 mt-4">
        <button
          className="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600"
          onClick={handleAddToCart}
        >
          Thêm vào giỏ hàng
        </button>
      </div>
    </div>
  );
};
const ProductPage = () => {
  const [product, setProduct] = useState(null);
  const [searchParams] = useSearchParams();
  
  const product_id = searchParams.get("product_id");

  useEffect(() => {
    get_product_detail(product_id).then(setProduct);
  }, [product_id]);

  return (
    <div>
      <Header />
      <div className="max-w-6xl mx-auto flex gap-8 mt-8">
        <ProductImage imgPath={product?.ImagePath} />
        <ProductDetailPanel product={product} />
      </div>
    </div>
  );
};

export default ProductPage;