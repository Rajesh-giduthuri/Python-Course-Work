#matplotlib : to visualize the data in the form of graphical representation chart

#Graphs / Chart :

import matplotlib.pyplot as plt
months=["Jan","Feb","Mar","Apr"]
sales=[25,32,28,45]

#--> Line plot : show changes over time
# plt.plot(months,sales,marker="o",color="orange") #marker for dot (marker="*")
# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.grid(color="yellow")
# plt.show()

#--> Bar graph : compare values
# plt.bar(months,sales,color="g")
# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()

# plt.barh(months,sales,color="b")
# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()

#--> Pie chart : show percentages
# plt.pie(sales,labels=months,startangle=90,autopct="%1.0f%%")
# plt.title("Monthly Sales")
# plt.show()

#--> Histogram : show data distribution
# marks=[35,42,44,50,53,60,66,70,72,80,84]
# plt.hist(marks,bins=5,color="orange")
# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()

#--> Scatter plot : show relationships on numarical data
# plt.scatter(months,sales,color="r",marker="*")
# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.grid(color="yellow")
# plt.show()

#--> Box plot : min , max , median , outliers
# charge=[2,35,40,48,65,80,150]
# plt.boxplot(charge)
# plt.show()

#--> Heatmap : represent values using diff shades/intensities
# park=[
#     [80,70,75,90],
#     [60,62,85,75],
#     [90,80,70,95]
# ]
# plt.imshow(park)
# plt.colorbar()
# plt.title("PARK")
# plt.show()

#--> Subplots : combination of two or more graphs
fig,ax=plt.subplot(2,2,figsize=(18,6))
ax[0,0].plot([1,2,3],[10,20,15])
ax[0,0].set_title("Line")

ax[0,1].bar(["A","B","C"],[10,20,15])
ax[0,1].set_title("Bar")

ax[1,0].scatter([1,2,3],[10,20,15])
ax[1,0].set_title("Scatter")

ax[1,1].barh([1,2,3],[10,20,15])
ax[1,1].set_title("Bar")

plt.show()