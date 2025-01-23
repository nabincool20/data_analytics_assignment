
################ Data cleaning the Iris dataset #################
from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load iris dataset
iris = datasets.load_iris()
# Since this is a bunch, create a dataframe
iris_df=pd.DataFrame(iris.data)
iris_df['class']=iris.target

iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#### ===> TASK 1: here - add two more lines of the code to find the number and mean of missing data
cleaned_data = iris_df.dropna(how="all", inplace=True) # remove any empty lines
missing_data_number = iris_df.isnull().sum()
print("The missing number is :", missing_data_number)


missing_data_mean = iris_df.isnull().mean()
print("The missing data mean is :", missing_data_mean)

iris_X=iris_df.iloc[:5,[0,1,2,3]]
print(iris_X)

### TASK2: Here - Write a short readme to explain above code and how we can calculate the corrolation amoung featuers with description

correlation_matrix = iris_df.corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()