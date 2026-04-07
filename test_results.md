
##  Test 1
Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu

TravelBuddy đang suy nghĩ...

[AGENT NODE]
-> Trả lời trực tiếp, không gọi tool.

TravelBuddy: Chào bạn! Để mình có thể giúp bạn lên kế hoạch chuyến đi, bạn có thể cho mình biết một số thông tin như:

1. Bạn muốn đi đâu? (Điểm đến)
2. Thời gian dự kiến đi (ngày đi và số ngày lưu trú)
3. Số người đi cùng bạn
4. Ngân sách dự kiến cho chuyến đi

Khi có những thông tin này, mình sẽ giúp bạn tìm kiếm các lựa chọn phù hợp!

##  Test 2
Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...

[AGENT NODE]
-> Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})

[AGENT NODE]
-> Trả lời trực tiếp, không gọi tool.

TravelBuddy: Dưới đây là danh sách các chuyến bay từ Hà Nội đi Đà Nẵng:

1. **VietJet Air** | 08:30 - 09:50 | Economy | **890.000đ** (Gợi ý tiết kiệm nhất)
2. **Bamboo Airways** | 11:00 - 12:20 | Economy | 1.200.000đ
3. **Vietnam Airlines** | 06:00 - 07:20 | Economy | 1.450.000đ
4. **Vietnam Airlines** | 14:00 - 15:20 | Business | 2.800.000đ

Nếu bạn cần thêm thông tin hoặc muốn đặt vé, hãy cho mình biết nhé!


##  Test 3
Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...

[AGENT NODE]
-> Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})

[AGENT NODE]
-> Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2000000})

[AGENT NODE]
-> Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'})

[AGENT NODE]
-> Trả lời trực tiếp, không gọi tool.

TravelBuddy: Dưới đây là kế hoạch chuyến đi từ Hà Nội đến Phú Quốc trong 2 đêm của bạn:

### Chuyến đi:
- **Điểm khởi hành:** Hà Nội
- **Điểm đến:** Phú Quốc
- **Thời gian:** 2 đêm

### Chuyến bay:
- **Hãng:** VietJet Air
- **Giờ bay:** 16:00 - 18:15
- **Giá vé:** 1.100.000đ (gợi ý tiết kiệm nhất)

### Khách sạn:
- **Tên:** 9Station Hostel
- **Khu vực:** Dương Đông
- **Giá mỗi đêm:** 200.000đ
- **Rating:** 4.5

### Ngân sách:
- **Ngân sách ban đầu:** 5.000.000đ
- **Chi phí vé máy bay:** 1.100.000đ
- **Chi phí khách sạn (2 đêm):** 400.000đ (200.000đ x 2)
- **Tổng chi phí ước tính:** 1.500.000đ
- **Ngân sách còn lại:** 3.500.000đ

### Gợi ý thêm:
- Bạn có thể sử dụng ngân sách còn lại để tham gia các hoạt động vui chơi, ăn uống hoặc mua sắm tại Phú Quốc.
- Nếu bạn cần thêm thông tin về các hoạt động hoặc địa điểm tham quan, hãy cho mình biết nhé!

##  Test 4
Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...

[AGENT NODE]
-> Trả lời trực tiếp, không gọi tool.

TravelBuddy: Mình cần thêm các thông tin sau để tư vấn chính xác hơn:

1. Thành phố bạn muốn đặt khách sạn là gì?
2. Ngân sách tối đa mỗi đêm bạn dự định chi là bao nhiêu?
3. Số đêm bạn dự định lưu trú là bao nhiêu?


## Test 5
Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...

[AGENT NODE]
-> Trả lời trực tiếp, không gọi tool.

TravelBuddy: Mình chỉ hỗ trợ các yêu cầu liên quan đến du lịch, vé máy bay, khách sạn, lịch trình và ngân sách chuyến đi. Nếu bạn có câu hỏi nào về du lịch, hãy cho mình biết nhé!


