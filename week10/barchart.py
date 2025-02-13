import matplotlib.pyplot as plt
categories=['A','B','C','D']
values = [3,7,1,8]
plt.bar(categories, values, color='skyblue')
plt.xlabel('categories')
plt.ylabel('Values')
plt.title('Bar chart Example')
plt.show()