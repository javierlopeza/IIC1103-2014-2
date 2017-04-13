if click=='enviados':
    cantidad_enviados=int(whatsintro_msg.cantidad_enviados())
    print(cantidad_enviados)

    for k in range(o, cantidad_enviados):
        msg_enviado=(whatsintro_msg.mensaje_enviado(k))
        print(msg_enviado)

        texto_enviado = msg_enviado
        texto_enviado_lista=texto_enviado.split()
        
        remitente=texto_enviado_lista[0]
        destinatario=texto_enviado_lista[1]
        msg=texto_enviado_lista[2]

        print(remitente)
        print(destinatario)
        print(msg)

    VF=0
