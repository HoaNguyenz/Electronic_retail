import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import { get_cart_items, remove_item_cart, make_payment } from "../services/api";

const CheckoutPage = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [payingOrderId, setPayingOrderId] = useState(null);

  const storedUserStr = localStorage.getItem("user");
  const storedUser = storedUserStr ? JSON.parse(storedUserStr) : null;
  const customer_id = storedUser?.customer_id;

  useEffect(() => {
    const fetchCart = async () => {
      setLoading(true);
      if (!customer_id) {
        setOrders([]);
        setLoading(false);
        return;
      }
      const res = await get_cart_items({ customer_id });
      setOrders(res);
      setLoading(false);
    };
    fetchCart();
  }, [customer_id]);

  const refreshCart = async () => {
    const res = await get_cart_items({ customer_id });
    setOrders(res);
  };

  const handleRemove = async (order_item_id) => {
    await remove_item_cart(order_item_id);
    await refreshCart();
  };

  const handlePayment = async (order_id) => {
    const payment_method = "cash";
    setPayingOrderId(order_id);
    try {
      const result = await make_payment({ customer_id, order_id, payment_method });
      alert(result?.message || "Thanh toán thành công!");
      await refreshCart();
    } catch (err) {
      alert("Thanh toán thất bại!");
    }
    setPayingOrderId(null);
  };

  return (
    <div>
      <Header />
      <div className="max-w-4xl mx-auto mt-8 p-4 bg-white rounded shadow">
        <h2 className="text-2xl font-bold mb-6">Giỏ hàng của bạn</h2>
        {loading ? (
          <div>Đang tải...</div>
        ) : orders.length === 0 ? (
          <div>Giỏ hàng trống.</div>
        ) : (
          orders.map((order) => {
            const total = order.cart.reduce(
              (sum, item) => sum + (item.price || 0) * (item.quantity || 1),
              0
            );
            return (
              <div key={order.order_id} className="mb-8 border rounded p-4 shadow-sm">
                <h3 className="text-xl font-semibold mb-3">Đơn hàng #{order.order_id}</h3>
                <table className="w-full mb-4">
                  <thead>
                    <tr className="border-b">
                      <th className="text-left py-2">Sản phẩm</th>
                      <th className="text-left py-2">Giá</th>
                      <th className="text-left py-2">Số lượng</th>
                      <th className="text-left py-2">Thành tiền</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    {order.cart.map((item) => (
                      <tr key={item.order_item_id} className="border-b">
                        <td className="py-2">{item.name}</td>
                        <td className="py-2">{item.price?.toLocaleString()}₫</td>
                        <td className="py-2">{item.quantity}</td>
                        <td className="py-2">
                          {(item.price * item.quantity)?.toLocaleString()}₫
                        </td>
                        <td className="py-2">
                          <button
                            className="text-red-500 hover:underline"
                            onClick={() => handleRemove(item.order_item_id)}
                          >
                            Xóa
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                <div className="text-right font-bold text-lg">
                  Tổng cộng: {total.toLocaleString()}₫
                </div>
                <button
                  className="mt-4 bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600"
                  onClick={() => handlePayment(order.order_id)}
                  disabled={payingOrderId === order.order_id}
                >
                  {payingOrderId === order.order_id ? "Đang thanh toán..." : "Thanh toán"}
                </button>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};

export default CheckoutPage;
