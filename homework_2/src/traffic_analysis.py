"""Traffic Analysis Exercise""" 
import pandas as pd 
import matplotlib.pyplot as plt 


def analyze_traffic(df):
   print(df)
   # 1. Time series analysis:
   df['Day'] = ['Lun', 'Mar','Mer','Gio','Ven','Sab','Dom',
                    'Lun', 'Mar','Mer','Gio','Ven','Sab','Dom',
                    'Lun', 'Mar','Mer','Gio','Ven','Sab','Dom',
                    'Lun', 'Mar','Mer','Gio','Ven','Sab','Dom', 'Lun', 'Mar']
    
   daily_traffic_vis = df.groupby('Day')['Visitors'].mean()
   daily_traffic_bounce_rate = df.groupby('Day')['Bounce_Rate'].mean()


   moving_avg_3_days = df.rolling(window=3)['Visitors'].mean()
   moving_avg_7_days = df.rolling(window=7)['Visitors'].mean()

    
   #2. Bounce rate analysis:
   avg_bounce_rates = df['Bounce_Rate'].mean()
   moving_avg_3_days_br = df.rolling(window=3)['Bounce_Rate'].mean()
   moving_avg_7_days_br = df.rolling(window=7)['Bounce_Rate'].mean()

   corr_traffic_bounce_rate = df['Visitors'].corr(df['Bounce_Rate'])
   high_bounce_rate_period = df.groupby('Day')['Bounce_Rate'].max()
   low_bounce_rate_period = df.groupby('Day')['Bounce_Rate'].min()


   #Visualization
   # Create visualizations
   fig, ax = plt.subplots(2, 2, figsize=(12, 10))

   days = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom']

   # Plot1
   ax[0][0].set_title('Moving Averages')
   ax[0][0].plot(moving_avg_3_days)
   ax[0][0].grid(True, alpha=0.3)
   ax[0][0].legend()
   ax[0][0].set_xlabel('Days')
   ax[0][0].set_ylabel('Traffic Avg')
   ax[0][0].plot(moving_avg_7_days)

      
   # Plot2
   ax[0][1].set_title('Daily Averages')
   ax[0][1].plot(days, daily_traffic_vis)
   ax[0][1].grid(True, alpha=0.3)
   ax[0][1].legend()
   ax[0][1].set_xlabel('Days')
   ax[0][1].set_ylabel('Avg')
   ax[0][1].plot(days, daily_traffic_bounce_rate)

   # Plot3
   ax[1][0].set_title('Bounce Rate Trend')
   ax[1][0].plot(moving_avg_3_days_br)
   ax[1][0].plot(moving_avg_7_days_br)
   ax[1][0].grid(True, alpha=0.3)
   ax[1][0].legend()
   ax[1][0].set_xlabel('Days')
   ax[1][0].set_ylabel('Avg')


   #Plot4
   ax[1][1].scatter(df['Visitors'], df['Bounce_Rate'])
   ax[1][1].set_title('')
   ax[1][1].set_xlabel('Visitors')
   ax[1][1].set_ylabel('Bounce_Rate')
   ax[1][1].grid(True, alpha=0.3)


   plt.show()





   """
    Exercise 4: Website Traffic Analysis with Pandas
    --------------------------------------------
    Task: Analyze website traffic patterns and bounce rates.
    
    Required steps:
    1. Time series analysis:
       - Compute moving averages (3-day and 7-day)
       - Identify weekly patterns
    
    2. Bounce rate analysis:
       - Calculate average bounce rates
       - Correlate bounce rates with traffic
       - Identify high/low bounce rate periods
    
    3. Create visualizations:
       - Traffic trends with moving averages
       - Daily traffic patterns
       - Bounce rate trends
       - Traffic vs bounce rate correlation
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns:
        - Date: datetime index
        - Visitors: daily visitor count
        - Bounce_Rate: daily bounce rate percentage
    
    Expected Output:
    --------------
    1. Four-panel figure showing:
       - Traffic trends with moving averages
       - Average daily traffic patterns
       - Bounce rate trend
       - Correlation scatter plot
    2. Dictionary with traffic statistics
    
    Hint: Use df.rolling for moving averages
   """
   pass
