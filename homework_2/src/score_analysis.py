"""Score Analysis Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 
 
def analyze_scores(scores):
   # Calculate statistics

   students_avg_performance = []
   for el in scores:
      students_avg_performance.append(np.mean(el))
   overall_perf = np.mean(students_avg_performance)


   scores_transpose = np.transpose(scores)
   subjects_average_score = []
   for el in scores_transpose:
      subjects_average_score.append(np.mean(el))


   # Analyze score distribution
   std_scores = np.std(students_avg_performance)
   high_perf_student = students_avg_performance.index(np.max(students_avg_performance))
   low_perf_student = students_avg_performance.index(np.min(students_avg_performance))

   score_ranges = []
   for el in scores_transpose:
      score_ranges.append([np.min(el), np.max(el)])


   # Create visualizations
   fig, ax = plt.subplots(2, 2, figsize=(12, 10))

   # Plot1

   plot1_categories = []
   for el in students_avg_performance:
      plot1_categories.append(str(students_avg_performance.index(el)+1))

   plot1_colors_cool = plt.cm.tab10(np.linspace(0, 1, len(plot1_categories)))

   plot1_bars = ax[0][0].bar(plot1_categories, students_avg_performance, color=plot1_colors_cool)
   ax[0][0].set_title('Bar Plot')
   ax[0][0].set_xlabel('Students')
   ax[0][0].set_ylabel('AVG Scores')

   for bar in plot1_bars:
      height = bar.get_height()
      ax[0][0].text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.0f}',
               ha='center', va='bottom')
      

   # Plot2
   plot2_categories = []
   for el in subjects_average_score:
      plot2_categories.append(str(subjects_average_score.index(el)+1))

   plot2_colors_cool = plt.cm.tab10(np.linspace(0, 1, len(plot2_categories)))

   plot2_bars = ax[0][1].bar(plot2_categories, subjects_average_score, color=plot2_colors_cool)
   ax[0][1].set_title('Bar Plot')
   ax[0][1].set_xlabel('Subjects')
   ax[0][1].set_ylabel('AVG Scores')

   for bar in plot2_bars:
      height = bar.get_height()
      ax[0][1].text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.0f}',
               ha='center', va='bottom')
      
   #Plot3
   ax[1][0].hist(scores, bins=30, edgecolor='black', alpha=0.7)
   ax[1][0].set_title('Histogram')
   ax[1][0].set_xlabel('Scores')
   ax[1][0].set_ylabel('Frequency')
   ax[1][0].grid(True, alpha=0.3)

   #Plot4
   ax[1][1].boxplot(scores_transpose)

   
   plt.show()


   statistical_analysis = {
      'Average Student Performance' : students_avg_performance,
      'Average Subject Score' : subjects_average_score,
      'Lowest Performance Student' : low_perf_student,
      'Highest Performance Student' : high_perf_student,
      'STD' : std_scores,
      'Score Ranges' : score_ranges
   }