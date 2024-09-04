import matplotlib.pyplot as plt
# ---------------------------读取数据-------------------------------
data_buff = []

file_path = 'data.txt'
with open(file_path, 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        # 在这里你可以使用numbers变量进行进一步处理
        data_buff.append(numbers)

print(data_buff)

# -----------------------------绘图配置---------------------------------
plt.ion() # turning interactive mode on
plt.ylim([0,180])


# -----------------------------绘图---------------------------------
x = []
y = []
y1 = []
time_len = len(data_buff)

for t in range(time_len):
    x.append(t)

    y.append(data_buff[t][0])
    y1.append(data_buff[t][1])

    plt.plot(x, y, 'ro--')
    plt.plot(x, y1, 'bo--')
    plt.pause(1)

plt.pause(999999)