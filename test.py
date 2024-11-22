# # import mysql.connector
# # import pandas as pd
# # import plotly.express as px
# # import streamlit as st
# # from datetime import datetime

# # # Kết nối đến cơ sở dữ liệu MySQL
# # def connect_to_database():
# #     return mysql.connector.connect(
# #         host="127.0.0.1",
# #         user="root",
# #         password="Ptn.1910",
# #         database="flight_2"
# #     )




# #     elif user_input == "Flights Analytics":
# #         st.title("Analytics")

# #         # # Phân phối giá
# #         # st.header("Price Distribution")
# #         # query_price = f"""
# #         # SELECT airline, AVG(price) AS average_price
# #         # FROM flights_data
# #         # WHERE id_departure = %s AND id_arrival = %s
# #         # GROUP BY airline;
# #         # """
# #         # cursor = conn.cursor()
# #         # cursor.execute(query_price, (source, destination))
# #         # result = cursor.fetchall()
# #         # column_names = [desc[0] for desc in cursor.description]
# #         # cursor.close()

# #         # if result:
# #         #     df = pd.DataFrame(result, columns=column_names)
# #         #     fig = px.bar(df, x='airline', y='average_price', title='Average price by airline')
# #         #     st.plotly_chart(fig)
# #         # else:
# #         #     st.warning("No price distribution data available.")

# # except mysql.connector.Error as err:
# #     st.error(f"Database connection error: {err}")

# # finally:
# #     if 'conn' in locals() and conn.is_connected():
# #         conn.close()

# import mysql.connector
# import pandas as pd
# import plotly.express as px
# import streamlit as st
# from datetime import datetime

# # Kết nối đến cơ sở dữ liệu MySQL
# def connect_to_database():
#     return mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="Ptn.1910",
#         database="flight_2"
#     )

# # Lấy danh sách thành phố (departure hoặc arrival)
# def get_cities(conn, column_name):
#     query = f"SELECT DISTINCT {column_name} FROM flights_data;"
#     cursor = conn.cursor()
#     cursor.execute(query)
#     cities = [row[0] for row in cursor.fetchall()]
#     cursor.close()
#     return cities

# # Lấy dữ liệu chuyến bay theo điểm đi, điểm đến và ngày bay
# def get_flights(conn, source, destination, date):
#     query = f"""
#     SELECT airline, travel_class, is_nonstop, price, departure_datetime, arrival_datetime
#     FROM flights_data
#     WHERE id_departure = %s AND id_arrival = %s AND STR_TO_DATE(SUBSTRING_INDEX(departure_datetime, ' ', 1), '%m/%d/%Y') = %s;
#     """
#     cursor = conn.cursor()
#     cursor.execute(query, (source, destination, date))
#     result = cursor.fetchall()
#     column_names = [desc[0] for desc in cursor.description]
#     cursor.close()
#     return result, column_names

# # Cải tiến giao diện với các thành phần Streamlit
# def build_interface():
#     st.sidebar.image("https://i2.ex-cdn.com/crystalbay.com/files/content/2024/05/13/charter-flight-tashkent-cam-ranh-thang-6-7-2024-1-1808.jpeg", use_container_width=True
# )  # Logo placeholder
#     st.sidebar.title("✈️ Flight Dashboard")
#     user_input = st.sidebar.selectbox(
#         "Menu", ["Home", "Search Flights", "Flight Analytics"]
#     )
#     return user_input

# # Kết nối với cơ sở dữ liệu
# try:
#     conn = connect_to_database()

#     # Xây dựng giao diện
#     user_input = build_interface()

#     if user_input == "Home":
#         st.title("Welcome to Flight Dashboard")
#         st.markdown(
#             """
#             ### ✈️ Explore and Analyze Flights
#             - Search for available flights between cities.
#             - View price distributions and analytics.
#             """
#         )
#         st.image("https://hcmus.edu.vn/wp-content/uploads/2024/11/thumbnail-01-860x575.png", use_container_width=True)

#     elif user_input == "Search Flights":
#         st.title("Search Flights")
#         st.markdown("Find the best flights for your journey.")
#         st.subheader("Enter travel details below:")

#         # Lấy danh sách thành phố
#         cities_departure = get_cities(conn, "id_departure")
#         cities_arrival = get_cities(conn, "id_arrival")

#         col1, col2, col3 = st.columns([1, 1, 1])
#         with col1:
#             source = st.selectbox("Source City", cities_departure)
#         with col2:
#             destination = st.selectbox("Destination City", cities_arrival)
#         with col3:
#             departure_date = st.date_input("Departure Date", datetime.today())

