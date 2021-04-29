import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
plt.style.set('ggplot')

#Show the first 5 rows of data
df = pd.read_csv('resulting_data.csv')
df.head()

#strip columns
df.rename(columns=lambda x:x.strip(),inplace=True)

#scatterplot
plt.style.use('ggplot')
plt.figure(figsize=[7,5])
plt.title('The Scatterplot relation between Number of Retweets and Net Score',fontsize=15,fontweight = 'bold')
sns.scatterplot(data=df , y='Number of Retweets',x='Net Score')
plt.show()
