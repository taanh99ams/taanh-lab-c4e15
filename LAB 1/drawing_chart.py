from matplotlib import pyplot

#1. Prepare data
labels = ["Android", "IOS", "Web"]
values = [300, 400, 300]
colors = ["red", "blue", "yellow"]
explode = [0.1, 0.1, 0.1]     #tinh tien ra khoi tam = thong so x ban kinh

#2. Plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode)

pyplot.axis("equal")



#3. Show
pyplot.show()
