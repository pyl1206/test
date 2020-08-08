import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_value, squares, linewidth=5)  # 设置线宽

# 设置图标的标题和坐标
plt.title("squares numbers", fontsize=24)  # 设置标题的字号
plt.xlabel("Value", fontsize=14)
plt.ylabel("squares of value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()  # 展示
