import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

###Texto de introducción al programa###
st.markdown("<h1 style='text-align: center; color: blue;'>Simulación de trayectoria de un proyectil lanzado por un volcán</h1>", unsafe_allow_html=True)
st.markdown("<h2> Introducción </h2>", unsafe_allow_html=True)
st.markdown("Un volcán es definido como una abertura de la corteza terrestre por donde sale magma, fragmentos de piedra y demás gases (UNAM, 2015). \
    Un volcán puede representar un riesgo para la población y demás ecosistemas si no se tiene la debida precaución y conocimiento de sus posibles eventos y fenómenos. \
        Hoy en día, y gracias a la tecnología, se pueden hacer distintos modelos para predecir el comportamiento de los volcanes y el alcance, así como el nivel del peligro, que éstos pueden llegar a tener. \
            En esta investigación se intentó resolver la incógnita sobre el alcance de la trayectoria descrita por un proyectil disparado desde el cráter del volcán Popocatépetl\
                mediante la creación de una simulación interactiva para así determinar si estos proyectiles son una amenaza para la Ciudad de México y demás entidades en la periferia.")
st.markdown("En esta simulación se intentará explicar y graficar el movimiento de un proyectil que tiene resistencia al aire al ser lanzado desde el cráter de un volcán.")

st.markdown("<h2> Metodología </h2>", unsafe_allow_html=True)
st.markdown("Para la consolidación de este trabajo se realizó una investigación previa sobre el comportamiento de las erupciones volcánicas, los tipos de posibles proyectiles arrojados específicamente por el volcán Popocatépetl,\
    así como el comportamiento de los proyectiles al entrar en contacto con el aire, la temperatura del ambiente y su interacción con la altitud relativa a la que se encuentran.\
        Así mismo se aplicaron relaciones matemáticas sobre la velocidad expresada de un objeto mediante vectores de posición respecto al tiempo y ángulo en la que los proyectiles son arrojados.\
            Se investigó sobre la relación que tiene el coeficiente de arrastre de un objeto con su masa y su área expuesta al aire, así como el cálculo del coeficiente de fricción del aire mismo de acuerdo con su altitud sobre el nivel mar y la temperatura a la que se encuentra.")

st.markdown("<h2> Desarrollo </h2>", unsafe_allow_html=True)
st.markdown("Para la comparación de la trayectoria idónea observada en un proyectil que no cuenta con resistencia del aire, se puso en práctica la relación que tiene la velocidad inicial del proyectil con sus componentes vectoriales 'x' y 'y',\
    de acuerdo con el ángulo en el que este es arrojado. Para la altura inicial del proyectil se ocupó la prominencia del volcán de acuerdo con la Ciudad de México, siendo ésta de aproximadamente 3800 m.\
        Así mismo, se ocuparon distintos ángulos para su comparación, sumados a los datos arrojados por la investigación preliminar, siendo los principales de 43.5°, 41.5°, 48.5° y 45°.") 
st.markdown("Por otro lado, para la trayectoria del proyectil que presenta una resistencia del aire, se aplicó la Segunda Ley de Newton para el cálculo de las fuerzas totales relativas\
    (sin tomar en consideración otras fuerzas significativas, tales como presión atmosférica, presión hidrostática inicial del volcán o nivel de humedad del entorno) que se ejercen sobre el proyectil antes descrito.\
        Para la sumatoria de fuerzas se tomó en consideración el diámetro descrito de los proyectiles descritos en la investigación previa, siendo de 0.2 a 0.6 m, la densidad máxima que presentaban (2600 kg/m\u00b3),\
            el cálculo de su volumen ideal gracias a su densidad, así como el área en contacto con el roce del aire. Mediante una serie de despejes a la sumatoria de fuerzas,\
                se logró obtener la aceleración inicial que describe el objeto al ser arrojado del cráter del volcán en el instante de tiempo 0, su velocidad inicial en sus componentes vectoriales 'x' y 'y' así como su velocidad total en el mismo instante de tiempo.\
                    Para el cálculo de los siguientes instantes, se tomó como ayuda el uso del método de Euler para el cálculo de la diferencia de aceleración, velocidad y posición relativa mediante el cambio definido del tiempo, tratando este intervalo de 0.05 segundos. ")


