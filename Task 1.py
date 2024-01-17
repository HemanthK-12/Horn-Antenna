import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Reading data from spectra text file given

path = './galaxy_21cm_spectrum-20240111T043850Z-001'

# iterate over files in that path
for filename in os.listdir(path):
    if filename.endswith(".txt"):  # check if the file is a .txt file
        file_path = os.path.join(path, filename)
        df = pd.read_csv(file_path)
        
        
#df = pd.read_csv('C:\\Users\\heman\\OneDrive\\Desktop\\BITS\\AD ASTRA\\Horn Antennae Practice\\galaxy_21cm_spectrum-20240111T043850Z-001\\spectrum_d_0.69_kpc.txt')

wavelength=[]
brightness=[]
for i in range(1,len(df)):
    values=df.iloc[i,0]
    wavelength_brightness=values.split(" ")
    wavelength.append(wavelength_brightness[0])
    brightness.append(wavelength_brightness[1])

wav=np.array(wavelength, dtype=float)
bri=np.array(brightness, dtype=float)

max_index=np.argmax(bri)
h_alpha_wavelength=wav[max_index]

plt.plot(wav, bri)
plt.xlabel('Wavelength(cm)')
plt.ylabel('Intensity(W/m^2)')
plt.title('First Spectra')
plt.xticks(np.arange(min(wav), max(wav), step=(max(wav)-min(wav))/10))
plt.yticks(np.arange(min(bri), max(bri), step=(max(bri)-min(bri))/10))
plt.plot(wav[max_index],bri[max_index], 'ro')
plt.annotate(f'Max: ({wav[max_index]},{bri[max_index]})', (wav[max_index],bri[max_index]), textcoords="offset points", xytext=(10,7), ha='center')
plt.grid()


rest_wavelength=21.106114054160
shift_wavelength=h_alpha_wavelength-rest_wavelength
doppler_velocity=(shift_wavelength/rest_wavelength)*299792.458

print(f'Doppler Velocity: {doppler_velocity} km/s.It is negative as it is moving away from you and getting redshifted.')

#Gaussian Fit
def gaussian_function(x,a,mu,sigma):
    return a*np.exp(-(x-mu)**2/(sigma**2))

#popt,pcov=curve_fit(gaussian_function,wav,bri,p0=[5942.1031736225705,21.00243592095089,0.000810641678294])
popt,pcov=curve_fit(gaussian_function,wav,bri,p0=[np.max(bri),np.mean(wav),np.std(wav)])

print(pcov)
a_opt,mu_opt,sigma_opt=popt
x_opt=np.linspace(min(wav),max(wav),100)
y_opt=gaussian_function(x_opt,a_opt,mu_opt,sigma_opt)

plt.plot(x_opt,y_opt,'r')
plt.show()

