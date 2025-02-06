import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

ECG = "S0603_DT_V2"

# Leer la señal desde el archivo
lecturasignal = wfdb.rdrecord(ECG)
signal = lecturasignal.p_signal[:,0]  
fs = lecturasignal.fs  
numero_datos = len(signal) 
muestreo=int(5*fs)

# Grafica la señal muscular del gastrocnemio
time = [i / fs for i in range(numero_datos)]  
signal = signal[:muestreo]
time = time[:muestreo]
plt.figure(figsize=(12,4))
plt.plot(time, signal, color="violet")

plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mv)")
plt.title("Señal Biomédica EMG bases de datos physionet")
plt.grid()
plt.show()


# Histograma solo

plt.figure(figsize=(8, 4))
plt.hist(signal, bins=50, color='orange', alpha=0.7, edgecolor='black', density=True)
plt.xlabel("Amplitud de la señal")
plt.ylabel("Frecuencia normalizada")
plt.title("Histograma de la señal")
plt.grid()

# Funcion de probabilidad
kde = gaussian_kde(signal)
x_vals = np.linspace(min(signal), max(signal), 1000)
pdf_vals = kde(x_vals)
plt.plot(x_vals, pdf_vals, color='brown', label="")
plt.show()


# Calculo a mano de la media
suma=0
for i in range(len(signal)):
    suma += signal[i]
media = suma/ len(signal)
print(f"Media de la señal: {media:.4f}")

# Calculo de n
longitud_vector = 0
for _ in signal:
    longitud_vector +=1
print(f"Longitud del vector: {longitud_vector}")

# Desviacion estandar
desviacion = 0
for i in range(len(signal)):
    desviacion += (signal[i] - media) ** 2
desviacion_estandar = (desviacion/len(signal)) ** 0.5
print(f"Desviación estándar: {desviacion_estandar:.4f}")

coeficiente_de_variacion = desviacion_estandar/ media if media != 0 else float ('nan')
print(f"Coeficiente de variación: {coeficiente_de_variacion:.4f}")


# calculos con funciones de python
media_librerias = np.mean(signal)
longitud_vector_librerias = len(signal)
desviacion_librerias = np.std(signal)
coeficiente_variacion_librerias = desviacion_librerias / media_librerias if media_librerias != 0 else np.nan

print(f"Media de la señal con librerias: {media_librerias:.4f}")
print(f"Longitud del vector con librerias: {longitud_vector_librerias}")
print(f"Desviación estándar con librerias: {desviacion_librerias:.4f}")
print(f"Coeficiente de variación con librerias: {coeficiente_variacion_librerias:.4f}")

# Contaminaciones de ruido gaussiano y SNR
ruido_media = 0  # Media del ruido
ruido_std = 0.2  # Desviación estándar del ruido (ajustar según el nivel de ruido deseado)

# Generar ruido gaussiano
ruidoG = np.random.normal(ruido_media, ruido_std, len(signal))

señalCRG = signal + ruidoG
plt.figure(figsize=(10, 4))
plt.plot(time, signal, color="violet")
plt.plot(time, señalCRG, color="blue")
plt.xlabel("Tiempo(s)")
plt.ylabel("Amplitud(mV)")
plt.title("Señal fisiológica con ruido gaussiano")
plt.grid()
plt.show()

potSeñal = np.mean(signal ** 2)
potGaus = np.mean(ruidoG ** 2)
SNRGaus = 10*np.log10(potSeñal/potGaus)
print(f"SNR para la señal contaminada con ruido tipo gaussiano: {SNRGaus:.2f} dB")

# Contaminaciones de ruido impulso y SNR
num_impulsos = int(len(signal) * 0.05)  # Proporción de impulsos (1% de la señal)
amplitud_max = np.max(signal) * 0.5  # Amplitud de los impulsos (ajustable)

# Generar ruido impulsivo
ruidoI = np.zeros(len(signal))
posiciones = np.random.randint(0, len(signal), num_impulsos)  # Posiciones aleatorias
valores_impulsos = np.random.choice([-amplitud_max, amplitud_max], num_impulsos)  # Positivos y negativos
ruidoI[posiciones] = valores_impulsos  # Insertar los impulsos en la señal

señalCRI = signal + ruidoI
plt.figure(figsize=(10, 4))
plt.plot(time, signal, color="violet")
plt.plot(time, señalCRI, color="red")
plt.xlabel("Tiempo(s)")
plt.ylabel("Amplitud(mV)")
plt.title("Señal fisiológica con ruido impulso")
plt.grid()
plt.show()

potImp = np.mean(ruidoI ** 2)
SNRImp = 10*np.log10(potSeñal/potImp)
print(f"SNR para la señal contaminada con ruido tipo impulso: {SNRImp:.2f} dB")

# Contaminaciones de ruido artefacto y SNR
# primer artefacto, Interferencia de red eléctrica (60 Hz)
frecuencia_red = 50  # Frecuencia de la corriente alterna (puede ser 60 Hz en algunos países)
artefacto_red = 0.05 * np.sin(2 * np.pi * frecuencia_red * np.arange(len(signal)) / fs)

# segundo artefacto, pérdida de contacto del electrodo (picos aleatorios)
num_picos = int(len(signal) * 0.005)  # 0.5% de la señal con picos
posiciones_picos = np.random.randint(0, len(signal), num_picos)
artefacto_electrodo = np.zeros(len(signal))
artefacto_electrodo[posiciones_picos] = np.random.choice([-1, 1], num_picos) * np.max(signal) * 1.5

señalCRA = signal + artefacto_electrodo + artefacto_red
plt.figure(figsize=(10, 4))
plt.plot(time, signal, color="violet")
plt.plot(time, señalCRA, color="black")
plt.xlabel("Tiempo(s)")
plt.ylabel("Amplitud(mV)")
plt.title("Señal fisiológica con ruido artefacto")
plt.grid()
plt.show()

potART = np.mean(artefacto_electrodo+artefacto_red ** 2)
SNRART = 10*np.log10(potSeñal/potART)
print(f"SNR para la señal contaminada con ruido tipo artefacto: {SNRART:.2f} dB")



