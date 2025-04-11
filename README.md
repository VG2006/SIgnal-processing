I had to filter the given audio which is modulated using AM.

**Approach:**
I need to remove the carrier frequency. Carrier frequency is generally the frequency associated with the highest peak in FFT plot. After finding the carrier frequency I need to demodulate it. For demodulation we have to multiply signal data with cosine wave of carrier frequency (i.e Demodulated = data*cos(2*pi*fc*t)). To get the original audio we need to apply lowpass filter which recovers the baseband signal we require. Finally the demodulated and filtered signal are normalized and saved as .wav file

**Code Implementation:**
I used python as my coding language. First I read the signal and collect the data. Demodulated signal plot is plotted.

![Modulated: Noisy Signal](https://github.com/user-attachments/assets/849660a6-d252-4e67-9f4c-95792ec0c848)

then I transformed it into FFT. FFT of demodulated is plotted.

![FFT of Modulated](https://github.com/user-attachments/assets/20ee351a-338e-46bd-a2e3-dd521e683827)

The carrier frequency is estimated by
 locating the peak in the magnitude spectrum. Then the signal is multiplied with cosine wave of carrier frequency which shifts the baseband component to 0Hz. Demodulated signal is plotted. 

 ![Demodulated](https://github.com/user-attachments/assets/f8af0bb7-438c-488a-8436-e9f1d6221e11)


By applying Butterworth low-pass filter high frequency components are removed which helps us recover original audio. Then finally filtered signal is normalized and saved as .wav file.

filtered signal 

![Filtered Signal](https://github.com/user-attachments/assets/bbf66e7d-ed84-4251-a8db-c17f161c386e)



