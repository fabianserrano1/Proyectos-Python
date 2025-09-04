# Importar librerias
import turtle
import time
import threading

# Configuración inicial de la ventana
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)  # Desactivamos las actualizaciones automáticas de la pantalla

# Función para solicitar los nombres de los jugadores
def solicitar_nombres():
    nombre_izquierda = ventana.textinput("Nombre del jugador izquierdo", "Ingrese el nombre del jugador izquierdo:")
    nombre_derecha = ventana.textinput("Nombre del jugador derecho", "Ingrese el nombre del jugador derecho:")
    return nombre_izquierda, nombre_derecha

# Solicitar nombres de los jugadores inicialmente
nombre_jugador_izquierda, nombre_jugador_derecha = solicitar_nombres()

# Marcador
marcador_izquierda = 0
marcador_derecha = 0

# Paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("white")
paleta_izquierda.shapesize(stretch_wid=6, stretch_len=1)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("white")
paleta_derecha.shapesize(stretch_wid=6, stretch_len=1)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")  # aqui podemos definir si queremos una bola redonda o cuadrada
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.2  # Velocidad en la dirección x esta es la velocidad inicial que podemos cambiar si queremos
pelota.dy = 0.2  # Velocidad en la dirección y

# Funciones para el movimiento de las paletas
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    if y < 250:
        y += 20  
        paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    if y > -240:
        y -= 20  
        paleta_izquierda.sety(y)

def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    if y < 250:
        y += 20
        paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    if y > -240:
        y -= 20
        paleta_derecha.sety(y)

# Configuración de las teclas del teclado
ventana.listen()
ventana.onkeypress(paleta_izquierda_abajo, "w")  # movimiento de la paleta izquierda hacia abajo
ventana.onkeypress(paleta_izquierda_arriba, "s")  # movimiento de la paleta izquierda hacia arriba
ventana.onkeypress(paleta_derecha_arriba, "Up")  # movimiento de la paleta derecha hacia arriba
ventana.onkeypress(paleta_derecha_abajo, "Down")   # movimiento de la paleta derecha hacia abajo

# Texto del marcador
texto_marcador = turtle.Turtle()
texto_marcador.speed(0)
texto_marcador.color("white")
texto_marcador.penup()
texto_marcador.hideturtle()
texto_marcador.goto(0, 260)
texto_marcador.write("{}: 0  {}: 0".format(nombre_jugador_izquierda, nombre_jugador_derecha), align="center", font=("Courier", 24, "normal"))

# Función para actualizar el marcador
def actualizar_marcador():
    texto_marcador.clear()
    texto_marcador.write("{}: {}  {}: {}".format(nombre_jugador_izquierda, marcador_izquierda, nombre_jugador_derecha, marcador_derecha),
                         align="center", font=("Courier", 24, "normal"))

# Función para mostrar el mensaje del ganador
def mostrar_ganador(ganador, perdedor):
    texto_marcador.goto(0, 0)
    texto_marcador.write("¡{} ha ganado! {} ha perdido.".format(ganador, perdedor),
                         align="center", font=("Courier", 24, "normal"))

# Función para reiniciar las posiciones de las paletas y la pelota
def reiniciar_posiciones():
    paleta_izquierda.goto(-350, 0)
    paleta_derecha.goto(350, 0)
    pelota.goto(0, 0)
    pelota.dx = 0.2
    pelota.dy = 0.2

# Función para reiniciar el juego
def reiniciar_juego():
    global marcador_izquierda, marcador_derecha, nombre_jugador_izquierda, nombre_jugador_derecha

    while True:
        respuesta = ventana.textinput("Juego terminado", "¿Quieres jugar de nuevo? (si/no)").strip().lower()
        if respuesta == "si":
            cambiar_nombres = ventana.textinput("Juego nuevo", "¿Cambiar nombres de los jugadores? (si/no)").strip().lower()
            if cambiar_nombres == "si":
                nombre_jugador_izquierda, nombre_jugador_derecha = solicitar_nombres()
            marcador_izquierda = 0
            marcador_derecha = 0
            actualizar_marcador()
            reiniciar_posiciones()
            return True
        elif respuesta == "no":
            ventana.bye()
            return False
        else:
            ventana.textinput("Entrada inválida", "Por favor ingresa 'si' o 'no'.")

# Aumentar la velocidad de la pelota progresivamente cada minuto
def aumentar_velocidad_progresivamente():
    while True:
        time.sleep(60)
        if pelota.dx > 0:
            pelota.dx += 0.1
        else:
            pelota.dx -= 0.1
        if pelota.dy > 0:
            pelota.dy += 0.1
        else:
            pelota.dy -= 0.1

# Iniciar el hilo para aumentar la velocidad progresivamente
velocidad_thread = threading.Thread(target=aumentar_velocidad_progresivamente)
velocidad_thread.daemon = True
velocidad_thread.start()

# Bucle principal del juego
jugando = True
while jugando:
    ventana.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Colisiones con los bordes superiores e inferiores
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
    
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Colisiones con las paletas
    if (pelota.dx > 0) and (340 < pelota.xcor() < 350) and (paleta_derecha.ycor() + 50 > pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.setx(340)
        pelota.dx *= -1
    elif (pelota.dx < 0) and (-350 < pelota.xcor() < -340) and (paleta_izquierda.ycor() + 50 > pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1

    # Punto para la paleta derecha
    if pelota.xcor() > 390:
        marcador_izquierda += 1
        pelota.goto(0, 0)
        pelota.dx *= -1
        actualizar_marcador()
        if marcador_izquierda == 5 or marcador_derecha == 5:
            if marcador_izquierda == 5:
                mostrar_ganador(nombre_jugador_izquierda, nombre_jugador_derecha)
            else:
                mostrar_ganador(nombre_jugador_derecha, nombre_jugador_izquierda)
            ventana.update()  # hay que asegurarse de que se actualice la pantalla antes de solicitar la entrada
            jugando = reiniciar_juego()

    # Punto para la paleta izquierda
    if pelota.xcor() < -390:
        marcador_derecha += 1
        pelota.goto(0, 0)
        pelota.dx *= -1
        actualizar_marcador()
        if marcador_izquierda == 5 or marcador_derecha == 5:
            if marcador_izquierda == 5:
                mostrar_ganador(nombre_jugador_izquierda, nombre_jugador_derecha)
            else:
                mostrar_ganador(nombre_jugador_derecha, nombre_jugador_izquierda)
            ventana.update()  # Asegúrate de que se actualice la pantalla antes de solicitar la entrada
            jugando = reiniciar_juego()

# Llamar al método mainloop() para iniciar el bucle principal de la ventana de Turtle
turtle.mainloop()
