# ANÁLISIS DE DATOS ELECTROMIOGRÁFICOS EN UN ESTUDIO DE TAI CHI 

## DESCRIPCIÓN 

En el presente escrito, se muestra la medición y explicación de los estadísticos de una señal dirigida específicamente al procesamiento digital de señales. 

Como fundamento de este repositorio se utilizó una base de datos de una señal electromiográfica tomada de Physionet, sobre un estudio clínico que investigó los efectos inmediatos en un grupo de 60 pacientes luego de practicar una sesión de Tai Chi por primera vez. Como resultado de esta recopilación de datos luego de exponer a los pacientes a caminar en dos condiciones diferentes aleatoriamente, como caminar normalmente por diez minutos o durante minuto y medio mientras resolvían verbalmente restas matemáticas, se pudo estudiar la variabilidad en el tiempo de cada uno de los pasos dados relacionado con la velocidad de la marcha para poder evaluar la salud de la movilidad, el funcionamiento de los músculos y su debida contracción para demostrar que esta práctica puede llegar a  mejorar la movilidad del paciente.  

## DESARROLLO 

Para la implementación este laboratorio se hizo uso de un entorno de desarrollo integrado multiplataforma de código abierto llamado “Spyder” el cuál trabaja con el lenguaje de programación de Python y es el que nos permite realizar el cálculo y por consiguiente el análisis de los datos del estudio científico. 

Primeramente, se deben de descargar los archivos que contienen los datos del ya mencionado estudio los cuales están adjuntos en el presente repositorio y tienen como nombre “S0603_DT_V2.dat” y “S0603_DT_V2.hea”. Después de ello para que el código pueda acceder a esta información usamos las siguientes líneas de código que, además nos permite graficarlos para evidenciarlos de una manera visual y ver las contracciones en el músculo estudiado. 

  
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

![alt](SeñalBiologica.png)
Gráfica de la electromiografía en funcion de tiempo.

### HISTOGRAMA Y FUNCIÓN DE PROBABILIDAD
![alt](Histograma.png)

Estadísticamente un histograma cumple la función de determinar el centro, la extensión y forma de un grupo de datos tomados, esto con el fin de visualmente poder determinar la función de normalidad y así comprobar valores atípicos en la toma.  La gráfica programada, ayuda a concluir que la señal tomada proviene de un músculo de baja activación y que tiene picos de mayor actividad, ya que visualmente se observa que es sesgada a la derecha indicando así que la adquisición valores de una señal con una oscilación de pequeñas muestras de amplitud, presentando algunos eventos de mayor intensidad, indicando que la señal del gastrocnemio referencia un músculo en reposo que en ausencia de una contracción la actividad muscular es mínima.  

Para el cálculo manual se grafica la información tomada en un diagrama de columnas para poder determinar la frecuencia de los datos. Para calcular el histograma o programar su gráfica en Python, se hizo uso de la siguiente función:  

     plt.figure(figsize=(8, 4))
     plt.hist(signal, bins=50, color='orange', alpha=0.7, edgecolor='black', 
     density=True)
     plt.xlabel("Amplitud de la señal")
     plt.ylabel("Frecuencia normalizada")
     plt.title("Histograma de la señal")
     plt.grid()


Haciendo uso de la función “plt.xlabel("Amplitud de la señal")” para poder crear la etiqueta de la amplitud de la señal en el eje x, y la función “plt.ylabel("Frecuencia normalizada")” para marcar que el eje y será la gráfica correspondiente a la frecuencia de la toma de datos. Es importante recalcar que el término “plt” es el encargado de dibujar el histograma. 

 

### FUNCION DE PROBABILIDAD 

En estadística, una función de probabilidad se encarga de devolverle la probabilidad a una función de que una variable aleatoria discreta sea semejante a un valor en específico, mostrando así un espacio muestral (X) relacionado con la probabilidad de que se asuma.  

Para calcular manualmente se cumple la siguiente expresión: 

    # Funcion de probabilidad
    kde = gaussian_kde(signal)
    x_vals = np.linspace(min(signal), max(signal), 1000)
    pdf_vals = kde(x_vals)
    plt.plot(x_vals, pdf_vals, color='brown', label="")
    plt.show()


