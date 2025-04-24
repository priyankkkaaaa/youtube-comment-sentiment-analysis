
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiments(df):
    sns.countplot(x='sentiment', data=df, palette='pastel')
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()
