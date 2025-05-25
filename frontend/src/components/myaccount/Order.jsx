import React, { useEffect, useState } from "react";
import DataTable from "./DataTable";
import { fetch_orders } from "../../services/api";
import { DataGrid } from "@mui/x-data-grid";

const Order = () => {
  const storedUserStr = localStorage.getItem("user");
  const storedUser = storedUserStr ? JSON.parse(storedUserStr) : null;
  const customer_id = storedUser?.customer_id;

  const [rows, setRows] = useState([]);
  const [selectedOrder, setSelectedOrder] = useState(null);

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "date", headerName: "Ngày đặt", width: 200 },
    { field: "price", headerName: "Thành tiền", width: 250 },
    { field: "info", headerName: "Thông tin", width: 150 },
  ];

  useEffect(() => {
    const loadOrders = async () => {
      try {
        const data = await fetch_orders(customer_id);
        const mappedRows = data.map((order) => ({
          ...order,
          id: order.order_id,
          date: new Date(order.order_date).toLocaleDateString("vi-VN"),
          price: order.total.toLocaleString("vi-VN") + "Đ",
          info: order.items && order.items.length > 0
            ? order.items.map(item => `${item.name} (x${item.quantity})`).join(", ")
            : "Xem",
        }));
        setRows(mappedRows);
      } catch (error) {
        setRows([]);
      }
    };
    loadOrders();
  }, [customer_id]);

  const handleRowClick = (order) => {
    console.log("Row clicked:", order);
    setSelectedOrder(order);
  };

  const closeModal = () => {
    setSelectedOrder(null);
  };

  return (
    <div className="w-full rounded-sm">
      <div className="w-full h-[7vh] bg-gray-200 flex items-center rounded-sm">
        <h2 className="ml-5">Đơn hàng đã đặt</h2>
      </div>
      <div className="pt-3">
        <DataTable rows={rows} columns={columns} onRowClick={handleRowClick} />
      </div>

      {selectedOrder && (
        <div className="fixed inset-0 z-50 bg-black bg-opacity-40 flex justify-center items-center">
          <div className="bg-white p-6 rounded-md w-[500px] max-h-[80vh] overflow-y-auto">
            <h3 className="text-xl font-semibold mb-4">Chi tiết đơn hàng</h3>
            <p><strong>Mã đơn:</strong> {selectedOrder.order_id}</p>
            <p><strong>Ngày:</strong> {selectedOrder.date}</p>
            <p><strong>Thành tiền:</strong> {selectedOrder.price}</p>
            <p className="mt-3"><strong>Sản phẩm:</strong></p>
            <ul className="list-disc ml-5">
              {selectedOrder.items?.map((item, idx) => (
                <li key={idx}>{item.name} - {item.quantity} x {item.unit_price?.toLocaleString("vi-VN")}Đ</li>
              ))}
            </ul>
            <div className="flex justify-end mt-5">
              <button onClick={closeModal} className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                Đóng
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Order;
