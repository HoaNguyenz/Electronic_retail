import React from "react";
import DataTable from "./DataTable";

const Order = () => {
  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "date", headerName: "Ngày đạt", width: 200 },
    { field: "price", headerName: "Thành tiền", width: 250 },
    { field: "info", headerName: "Thông tin", width: 150 },
  ];

  const rows = [
    { id: 1, date: "13/03/2025", price: "2.339.000Đ", info: "Xem" },
    { id: 2, date: "02/01/2025", price: "199.000Đ", info: "Xem" },
    { id: 3, date: "12/12/2024", price: "1.254.000Đ", info: "Xem" },
  ];
  return (
    <div className="w-full rounded-sm">
      <div className="w-full h-[7vh] bg-gray-200 flex items-center rounded-sm">
        <h2 className="ml-5">Đơn hàng đã đặt</h2>
      </div>
      
      <div className="pt-3">
        <DataTable rows={rows} columns={columns} />
      </div>
    </div>
  );
};

export default Order;
