from langchain_core.tools import tool

# ============================================================
# MOCK DATA - Dữ liệu giả lập hệ thống du lịch
# Lưu ý: Giá cả có logic (VD: cuối tuần đắt hơn, hạng cao hơn đắt hơn)
# Sinh viên cần đọc hiểu data để debug test cases.
# ============================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1450000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2800000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1200000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1350000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1100000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1600000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1300000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3200000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1300000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1800000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1200000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3500000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1500000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2800000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1400000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180000, "area": "Quận 1", "rating": 4.6},
    ],
}


def format_price(price: int) -> str:
    """Format số tiền kiểu Việt Nam: 1450000 -> 1.450.000đ"""
    return f"{price:,}".replace(",", ".") + "đ"


def normalize_text(text: str) -> str:
    """Chuẩn hóa chuỗi đầu vào để giảm lỗi do khoảng trắng thừa."""
    return text.strip()


@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.

    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')

    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy chuyến bay, trả về thông báo không có chuyến.
    """
    origin = normalize_text(origin)
    destination = normalize_text(destination)

    key = (origin, destination)
    reverse_key = (destination, origin)

    flights = None
    route_text = f"{origin} -> {destination}"

    if key in FLIGHTS_DB:
        flights = FLIGHTS_DB[key]
    elif reverse_key in FLIGHTS_DB:
        flights = FLIGHTS_DB[reverse_key]
        route_text = f"{destination} -> {origin} (tìm thấy theo chiều ngược trong mock data)"
    else:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    # Sắp xếp theo giá tăng dần rồi theo giờ khởi hành
    flights = sorted(flights, key=lambda x: (x["price"], x["departure"]))

    lines = [f"Danh sách chuyến bay cho chặng {route_text}:"]
    for idx, flight in enumerate(flights, start=1):
        lines.append(
            f"{idx}. {flight['airline']} | "
            f"{flight['departure']} - {flight['arrival']} | "
            f"{flight['class']} | "
            f"{format_price(flight['price'])}"
        )

    cheapest = flights[0]
    lines.append(
        f"Gợi ý tiết kiệm nhất: {cheapest['airline']} lúc {cheapest['departure']} "
        f"với giá {format_price(cheapest['price'])}."
    )

    return "\n".join(lines)


@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.

    Tham số:
    - city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: giá tối đa mỗi đêm (VNĐ), mặc định không giới hạn

    Trả về danh sách khách sạn phù hợp với tên, số sao, giá, khu vực, rating.
    """
    city = normalize_text(city)

    if city not in HOTELS_DB:
        return f"Không tìm thấy dữ liệu khách sạn tại {city}."

    hotels = HOTELS_DB[city]

    # Lọc theo giá
    filtered_hotels = [hotel for hotel in hotels if hotel["price_per_night"] <= max_price_per_night]

    if not filtered_hotels:
        return (
            f"Không tìm thấy khách sạn tại {city} với giá dưới "
            f"{format_price(max_price_per_night)}/đêm. Hãy thử tăng ngân sách."
        )

    # Sắp xếp theo rating giảm dần, nếu bằng nhau thì giá tăng dần
    filtered_hotels.sort(key=lambda x: (-x["rating"], x["price_per_night"]))

    lines = [
        f"Danh sách khách sạn tại {city} với giá tối đa {format_price(max_price_per_night)}/đêm:"
    ]

    for idx, hotel in enumerate(filtered_hotels, start=1):
        lines.append(
            f"{idx}. {hotel['name']} | "
            f"{hotel['stars']} sao | "
            f"Khu vực: {hotel['area']} | "
            f"Rating: {hotel['rating']} | "
            f"{format_price(hotel['price_per_night'])}/đêm"
        )

    best_hotel = filtered_hotels[0]
    lines.append(
        f"Gợi ý nổi bật: {best_hotel['name']} "
        f"({best_hotel['rating']}★) với giá {format_price(best_hotel['price_per_night'])}/đêm."
    )

    return "\n".join(lines)


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.

    Tham số:
    - total_budget: tổng ngân sách ban đầu (VNĐ)
    - expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy,
      định dạng 'tên_khoản:số_tiền'
      (VD: 'vé_máy_bay:890000,khách_sạn:650000')

    Trả về bảng chi tiết các khoản chi và số tiền còn lại.
    Nếu vượt ngân sách, cảnh báo rõ ràng số tiền thiếu.
    """
    if total_budget < 0:
        return "Lỗi: total_budget phải là số không âm."

    expenses = expenses.strip()
    if not expenses:
        return "Lỗi: expenses không được để trống."

    expense_items = expenses.split(",")
    parsed_expenses = {}

    try:
        for item in expense_items:
            item = item.strip()
            if ":" not in item:
                return (
                    "Lỗi định dạng expenses. "
                    "Mỗi khoản phải có dạng 'tên_khoản:số_tiền'. "
                    "Ví dụ: 'vé_máy_bay:890000,khách_sạn:650000'"
                )

            name, value = item.split(":", 1)
            name = name.strip()
            value = value.strip()

            if not name:
                return "Lỗi định dạng expenses: tên khoản chi không được để trống."

            amount = int(value)
            if amount < 0:
                return f"Lỗi: số tiền của khoản '{name}' không được âm."

            parsed_expenses[name] = parsed_expenses.get(name, 0) + amount

    except ValueError:
        return (
            "Lỗi định dạng số tiền trong expenses. "
            "Hãy dùng số nguyên, ví dụ: 'vé_máy_bay:890000,khách_sạn:650000'"
        )

    total_expense = sum(parsed_expenses.values())
    remaining = total_budget - total_expense

    lines = ["Bảng chi phí:"]
    for name, amount in parsed_expenses.items():
        pretty_name = name.replace("_", " ").capitalize()
        lines.append(f"- {pretty_name}: {format_price(amount)}")

    lines.append("---")
    lines.append(f"Tổng chi: {format_price(total_expense)}")
    lines.append(f"Ngân sách: {format_price(total_budget)}")

    if remaining >= 0:
        lines.append(f"Còn lại: {format_price(remaining)}")
    else:
        lines.append(f"Vượt ngân sách: {format_price(abs(remaining))}. Cần điều chỉnh kế hoạch.")

    return "\n".join(lines)