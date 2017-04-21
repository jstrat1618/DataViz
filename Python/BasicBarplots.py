
# coding: utf-8

# In[1]:

#Let’s make a basic barplot of two lists the list y. 
#We’ll use the list x to provide x coordinates for the boxplot, but this is not a variable of interest.
import matplotlib.pyplot as plt
 
x=[1,2]
y=[8,3]
 
#A Basic barplot
plt.bar(x,y)
plt.show()


# In[4]:

#Let’s say we want to compare the Golden State Warriors shoot 55% at home and 49% on the road.
#Here's how we would plot this.
gsw=[55,49]
xgsw=[0,1]
labs=['Home', 'Away']

plt.bar(xgsw, gsw)
 
#Let’s change the axses
#Get current axses
axes = plt.gca()
#Change the x axsis
axes.set_xlim([-1,3])#Note you cannot use this function without plt.gca()
#However, we don’t want the x-axis to say be numbers; we want it to say Home or Away
plt.xticks(xgsw, labs)
plt.show()


# In[5]:

#Suppose the LAL are 48% at Home and 43% Away. Let’s incorporate both teams into a bar plot
lal=[48,43]
xlal=[2,3]
 
plt.bar(xgsw, gsw, label="GSW", color="gold")
plt.bar(xlal, lal, label="LAL", color="purple")
#Get current axses
axses=plt.gca()
#Change x-axis
axses.set_xlim([-1,4])
#Now we need new labels on the x-axis
xlabs=[0,1,2,3]
newLabs=['H','A','H','A']
plt.xticks(xlabs, newLabs)
#Legend to distiguish teams
plt.legend()
#Label both axses
plt.xlabel("H= Home   A= Away")
plt.ylabel("Shooting Percentage")
#Add a title
plt.title("LAL vs GSW \n Shooting Percentage") #\n moves to the next line
plt.show()


# In[ ]:



