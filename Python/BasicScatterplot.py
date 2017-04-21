
# coding: utf-8

# In[1]:

#Here is a basic scatter plot in python 3 using the the matplot lib library. 
#First, I define the lists x and y and then plot them.
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,3,2,4,6]
 
#A Basic scatter plot
plt.scatter(x,y)
#Add title and axis labels (the decor)
plt.title('This is the  Title!')
plt.xlabel('X label')
plt.ylabel('Y label')
#show plot
plt.show()


# In[2]:

#In python, if you want a line plot, you simply need to use the plot function
plt.plot(x,y)
plt.title('This is the  Title!')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()


# In[5]:

#Let's make another pair of x and y's that's just stacked on top of the other
x1=x
y1=[]
for i in range(len(y)):
    temp=y[i] +1
    y1.append(temp)
 
 
#Let's distnighuish with a different color and a legend
plt.plot(x,y, label='x & y')#The label is for the legend
plt.plot(x1, y1, color='g', label='x1 & y1')
 
#Add the decor
plt.title('This is the  Title!')
#plt.legend()#Simply shows legend in the upper right corner
#If you want the legend in the upper left like I do in this case run the next 2 lines
ax = plt.subplot(111)
ax.legend(loc='upper left')#shows legend in upper left
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()


# In[ ]:



