import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Reading data from spectra text file given

path = 'C:\\Users\\heman\\OneDrive\\Desktop\\BITS\\AD ASTRA\\Horn Antennae Practice\\galaxy_21cm_spectrum-20240111T043850Z-001'

color=['blue','green','red','cyan','magenta','yellow','k','pink','orange','gray','brown','lime']
# iterate over files in that path
j=0
files=[]
for filename in os.listdir(path):
    files.append(filename[11]+filename[12]+filename[13]+filename[14])
for filename in os.listdir(path):
    if filename.endswith(".txt"):  # check if the file is a .txt file
        file_path = os.path.join(path, filename)
        df = pd.read_csv(file_path)
        wavelength=[]
        brightness=[]
        for i in range(497,762):
            values=df.iloc[i,0]
            wavelength_brightness=values.split(" ")
            wavelength.append(wavelength_brightness[0])
            brightness.append(wavelength_brightness[1])

        wav=np.array(wavelength, dtype=float)
        bri=np.array(brightness, dtype=float)

        max_index=np.argmax(bri)      
        h_alpha_wavelength=wav[max_index]

        #plt.plot(wav, bri)
        plt.xlabel('Wavelength(cm)')
        plt.ylabel('Intensity(W/m^2)')
        plt.title('First Spectra')
        plt.xticks(np.arange(20.9995,21.0230, step=0.00235))
        plt.yticks(np.arange(min(bri),5943, step=594.3))
        plt.plot(wav[max_index],bri[max_index],'r')
        #plt.annotate(f'{filename[11]}{filename[12]}{filename[13]}{filename[14]}', (wav[max_index],bri[max_index]), textcoords="offset points", xytext=(10,7), ha='center')
        plt.grid()


        rest_wavelength=21.106114054160
        shift_wavelength=h_alpha_wavelength-rest_wavelength
        doppler_velocity=(shift_wavelength/rest_wavelength)*299792.458

        #print(f'Doppler Velocity: {doppler_velocity} km/s.')

        #Gaussian Fit
        def gaussian_function(x,a,mu,sigma):
            return a*np.exp(-(x-mu)**2/(sigma**2))

        #popt,pcov=curve_fit(gaussian_function,wav,bri,p0=[5942.1031736225705,21.00243592095089,0.000810641678294])
        popt,pcov=curve_fit(gaussian_function,wav,bri,p0=[np.max(bri),np.mean(wav),np.std(wav)])

        #print(pcov)
        a_opt,mu_opt,sigma_opt=popt
        x_opt=np.linspace(min(wav),max(wav),100)
        y_opt=gaussian_function(x_opt,a_opt,mu_opt,sigma_opt)
        str=filename[11]+filename[12]+filename[13]+filename[14]
        plt.plot(x_opt,y_opt,color=color[j],label=str)      
        j+=1

plt.legend()
plt.show()