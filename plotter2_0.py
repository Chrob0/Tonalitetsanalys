import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file into a Pandas DataFrame
df = pd.read_excel('G:\My Drive\Skola\Akademisk kommunikation\sentiments.xlsx')

# Filter data by Site URL
df = df[df['Site'] == 'https://dn.se']

# Convert Timestamp to datetime and extract weekday and hour
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Weekday'] = df['Timestamp'].dt.weekday
df['Hour'] = df['Timestamp'].dt.hour



def colormap():
    # Group by weekday and hour and compute average Sentiment
    grouped = df.groupby(['Weekday', 'Hour'])['Sentiment'].mean()

    # Reshape data into a pivot table for plotting
    pivot = grouped.reset_index().pivot(index='Hour', columns='Weekday', values='Sentiment')
    # Plot average Sentiment by weekday and hour
    plt.imshow(pivot, cmap='seismic', aspect='equal')
    plt.colorbar()
    plt.title('Average Sentiment by Weekday and Hour for Aftonbladet')
    plt.xlabel('Weekday')
    plt.ylabel('Hour of Day')
    plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.yticks(range(4), ['00:00', '06:00', '12:00', '18:00'])
    plt.show()



def plot():
    grouped = df.groupby('Weekday')['Sentiment'].mean()
    # Plot average Sentiment by weekday
    plt.plot(grouped.index, grouped.values)
    plt.title('Average Sentiment by Weekday for Aftonbladet')
    plt.xlabel('Weekday')
    plt.ylabel('Sentiment')
    plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.show()

def plotHigh():
    # Group by weekday and compute highest Sentiment
    grouped = df.groupby('Weekday')['Sentiment'].max()

    # Create a bar chart of highest Sentiment by weekday
    plt.plot(grouped.index, grouped.values)
    plt.title('Highest Sentiment by Weekday for Aftonbladet')
    plt.xlabel('Weekday')
    plt.ylabel('Sentiment')
    plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.show()

def plotLow():
    # Group by weekday and compute highest Sentiment
    grouped = df.groupby('Weekday')['Sentiment'].min()

    # Create a bar chart of highest Sentiment by weekday
    plt.plot(grouped.index, grouped.values)
    plt.title('Lowest Sentiment by Weekday for Aftonbladet')
    plt.xlabel('Weekday')
    plt.ylabel('Sentiment')
    plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.show()

colormap()
plot()
plotHigh()
plotLow()