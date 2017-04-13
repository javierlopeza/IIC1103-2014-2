import whatsintro_gui
import whatsintro_msg
from whatsintro_gui import*
from whatsintro_msg import*

def tarea(tablero):
    #Aqui empieza tu tarea
    clave = '705954849672'
    usuario = '@dicifuentes'

    #Conectar
    
    print(conectar("@dicifuentes",'705954849672'))

    emisor('@dicifuentes')

    esperar=esperar_click()

    if esperar=="enviar":
        





    


    
    	
	#Aqui termina tu tarea
    
app = whatsintro_gui.Application("tarea")
app.title('WhatsIntro')
app.loadProgram(tarea)
app.start()
