import whatsintro_gui
import whatsintro_msg
import random

def tarea(tablero):
    #Aqui empieza tu tarea
    usuario = "@jilopez8"
    clave = "8681307185584869"
    s = "Usuario conectado: " + usuario
    emisor = whatsintro_gui.emisor(s)
    conectar = whatsintro_msg.conectar(usuario, clave)
    conectar
    a="@jilopez8 javier lopez achondo"
    b="9402871902010010000110110110110010100110100110111001110101100100000111101000101000001011100110010101110010011101010111110001110001011010100011100101101010011111010110000101111001011100110011011101000001011000010111001101001101010011110100000001110001"
    validar_encriptacion=whatsintro_msg.validar_encriptacion(a, b)
    validar_encriptacion
    a=2
    while a==2:
        if conectar==True and validar_encriptacion==True:
            emisor
            click = whatsintro_gui.esperar.click()
            VF=0
            while Verd==0:
                if click=='enviar':
                    mensaje_encriptado="9402871902010010000110110110110010100110100110111001110101100100000111101000101000001011100110010101110010011101010111110001110001011010100011100101101010011111010110000101111001011100110011011101000001011000010111001101001101010011110100000001110001"
                    whatsintro_msg.enviar_mensaje(mensaje_encriptado)
                    print(whatsintro_msg.enviar_mensaje(mensaje_encriptado))
                    print(whatsintro_msg.mensaje_recibido(1)
            if conectar==False:
                s = "Usuario o clave incorrectos."
                emisor = whatsintro_gui.emisor(s)
                emisor
            Verd=1
        
        
    
    
app = whatsintro_gui.Application("tarea")
app.title('WhatsIntro')
app.loadProgram(tarea)
app.start()