#         if st.button("Search"):
#             # Chuyển đổi ngày sang định dạng chuỗi
#             formatted_date = departure_date.strftime("%Y-%m-%d")
#             result, column_names = get_flights(conn, source, destination, formatted_date)
#             if result:
#                 st.success(f"Flights found from {source} to {destination} on {departure_date}")
#                 df = pd.DataFrame(result, columns=column_names)
#                 st.dataframe(df.style.format({"price": "{:,.0f}"}))  # Hiển thị giá định dạng đẹp
#             else:
#                 st.warning(f"No flights found from {source} to {destination} on {departure_date}")

#     elif user_input == "Flight Analytics":
#         st.title("Flight Analytics")
#         st.subheader("Explore flight trends and patterns")

#         # Phân phối giá
#         st.markdown("### Price Distribution by Airline")
#         query_price = """
#         SELECT airline, AVG(price) AS average_price
#         FROM flights_data
#         GROUP BY airline;
#         """
#         cursor = conn.cursor()
#         cursor.execute(query_price)
#         result = cursor.fetchall()
#         column_names = [desc[0] for desc in cursor.description]
#         cursor.close()

#         if result:
#             df = pd.DataFrame(result, columns=column_names)
#             fig = px.bar(
#                 df, x="airline", y="average_price",
#                 title="Average Price by Airline",
#                 labels={"average_price": "Average Price (VND)", "airline": "Airline"},
#                 text_auto=True
#             )
#             st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.warning("No price data available.")

# except mysql.connector.Error as err:
#     st.error(f"Database connection error: {err}")

# finally:
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()

import mysql.connector
import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime

# Hàm thiết lập ảnh nền
def set_background_image():
    background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20210926/pngtree-watercolor-ink-background-with-blue-pastel-image_907645.png"  # URL ảnh nền
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Kết nối đến cơ sở dữ liệu MySQL
def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ptn.1910",
        database="flight_2"
    )

# Lấy danh sách thành phố (departure hoặc arrival)
def get_cities(conn, column_name):
    query = f"SELECT DISTINCT {column_name} FROM flights_data;"
    cursor = conn.cursor()
    cursor.execute(query)
    cities = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return cities

# Lấy dữ liệu chuyến bay theo điểm đi, điểm đến và ngày bay
def get_flights(conn, source, destination, date):
    query = f"""
    SELECT airline, travel_class, is_nonstop, price, departure_datetime, arrival_datetime
    FROM flights_data
    WHERE id_departure = %s AND id_arrival = %s AND STR_TO_DATE(SUBSTRING_INDEX(departure_datetime, ' ', 1), '%m/%d/%Y') = %s;
    """
    cursor = conn.cursor()
    cursor.execute(query, (source, destination, date))
    result = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    return result, column_names

# Cải tiến giao diện với các thành phần Streamlit
def build_interface():
    st.sidebar.image("https://i2.ex-cdn.com/crystalbay.com/files/content/2024/05/13/charter-flight-tashkent-cam-ranh-thang-6-7-2024-1-1808.jpeg", use_container_width=True)
    st.sidebar.title("✈️ Flight Dashboard")
    user_input = st.sidebar.selectbox(
        "Menu", ["Home", "Search Flights", "Flight Analytics"]
    )
    return user_input

# Thiết lập ảnh nền
set_background_image()

