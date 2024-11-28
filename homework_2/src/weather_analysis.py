"""Weather Analysis Exercise""" 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

def analyze_weather(df):

   
   # Calculate basic statistics
   monthly_temp_mean = df['Temperature'].mean()
   monthly_total_prec = df['Precipitation']
   # non ho capito in che modo usare pd.cut()
   df['Season'] = ['Winter', 'Winter','Spring','Spring','Spring','Summer','Summer','Summer','Autumn','Autumn','Autumn','Winter']
   temp_prec_correlation = df['Temperature'].corr(df['Precipitation'])

   # Create seasonal analysis
   seasonal_temp_avgs = df.groupby('Season')['Temperature'].mean()
   seasonal_prec_avgs = df.groupby('Season')['Precipitation'].mean()
   extreme_prec_month = df.loc[df["Precipitation"].idxmax(), "Month"]
   extreme_temp_month = df.loc[df["Temperature"].idxmax(), "Month"]

   weat_dict = {
      'Monthly Temperature Mean' : monthly_temp_mean,
      'Monthly Total Precipitation' : monthly_total_prec,
      'Temperature Precipitation Correlation' : temp_prec_correlation,
      'Seasonal Temperature AVGS' : seasonal_temp_avgs,
      'Seasonal Precipitation AVGS' : seasonal_prec_avgs,
      'Extreme Precipitation Month' : extreme_prec_month,
      'Extreme Temperature Month' : extreme_temp_month
   }
   

   # Create visualizations
   fig, ax = plt.subplots(2, 2, figsize=(12, 10))


   # Plot1
   ax[0][0].set_title('Tempearature and Precipitation')
   ax[0][0].plot(df['Month'], df['Temperature'])
   ax[0][0].grid(True, alpha=0.3)
   ax[0][0].legend()
   ax[0][0].set_xlabel('Time (s)')
   ax[0][0].set_ylabel('Temperature')

   ax2 = ax[0][0].twinx()
   ax2.plot(df['Month'], df['Precipitation'])
   ax2.grid(True, alpha=0.3)
   ax2.legend()
   ax2.set_xlabel('Time (s)')
   ax2.set_ylabel('Precipitation')

      

   # Plot2
   plot2_categories = df['Season'].unique()

   plot2_colors_cool = plt.cm.tab10(np.linspace(0, 1, len(plot2_categories)))

   plot2_bars = ax[0][1].bar(plot2_categories, seasonal_temp_avgs, color=plot2_colors_cool)
   ax[0][1].set_title('Bar Plot')
   ax[0][1].set_xlabel('Months')
   ax[0][1].set_ylabel('AVG Temp')

   for bar in plot2_bars:
      height = bar.get_height()
      ax[0][1].text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.0f}',
               ha='center', va='bottom')
      
   # #Plot3
   ax[1][0].hist(df['Temperature'], bins=30, edgecolor='black', alpha=0.7)
   ax[1][0].set_title('Histogram')
   ax[1][0].set_xlabel('Temperature')
   ax[1][0].set_ylabel('Frequency')
   ax[1][0].grid(True, alpha=0.3)

   #Plot4
   ax[1][1].scatter(df['Temperature'], df['Precipitation'])
   ax[1][1].set_title('')
   ax[1][1].set_xlabel('Temperature')
   ax[1][1].set_ylabel('Precipitation')
   ax[1][1].grid(True, alpha=0.3)
   
   plt.show()

