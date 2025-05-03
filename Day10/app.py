import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("Hello, Streamlit!!!")
st.write("This is my first web application !!")
st.write("This is my second web application !!")
st.write("This is my third web application !!!")
st.header("Tiêu đề 1")
st.subheader("Tiêu đề 2")
data = {
    'course': ['Web Developer', 'Computer Science'],
    'age': ['13-16','14-17']
}
df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)
st.header("Dữ liệu quảng cáo full")
df2 = pd.read_csv("ads_data_full.csv")
st.dataframe(df2.head(10))

st.header("Hiển thị biểu đồ trên web application bằng streamlit")
x = np.linspace(0,10,100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
st.pyplot(fig)


# Tạo dữ liệu mẫu
x_labels = ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5"]
x = np.arange(len(x_labels))  # Trục X là số nguyên
y1 = [10, 15, 7, 12, 18]
y2 = [5, 12, 10, 8, 15]
y3 = [8, 10, 5, 14, 11]

# Tạo figure
fig, ax = plt.subplots(figsize=(8, 5))

# Vẽ nhiều đường trên cùng một biểu đồ
ax.plot(x, y1, marker="o", linestyle="-", color="b", label="Dữ liệu 1")
ax.plot(x, y2, marker="s", linestyle="--", color="r", label="Dữ liệu 2")
ax.plot(x, y3, marker="^", linestyle=":", color="g", label="Dữ liệu 3")

# Thiết lập nhãn trục X
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=0)  # Hiển thị nhãn trục X ngang

# Thêm tiêu đề và chú thích
ax.set_title("Biểu đồ nhiều đường")
ax.set_xlabel("Thời gian")
ax.set_ylabel("Giá trị")
ax.legend()

# Hiển thị biểu đồ trên Streamlit
st.pyplot(fig)