# Kết nối với cơ sở dữ liệu
try:
    conn = connect_to_database()

    # Xây dựng giao diện
    user_input = build_interface()

    if user_input == "Home":
        st.title("Welcome to Flight Dashboard")
        st.markdown(
            """
            ### ✈️ Explore and Analyze Flights
            - Search for available flights between cities.
            - View price distributions and analytics.
            """
        )
        st.image("https://hcmus.edu.vn/wp-content/uploads/2024/11/thumbnail-01-860x575.png", use_container_width=True)

    elif user_input == "Search Flights":
        st.title("Search Flights")
        st.markdown("Find the best flights for your journey.")
        st.subheader("Enter travel details below:")

        # Lấy danh sách thành phố
        cities_departure = get_cities(conn, "id_departure")
        cities_arrival = get_cities(conn, "id_arrival")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            source = st.selectbox("Source City", cities_departure)
        with col2:
            destination = st.selectbox("Destination City", cities_arrival)
        with col3:
            departure_date = st.date_input("Departure Date", datetime.today())

        if st.button("Search"):
            # Chuyển đổi ngày sang định dạng chuỗi
            formatted_date = departure_date.strftime("%Y-%m-%d")
            result, column_names = get_flights(conn, source, destination, formatted_date)
            if result:
                st.success(f"Flights found from {source} to {destination} on {departure_date}")
                df = pd.DataFrame(result, columns=column_names)
                st.dataframe(df.style.format({"price": "{:,.0f}"}))  # Hiển thị giá định dạng đẹp
            else:
                st.warning(f"No flights found from {source} to {destination} on {departure_date}")

    elif user_input == "Flight Analytics":
        st.title("Flight Analytics")
        
        # Biểu đồ số lượng chuyến bay theo hãng
        query_flight_count = """
        SELECT airline, COUNT(*) AS flight_count
        FROM flights_data
        GROUP BY airline
        ORDER BY flight_count DESC;
        """
        cursor = conn.cursor()
        cursor.execute(query_flight_count)
        result = cursor.fetchall()
        cursor.close()

        if result:
            df = pd.DataFrame(result, columns=["Airline", "Flight Count"])
            st.subheader("Number of Flights by Airline")
            fig = px.bar(df, x="Airline", y="Flight Count", text="Flight Count", title="Number of Flights by Airline")
            st.plotly_chart(fig, use_container_width=True)

        # Biểu đồ: Phân phối giá vé trung bình theo điểm đến
        query_avg_price_by_destination = """
        SELECT id_arrival AS destination, AVG(price) AS avg_price
        FROM flights_data
        GROUP BY destination
        ORDER BY avg_price DESC;
        """
        cursor = conn.cursor()
        cursor.execute(query_avg_price_by_destination)
        result = cursor.fetchall()
        cursor.close()

        if result:
            df = pd.DataFrame(result, columns=["Destination", "Average Price"])
            st.subheader("Average Ticket Price by Destination")
            fig = px.bar(df, x="Destination", y="Average Price", text="Average Price",
                        title="Average Ticket Price by Destination", color="Destination")
            st.plotly_chart(fig, use_container_width=True)

        # Biểu đồ phân phối giá vé theo hãng
        query_price_distribution = """
        SELECT airline, price
        FROM flights_data;
        """
        cursor = conn.cursor()
        cursor.execute(query_price_distribution)
        result = cursor.fetchall()
        cursor.close()

        if result:
            df = pd.DataFrame(result, columns=["Airline", "Price"])
            st.subheader("Price Distribution by Airline")
            fig = px.box(df, x="Airline", y="Price", title="Price Distribution by Airline", points="all")
            st.plotly_chart(fig, use_container_width=True)
            
        # Biểu đồ: Thời gian cao điểm khởi hành
        query_departure_peak_hours = """
        SELECT HOUR(STR_TO_DATE(SUBSTRING_INDEX(departure_datetime, ' ', -1), '%H:%i')) AS hour, COUNT(*) AS count
        FROM flights_data
        GROUP BY hour
        ORDER BY hour;
        """
        cursor = conn.cursor()
        cursor.execute(query_departure_peak_hours)
        result = cursor.fetchall()
        cursor.close()

        if result:
            df = pd.DataFrame(result, columns=["Hour", "Count"])
            st.subheader("Peak Departure Hours")
            fig = px.histogram(df, x="Hour", y="Count", title="Peak Departure Hours",
                            text_auto=True, color="Hour")
            st.plotly_chart(fig, use_container_width=True)
            
        # Biểu đồ: Tỉ lệ chuyến bay trực tiếp và gián tiếp
        query_nonstop_distribution = """
        SELECT is_nonstop, COUNT(*) AS count
        FROM flights_data
        GROUP BY is_nonstop;
        """
        cursor = conn.cursor()
        cursor.execute(query_nonstop_distribution)
        result = cursor.fetchall()
        cursor.close()

        if result:
            df = pd.DataFrame(result, columns=["Nonstop", "Count"])
            st.subheader("Nonstop vs Indirect Flights")
            fig = px.pie(df, names="Nonstop", values="Count", title="Nonstop vs Indirect Flights")
            st.plotly_chart(fig, use_container_width=True)     
            
        # Biểu đồ: Xu hướng giá vé theo thời gian khởi hành
        query_price_trend_by_departure = """
        SELECT DATE(STR_TO_DATE(SUBSTRING_INDEX(departure_datetime, ' ', 1), '%m/%d/%Y')) AS departure_date,
            AVG(price) AS avg_price
        FROM flights_data
        GROUP BY departure_date
        ORDER BY departure_date;
        """
        cursor = conn.cursor()
        cursor.execute(query_price_trend_by_departure)
        result = cursor.fetchall()
        cursor.close()

        if result:
            df = pd.DataFrame(result, columns=["Departure Date", "Average Price"])
            st.subheader("Ticket Price Trend by Departure Date")
            fig = px.line(df, x="Departure Date", y="Average Price", title="Ticket Price Trend by Departure Date",
                        markers=True)
            st.plotly_chart(fig, use_container_width=True)      
            
        

except mysql.connector.Error as err:
    st.error(f"Database connection error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
