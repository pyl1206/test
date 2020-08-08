import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
#注意线段宽度是用linewidth,点的大小是直接用小写s,这里将颜色设置为随x变化的颜色，cnap是指定用什么颜色.
plt.scatter(x_value, y_value, c=y_value,cmap=plt.cm.Blues,edgecolor='none',s=20)
plt.title("scatter", fontsize=24)
plt.xlabel("X", fontsize=14)
plt.ylabel("Y", fontsize=14)
plt.tick_params(axis='both',labelsize=10)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
#下面这两个句子一个是展示图表，一个是保存成图片，两者一起用的时候先保存在展示，不能先展示在保存。
#plt.show()
plt.savefig('scatter.png',bbox_inches='tight')
plt.show()
