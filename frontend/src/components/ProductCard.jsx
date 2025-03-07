import React from 'react'
import img1 from "../assets/man_hinh.jpg"

const ProductCard = () => {
  return (
    <div className='w-[18vw] h-[50vh] border border-gray-300 rounded-md flex flex-col items-center mt-5 hover:border-primary'>
        <div className='w-[90%] h-[70%] border border-gray-300 rounded-md mt-2 overflow-hidden'>
            <img src={img1} alt="" className='object-fit'/>
        </div>
        <div className='mt-2 h-[30%] w-[90%]'>
            <h3 className='text-sm text-gray-400'>Bàn phím</h3>
            <h2 className='font-medium'>Bàn phím led rgb</h2>
            <p className='font-bold text-primary'>1.369.000Đ</p>
        </div>
    </div>
  )
}

export default ProductCard