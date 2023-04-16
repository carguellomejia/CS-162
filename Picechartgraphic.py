import matplotlib.pyplot as plot
# set up your lists
numlist = [7, 6, 5, 1]
namelist = ['Dinosaurs', 'humans', 'reptiles', 'plants']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.1, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 95)
plot.axis('equal')
plot.savefig('piechart.png')

