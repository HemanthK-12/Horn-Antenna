import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading data from spectra text file given
df = pd.read_csv('C:\\Users\\heman\\OneDrive\\Desktop\\BITS\\AD ASTRA\\Horn Antennae Practice\\galaxy_21cm_spectrum-20240111T043850Z-001\\spectrum_d_0.69_kpc.txt')

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

plt.scatter(wav, bri)
plt.xlabel('Wavelength(cm)')
plt.ylabel('Intensity(W/m^2)')
plt.title('First Spectra')
plt.xticks(np.arange(min(wav), max(wav), step=(max(wav)-min(wav))/10))
plt.yticks(np.arange(min(bri), max(bri), step=(max(bri)-min(bri))/10))
plt.plot(wav[max_index],bri[max_index], 'ro')
plt.annotate(f'Max: {wav[max_index]}', (wav[max_index],bri[max_index]), textcoords="offset points", xytext=(10,7), ha='center')
plt.grid()
plt.show()

rest_wavelength=21.106114054160
shift_wavelength=h_alpha_wavelength-rest_wavelength
doppler_velocity=(shift_wavelength/rest_wavelength)*299792.458

print(f'Doppler Velocity: {doppler_velocity} km/s.It is negative as it is moving away from you and getting redshifted.')

