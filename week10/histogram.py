import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'sample_data-213.csv'  
df = pd.read_csv(file_path)


columns = ['Normal_Distribution', 'Uniform_Distribution', 'Exponential_Distribution', 'Poisson_Distribution']



for col in columns:
    
    plt.hist(df[col], bins=30, alpha=1, label=col)  


sns.kdeplot(df['Normal_Distribution'], color='blue', linewidth=2)


plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Distributions')
plt.legend()


plt.show()


