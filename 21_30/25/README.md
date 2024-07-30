# multiprocessing - tạo nhiều process chạy độc lập với nhau

So sánh vs thread: <br>

1. Process sẽ thực sự chạy song song (thread thì k)
2. Sử dụng memory riêng
3. Tối ưu tác vụ CPU-bound, khi đẩy việc tính toán sang CPU khác
4. Tận dụng tài nguyên CPU tối đa
5. Overhead cao hơn, việc giao tiếp giữa các process phức tạp hơn thread