###Cálculo de la trayectoria idónea de proyectil###
st.markdown("<h2>Trayectoria sin resistencia al aire</h2>", unsafe_allow_html=True)

v_inicial = st.number_input('Velocidad inicial (m/s): ', min_value=150.00, max_value=250.00, value=250.00, step=0.1)
h_inicial = st.number_input('Altura inicial (m): ', min_value=0, max_value=3800, value=3800, step=1)
teta_angulo = st.number_input('Ángulo inicial (°): ', min_value=40.0, max_value=90.0, value=48.5, step=0.1)

###Cálculos Necesarios para operaciones futuras###
g = 9.8
y_final = 0
t_instante = np.linspace(0, 100, num=2000)
teta_radianes = np.radians(teta_angulo)
v_0x = v_inicial * np.cos(teta_radianes)
v_0y = v_inicial * np.sin(teta_radianes)
t_total = (-(v_0y)-np.sqrt(v_0y ** 2 - 4 * (-g/2) * h_inicial))/(2 * (-g/2))


###Datos finales###
v_y_sin = v_0y - g * t_total
v_final_sin = np.sqrt(v_0x ** 2 + v_y_sin ** 2)
distancia_final = v_0x * t_total


def proyectil_sin_arrastre(v_inicial, teta_angulo, h_inicial, t_instante, g = 9.8):
    teta_radianes = np.radians(teta_angulo)


    v_0x = v_inicial * np.cos(teta_radianes)
    v_0y = v_inicial * np.sin(teta_radianes)
    
    r_x = v_0x * t_instante
    r_y = (-(g/2) * t_instante ** 2) + (v_0y * t_instante) + h_inicial

    return r_x, r_y

r_x, r_y = proyectil_sin_arrastre(v_inicial, teta_angulo, h_inicial, t_instante)



###Tabla que muestra cálculo de variables###
st.markdown("<h3 style='text-align: center;'>Tabla de valores iniciales</h3>", unsafe_allow_html=True)
x,y = st.beta_columns(2)
with x:
    st.markdown('Ángulo en radianes: ')
    st.markdown('Velocidad inicial en x: ')
    st.markdown('Velocidad inicial en y: ')
    st.markdown('Gravedad: ')

with y:
    st.write(teta_radianes)
    st.write(v_0x)
    st.write(v_0y)
    st.markdown(g)

x_mayor = np.amax(r_x)
y_mayor = (np.amax(r_y) + 500)

fig = plt.figure(figsize=(15,4))
plt.plot(r_x,r_y)
plt.grid()
plt.axis('scaled')
plt.title("Trayectoria del proyectil sin resistencia del aire")
plt.xlim([0,x_mayor])
plt.ylim([0,y_mayor])
_ = plt.xticks(np.arange(0,x_mayor + 1,1000))
_ = plt.yticks(np.arange(0,y_mayor + 1,1000))

st.pyplot(fig)


###Trayectoria con resistencia al aire###

st.markdown("<h2>Trayectoria con resistencia al aire</h2>", unsafe_allow_html=True)

altitud = st.number_input('Altitud del volcán (msnm): ', min_value=0, max_value=8850, value=5426, step=1)
temp = st.number_input('Temperatura ambiente registrada (°C): ', min_value=-273.0, max_value=58.0, value=20.0, step=0.1)
diametro = st.number_input('Diámetro del proyectil (m): ',min_value=0.2, max_value=0.6, value=0.6, step=0.01)
dens = st.slider('Densidad del proyectil (kg/cm\u00b3): ',min_value=2100, max_value=2600, value=2600, step=1)

