import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import { Autoplay } from "swiper/modules";
import img1 from "../assets/ban_phim.png";
import img2 from "../assets/lot_chuot.png";
import img3 from "../assets/man_hinh.jpg";

const Banner = () => {
  return (
    <div className="w-full h-[60vh] px-[4vw] object-contain mt-[4vh]">
      <Swiper
        slidesPerView={1}
        loop={true}
        autoplay={{ delay: 3000, disableOnInteraction: false }}
        modules={[Autoplay]}
        className="w-full h-full"
      >
        <SwiperSlide>
          <div className="flex justify-center items-center w-full h-full">
            <img
              src={img1}
              alt="Ban Phim"
              className="w-auto h-full max-h-full object-contain rounded-lg"
            />
          </div>
        </SwiperSlide>
        <SwiperSlide>
          <div className="flex justify-center items-center w-full h-full">
            <img
              src={img2}
              alt="Lot Chuot"
              className="w-auto h-full max-h-full object-contain rounded-lg"
            />
          </div>
        </SwiperSlide>
        <SwiperSlide>
          <div className="flex justify-center items-center w-full h-full">
            <img
              src={img3}
              alt="Man Hinh"
              className="w-auto h-full max-h-full object-contain rounded-lg"
            />
          </div>
        </SwiperSlide>
      </Swiper>
    </div>
  );
};

export default Banner;