Usando “Kde” para hacer un estimado de la distribución de probabilidad, “x_vals = np.linspace(min(signal)” evalúa el valor mpinimo y máximo de la señal, y “pdf_vals = kde(x_vals)” representa la probabilidad en los puntos determinados.  

 

### MEDIA 

La media o también conocida como la media aritmética de los datos, es calculada como la suma de todos los valores obtenidos dividido por la cantidad de datos; en el contexto de este estudio, nos proporciona información de la actividad eléctrica promedio del gastrocnemio. Este valor nos podría indicar que tan intensamente está trabajando el músculo.  

Este valor fue calculado de manera tanto manual como por medio de funciones matemáticas y estadísticas ya integradas dentro de “Python”. Para el cálculo manual se hace una sumatoria de todos los datos por medio de un ciclo “for” y se divide por la cantidad de datos, el cual es calculado gracias a la función “len()”. Con respecto al cálculo directo con funciones de “Python” se utiliza una función integrada en las librerías de “numpy” la cual es “numpy.mean()”. Todos estos cálculos y resultados se muestran a continuación. 

      # Cálculo a mano de la media
      suma=0
      for i in range(len(signal)):
          suma += signal[i]
      media = suma/ len(signal)
      print(f"Media de la señal: {media:.4f}")
      
      # Cálculos con funciones de python
      media_librerias = np.mean(signal)
      
      # Resultados
      Media de la señal: -0.0005
      Media de la señal con librerias: -0.0005


### DESVIACIÓN ESTÁNDAR
La desviación estándar nos muestra que tanto se alejan los datos de las muestras con respecto a la media, en el contexto de la electromiografía nos puede decir la consistencia de la actividad muscular, que tanto cambio hay en la actividad muscular y si puede ser de manera impredecible por contracciones musculares irregulares. 

Para el cálculo manual se hace una sumatoria de la resta de cada uno de los datos con la media obtenida con anterioridad, se eleva al cuadrado, se divide por la cantidad de datos y por último se le saca la raíz. Para el cálculo directo de “Python” se implementa la función “numpy.std()” nuevamente perteneciente de la librería de “numpy”. A continuación, se presenta la respectiva programación y solución obtenida. 

      # Desviacion estandar
      desviacion = 0
      for i in range(len(signal)):
          desviacion += (signal[i] - media) ** 2
      desviacion_estandar = (desviacion/len(signal)) ** 0.5
      print(f"Desviación estándar: {desviacion_estandar:.4f}")
      
      # Desviación estándar con funciones de python
      desviacion_librerias = np.std(signal)
      print(f"Desviación estándar con librerias: {desviacion_librerias:.4f}")
      
      # Resultados
      Desviación estándar: 0.0752
      Desviación estándar con librerias: 0.0752

### COEFICIENTE DE VARIACIÓN
Por último, el coeficiente de variación se define como una medida de dispersión que hace una comparación de los valores obtenidos de la desviación estándar y la media por medio de un cociente y si se desea dar como un porcentaje se multiplica por 100. Hablando con el EMG, este es más usado para comparar valores y estudios de diferentes pacientes con diferentes valores de actividades musculares. 

El cálculo manual consiste en realizar el cociente entre la desviación estándar y la media, como se explicó anteriormente y con “Python” simplemente se realiza esa división entre los valores obtenidos en los ítems anteriores con ayuda de “numpy”. Los respectivos códigos, cálculos y resultados se muestran enseguida. 

      # Cálculo manual
      coeficiente_de_variacion = (desviacion_estandar/ media) if media != 0 else float ('nan')
      print(f"Coeficiente de variación: {coeficiente_de_variacion:.4f}")
      
      # Cálculo con funciones de Python
      coeficiente_variacion_librerias = (desviacion_librerias / media_librerias) if media_librerias != 0 else np.nan
      print(f"Coeficiente de variación con librerias: {coeficiente_variacion_librerias:.4f}")
      
      # Resultados obtenidos
      Coeficiente de variación: -151.2735
      Coeficiente de variación con librerias: -151.2735

## SNR
### SNR Gaussiano
![alt](RuidoGaussiano.png)
El SNR gaussiano es un tipo de ruido que se caracteriza por tener una distribución gaussiana en todas las frecuencias tomadas, modelándose con una función de media y varianza cero para lograr estipular la intensidad del ruido en la señal de entrada.  
La fórmula del SNR es la siguiente: 

SNR=10⋅log10 (potencia media de señal/ potencia media de ruido) 

Indicando así que al obtener una mayor SNR la señal será más limpia y será menos dañada por el ruido.  

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
Primero se generó el ruido con la función “ruidoG = np.random.normal(ruido_media, ruido_std, len(signal))” la cual simula la presencia de interferencia en la señal tomada, de modo que a mayor “ruido_std” se generará más ruido y será directamente proporcional a un SNR menor. Cabe recalcar que la función “señalCRG = signal + ruidoG” genera la suma de la señal original y la que tiene el ruido, luego de graficar, la señal original se verá color violeta y la contaminada será azul.  

 ### SNR Impulso
![alt](RuidoImpulso.png)

El ruido impulso se caracteriza principalmente por tener picos de gran amplitud y corta duración que son asignados de manera fortuita, en el mismo rango de datos de la señal original.  

En la programación: 
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
Con la función “num_impulsos = int(len(signal) * 0.05) # Proporción de impulsos (1% de la señal)” se define la cantidad de impulsos que se añadirán a la señal  y con “amplitud_max = np.max(signal) * 0.5 # Amplitud de los impulsos (ajustable)” se determina que la amplitud áxima de los impulsos será el 50% del valor máximo de la señal, evitando así que los impulsos demasiado grandes dañen la señal original. Se resalta que “posiciones = np.random.randint(0, len(signal), num_impulsos) # Posiciones aleatorias” se usa para asignar de manera aleatoria un vector dentro de la señal donde se agregará el ruido (sumarle impulsos), para finalmente sumarlas en la función “señalCRI = signal + ruidoI”. Finalmente, la señal original aparece en color violeta, mientras que la roja será el ruido añadido, ayudando a evidenciar, que los picos abruptos son los impulsos que se agregaron aleatoriamente.  


### SNR Artefacto
![alt](RuidoArtefacto.png)

La SNR artefacto, es una medición que relaciona la potencia de la señal fisiológica capturada y la potencia del ruido añadido por “artefactos”, los cuales clínicamente son causados por la mala colocación de los electrodos a la hora de la captura EMG sobre el paciente.  
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
Utilizando la función “frecuencia_red = 50” para generar el ruido de una amplitud de 0.05, para, como se explicó anteriormente, evitar que el ruido predomine sobre la señal. Con la función “posiciones_picos = np.random.randint(0, len(signal), num_picos) artefacto_electrodo = np.zeros(len(signal)) artefacto_electrodo[posiciones_picos] = np.random.choice([-1, 1], num_picos) * np.max(signal) * 1.5” se simula, la mala colocación del electrodo, causando que haya una generación de picos aleatorios, y así por último usar la función “señalCRA = signal + artefacto_electrodo + artefacto_red” para sumar el ruido a la señal original, y, como se evidencia en la gráfica, ver la señal original en color violeta, y la señal del ruido artefacto en color negro, creando una interferencia sinusoidal de manera aleatoria.  


## INSTRUCCIONES 

1) En primer lugar descargar o copiar y pegar el código de Python subido en este repositorio, el cuál esta guardado como "lab1V1.py", en el compilador que desee preferiblemente "Spyder". Cabe recalcar que debe asegurarse que se encuentren las librerias enlistadas en los requerimientos para que pueda compilarse adecuadamente el programa y muestre tanto las gráficas deseadas como los resultados de los cálculos.

