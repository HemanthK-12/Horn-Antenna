

# Galaxy 21cm Spectrum Data

This repository contains text files with spectral data from a 21cm line survey of various galaxies. Each file in the `galaxy_21cm_spectrum-20240111T043850Z-001` directory represents a different galaxy or a different observation.

## File Naming Convention

Each file is named using the convention `spectrum_d_XYZ_kpc.txt`, where `XYZ` represents the distance to the galaxy in kiloparsecs (kpc). For example, a file named `spectrum_d_0.69_kpc.txt` contains the spectral data for a galaxy that is 0.69 kiloparsecs away.I've collected data of galaxies which are  ['0.69', '1.38', '2.06', '2.72', '3.35', '3.96', '4.54', '5.11', '5.62', '6.06', '6.50', '6.87'] kpc away in this project. 

## File Format

Each file is a text file containing two columns of numerical datathe first being the wavelength of light emitted and the second being the intensity of the light reflected in the context of a 21cm line survey.

## Python Script

The python script task1_solution.py lists out the gaussian fits for all the plots of the galaxies listed in the folder.The plot is shown below:

![Task1_GaussianFit](https://github.com/HemanthK-12/Horn-Antenna/assets/134306795/7240ff95-b866-46e2-bff1-92dd14c6c54f)