r = diametro/2
area = np.pi * r ** 2
masa = ((4/3) * np.pi * r ** 3) * dens
aire = (348.42 * (1 - altitud * (1.05 * 10 ** -4))) / (temp + 273)
dt = 0.05
coef = (2 * masa * g) / (aire * area * v_inicial ** 2)

D = (aire * coef * area) / 2

st.markdown("<h3 style='text-align: center;'>Tabla de valores iniciales</h3>", unsafe_allow_html=True)
x1, y1 = st.beta_columns(2)
with x1:
    st.markdown('Radio: ')
    st.markdown('Área frontal (considerando una esfera): ')
    st.markdown('Masa del proyectil (kg): ')
    st.markdown('Densidad del aire (kg/m\u00b3): ')
    st.markdown('Coeficiente de fricción del proyectil: ')
    st.markdown('Coeficiente de arrastre: ')

with y1:
    st.write(r)
    st.write(area)
    st.write(masa)
    st.write(aire)
    st.write(coef)
    st.write(D)

###Número de iteraciones###
N = 20000


def proyectile_with_drag(v_inicial, teta_angulo, h_inicial, masa, D, dt, N, g=9.8):
    
    teta_radianes = np.radians(teta_angulo)
    
    v_0x = v_inicial * np.cos(teta_radianes)
    v_0y = v_inicial * np.sin(teta_radianes)
    
    this_t = 0
    t_list = [this_t]

    v = v_inicial
    v_x = v_0x
    v_y = v_0y

    v_list = [v]
    v_x_list = [v_0x]
    v_y_list = [v_0y]

    x = 0
    y = 3800

    x_list = [x]
    y_list = [y]

    a_x = -(D / masa) * v * v_x
    a_y = -(g) - ((D / masa) * v * v_y)

    a_x_list = [a_x]
    a_y_list = [a_y]
    
    for i in range(N):
        
        v_x_next = v_x + a_x * dt
        v_y_next = v_y + a_y * dt
        
        v_next = np.sqrt(v_x_next ** 2 + v_y_next ** 2)

        v_list.append(v_next)
        v_x_list.append(v_x_next)
        v_y_list.append(v_y_next)

        x_next = x + (v_x * dt) + (0.5 * a_x * dt ** 2)
        y_next = y + (v_y * dt) + (0.5 * a_y * dt ** 2)

        x_list.append(x_next)
        y_list.append(y_next)

        a_x_next = -(D / masa) * v * v_x_next
        a_y_next = -(g) - ((D / masa) * v * v_y_next)

        a_x_list.append(a_x_next)
        a_y_list.append(a_y_next)
        

        v_x = v_x_next
        v_y = v_y_next
        v = v_next

        x = x_next
        y = y_next

        a_x = a_x_next
        a_y = a_y_next

        this_t += dt
        t_list.append(this_t)
        if y_next < 0:
            break
        
    return x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list


[x_list, y_list, v_list, v_x_list, 
v_y_list, a_x_list, a_y_list, t_list] = proyectile_with_drag(v_inicial, teta_angulo, h_inicial, masa, D, dt, N)

###Establecer distancia, altura, tiempo, y velocidad máxima con resistencia al aire###
y_drag_max = np.amax(y_list)
x_drag_max = np.amax(x_list)
t_drag_max = np.amax(t_list)
vx_final = np.amin(v_x_list)
vy_final = np.amin(v_y_list)

v_drag_final = np.sqrt(vx_final ** 2 + vy_final ** 2)


###Graficar ambas trayectorias###
fig1 = plt.figure(figsize=(15,4))
plt.plot(r_x,r_y, label="Sin resistencia de Aire")
plt.plot(x_list,y_list, label="Con Resistencia de Aire")
plt.grid()
plt.axis('scaled')
plt.title("Trayectoria con y sin resistencia de aire")
plt.xlim([0,x_mayor])
plt.ylim([0,y_mayor])
_ = plt.xticks(np.arange(0,x_mayor + 1,1000))
_ = plt.yticks(np.arange(0,y_mayor + 1,1000))
_ = plt.legend()

