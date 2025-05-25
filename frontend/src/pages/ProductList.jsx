import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import { fetch_categories, fetch_products } from "../services/api";
import { useSearchParams, useNavigate } from "react-router-dom";

// CategorySelector Component
const CategorySelector = ({ categories, selected, onSelect }) => (
  <div className="flex gap-2 my-4 flex-wrap">
    {["all", ...categories].map((cat) => (
      <button
        key={cat}
        className={`px-4 py-2 rounded border ${selected === cat ? "bg-blue-500 text-white" : "bg-white text-black"}`}
        onClick={() => onSelect(cat)}
      >
        {cat === "all" ? "Tất cả" : cat}
      </button>
    ))}
  </div>
);

// ProductGrid Component
const ProductGrid = ({ products }) => {
  const navigate = useNavigate();
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {products.map((p) => (
        <div
          key={p.ProductID}
          className="border rounded p-4 shadow hover:shadow-lg transition cursor-pointer"
          onClick={() => navigate(`/product?product_id=${p.ProductID}`)}
        >
          <div className="font-bold text-lg mb-2">{p.Name}</div>
          <div className="text-gray-700 mb-1">{p.Description}</div>
          <div className="text-blue-600 font-semibold mb-1">{p.Price.toLocaleString()}₫</div>
          <div className="text-sm text-gray-500">Rating: {p.AvgRating ?? "N/A"}</div>
        </div>
      ))}
    </div>
  );
};

const ProductList = () => {
  const [categories, setCategories] = useState([]);
  const [selectedCat, setSelectedCat] = useState("all");
  const [products, setProducts] = useState([]);
  const [searchParams] = useSearchParams();

  // Fetch categories on mount
  useEffect(() => {
    fetch_categories().then((data) => {
      setCategories(data.categories || []);
    });
  }, []);

  // Set default category from URL param
  useEffect(() => {
    const urlCat = searchParams.get("category");
    if (urlCat) setSelectedCat(urlCat);
  }, [searchParams]);

  // Fetch products when selectedCat changes
  useEffect(() => {
    const filters = {};
    if (selectedCat !== "all") filters.category_name = selectedCat;
    fetch_products(filters).then((data) => setProducts(data || []));
  }, [selectedCat]);

  return (
    <div>
      <Header />
      <div className="max-w-6xl mx-auto px-4">
        <CategorySelector
          categories={categories}
          selected={selectedCat}
          onSelect={setSelectedCat}
        />
        <ProductGrid products={products} />
      </div>
    </div>
  );
};

export default ProductList;