import random
import matplotlib.pyplot as plt
import configparser

# ----------------------------------read configuration for plotting-------------------------------------------
config = configparser.ConfigParser() # 创建一个 ConfigParser 对象
config.read('config.ini')
color1 = config['plot']['color1']
color2 = config['plot']['color2']
xlabel = config['figure']['xlabel']
ylabel = config['figure']['ylabel']
# width = config['plot']['width']


# -------------------------------------set the config of the figure-------------------------------------------
xlabel = xlabel
ylabel = ylabel
# TODO
title = "Bar Chart Example"
labels = ['A', 'uyguyvigyi', 'C', 'D', 'E','1', '2', '3', '4', '5']# 标签
colors = [color1, color2, 'b', 'y', 'purple','r', 'g', 'b', 'y', 'purple']
ymin = 0
ymax = 200 
width = 0.5

# ------------------------- show these numbers in figure by histogram-----------------------------------------
values = [0 for _ in range(10)]# 初始数据

plt.ion() # turning interactive mode on
graph = plt.bar(labels, values)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.ylim([ymin,ymax])
plt.pause(1)

# ------------------------------------the update loop-------------------------------------------------------
for i in range(10):
	# updating the data
    values = [random.randint(1, 150) for _ in range(10)]

    # save the data
    with open('data.txt', 'a') as file:  # 'a' 表示以追加模式打开文件
        for item in values:
            file.write(str(item) + ' ')
        file.write("\n")

	# removing the older graph
    graph.remove()
	
	# plotting newer graph
    graph = plt.bar(labels, values, color=colors, width=width)
		# calling pause function for 0.25 seconds
    plt.pause(1)


# save