st.pyplot(fig1)

###Tabla de resultados a comparar###
st.markdown("<h2 style='text-align: center;'>Tabla de resultados de trayectorias</h2>", unsafe_allow_html=True)

x2, y2 = st.beta_columns(2)
with x2:
    st.markdown('<center>Trayectoria sin resistencia</center>', unsafe_allow_html=True)
with y2:
    st.markdown('<center>Trayectoria con resistencia</center>', unsafe_allow_html=True)

a,b,c,d = st.beta_columns(4)
with a:
    st.markdown('Distancia máxima (m)')
    st.markdown('Altura máxima (m)')
    st.markdown('Tiempo de vuelo (s)')
    st.markdown('Velocidad final (m/s)')
with b:
    st.write(distancia_final)
    st.write(y_mayor)
    st.write(t_total)
    st.write(v_final_sin)
with c:
    st.markdown('Distancia máxima (m)')
    st.markdown('Altura máxima (m)')
    st.markdown('Tiempo de vuelo (s)')
    st.markdown('Velocidad final (m/s)')
with d:
    st.write(x_drag_max)
    st.write(y_drag_max)
    st.write(t_drag_max)
    st.write(v_drag_final)

st.markdown("<h2> Conclusiones </h2>", unsafe_allow_html=True)
st.markdown("En la gráfica presentada anteriormente, se pueden observar ambas trayectorias, tanto el proyectil sin resistencia al aire, así como el que presentaba resistencia.\
    Para el primero, su alcance máximo se estima entre aproximadamente 8700 y 9100 m con una velocidad final de 1330 a 1332 km/hr.\
        Se debe aclarar que esta trayectoria es hipotética, ya que dentro del planeta Tierra es físicamente imposible que un proyectil trace una parábola tan perfectamente formada sin verse afectado por demás fuerzas externas.\
            Para la segunda trayectoria se estima que su alcance máximo, en condiciones promedio de temperatura y sin vientos fuertes ni lluvia, se encuentre aproximadamente entre 4850 y 5100 m, con una velocidad final de hasta 810 km/hr.\
                Gracias a estos resultados se puede apreciar que el alcance del proyectil con resistencia del aire se ha visto reducido a un poco más que la mitad de su trayectoria hipotética.\
                    Así mismo, la velocidad se redujo a una cifra menor, pero mantiene su relevancia en cuanto a ser considerado como un riesgo.")

st.markdown("<h2> Referencias </h2>", unsafe_allow_html=True)
st.markdown("* Martín Del Pozzo, A. L. et al. (2017) <i>Estudios geológicos y actualización del mapa de peligros del volcán Popocatépetl.</i> UNAM. UNAM: México. [Sitio web] Recuperado de: http://www.geofisica.unam.mx/assets/monografias22.pdf", unsafe_allow_html=True)
st.markdown("* UNAM (2015). <i>Erupciones Volcánicas.</i> UNAM. [Sitio web] Recuperado de: https://www.unam.mx/medidas-de-emergencia/erupcion-volcanica", unsafe_allow_html=True)
st.markdown("* <i>Clima Parque Nacional Izta-Popo.</i> (2020) Meteoblue. [Sitio web] Recuperado de: https://www.meteoblue.com/es/tiempo/historyclimate/climatemodelled/parque-nacional-izta-popo_m%C3%A9xico_3817620", unsafe_allow_html=True)
st.markdown("* <i>Densidad del aire.</i> (2014) Full Mecánica. [Sitio web] Recuperado de: http://fullmecanica.com/definiciones/d/285-densidad-del-aire", unsafe_allow_html=True)

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("<span style='font-size: 11px;'><center>Un trabajo de Joshua R. Amaya Camilo</center></span>", unsafe_allow_html=True)