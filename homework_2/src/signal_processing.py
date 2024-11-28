"""Signal Processing Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 

 
 
def analyze_signal(time, clean, noisy):
   ## Calculate basic signal statistics
   mean = np.mean(noisy)
   std = np.std(noisy)
   max_value = np.max(noisy)
   min_value = np.min(noisy)
   SNR = mean/std

   signal_statistics = {
      'mean': mean,
      'std' : std,
      'max value' : max_value,
      'min value' : min_value,
      'SNR' : SNR,
   }
   print(signal_statistics)
   
   ## Process the signal
   windowed_mean = np.convolve(noisy, np.ones(5)/5, mode='same') # convolution with kernel (1/5, 1/5, 1/5, 1/5, 1/5)
   fft_analysis = np.fft.fft(noisy)
   n = fft_analysis.size
   timestep = 0.1
   freq = np.fft.fftfreq(n, d=timestep)

   ## Create visualizations
   fig, ax = plt.subplots(2, 1, figsize=(12, 10))   
   
   ax[0].set_title('Time Domain Signals')
   ax[0].plot(time, noisy, label='Noisy Signal')
   ax[0].plot(time, clean, label='Clean Signal', linestyle='--', color='red')
   ax[0].plot(time, windowed_mean, label='Windowed Signal', linestyle='--', color='green')
   ax[0].grid(True, alpha=0.3)
   ax[0].legend()
   ax[0].set_xlabel('Time (s)')
   ax[0].set_ylabel('Amplitude')

   ax[1].set_title('Frequency Domain Signals')
   ax[1].plot(freq, fft_analysis)
   ax[1].set_title('FFT Analysis')
   ax[1].grid(True, alpha=0.3)
   ax[1].legend()
   ax[1].set_ylabel('Magnitude')
   ax[1].set_xlabel('Frequency (Hz)')

   plt.tight_layout()
   plt.show()