2) Descargar los archivos que contienen los datos de la señal electromiográfica incluidos también en el presente repositorio con el nombre de “S0603_DT_V2.dat” y “S0603_DT_V2.hea”. Se aconseja que se guarden los archivos de este inciso y el anterior en la misma carpeta para su fácil acceso.

3) Correr el programa, esperar a que se compile por completo y si todo está en orden, se verán los resultados en el terminal de comandos de la manera que se muestra en la siguiente figura y sus respectivas gráficas.

![alt](terminal.jpg)

## REQUERIMIENTOS
- Python 3.11
- Spyder 6.0
- Librerias como: wfdb, matplotlib, numpy, scipy.stats 
## REFERENCIAS
[1] Histograma. (s. f.). Introducción A la Estadística | JMP. https://www.jmp.com/es_co/statistics-knowledge-portal/exploratory-data-analysis/histogram.html 

[2] Probabilidad: qué es, fórmula, tipos, teorías - Ferrovial. (2022, 2 noviembre). Ferrovial. https://www.ferrovial.com/es/stem/probabilidad/ 

[3] Iqbal, S., Khan, T. M., Naveed, K., Naqvi, S. S., & Nawaz, S. J. (2022). Recent trends and advances in fundus image analysis: A review. Computers In Biology And Medicine, 151, 106277. https://doi.org/10.1016/j.compbiomed.2022.106277 
## AUTORES
- Juan Diego Clavijo Fuentes
  est.juan.dclavijjo@unimilitar.edu.co
- Sofia Olivella Moreno
  est.sofia.olivella@unimilitar.edu.co
