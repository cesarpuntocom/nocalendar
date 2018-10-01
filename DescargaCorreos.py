from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors
import base64
import CPUEvents


def sin_etiquetas(corr):
    beerre = ""
    cad = ""
    cad2 = ""
    tag = False
    for i in corr:
        c = i
        if ord(i) > 31 or ord(i) == 13 or ord(i) == 10:
            if c == '<':
                tag = True
            if tag:
                if c == '>':
                    tag = False
            else:
                aux = cad + c
                cad = aux
        cad2 = cad.replace("\r\n\r\n", "\r\n")
        cad = cad2
    return cad


def recibir_ids_correos(cpu_ev):
    SCOPES = 'https://mail.google.com/'
    store = file.Storage('credentials.json')
    #fich_mensajes = open("correos.dat", "r+")
    creds = store.get()
    #mensajes = fich_mensajes.read()
    #mensajes_f = mensajes.split()
    #fich_mensajes.close()
    #mensajes_new = []
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))


    # Mails:
    try:
        response = service.users().messages().list(userId='me', q='is:unread label:' + cpu_ev.carpeta_origen).execute()
        #print("Carpeta origen -> " + cpu_ev.carpeta_origen)
        #print("Mensajes en carpeta origen -> " + str(response.values()))
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId='me', q='is:unread label:' + cpu_ev.carpeta_origen, pageToken=page_token).execute()
            messages.extend(response['messages'])
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
    return messages


    #for item in messages:
        #if item['id'] not in mensajes_f:
            #mensajes_new.append(item)
            #fich_mensajes.write(item['id'] + "\n")
    #print("Mensajes new: " + str(len(mensajes_new)))


    # Tenemos los correos en messages, pero no se puede acceder a su contenido salvo al ID, para descargarlos uno a uno.
    # Además, tenemos almacenados los correos que ya hemos procesado en un fichero,
    # por lo que en la lista mensajes_new solo están aquellos por procesar

    #print(len(messages))
    #mess=[]
    #mess.append(messages[0])
    #mess.append(messages[1])

def recibir_correos(message):
    SCOPES = 'https://mail.google.com/'
    store = file.Storage('credentials.json')
    # fich_mensajes = open("correos.dat", "r+")
    creds = store.get()
    # mensajes = fich_mensajes.read()
    # mensajes_f = mensajes.split()
    # fich_mensajes.close()
    # mensajes_new = []
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    if not message:
        print('No messages found.')
    else:
        mail = service.users().messages().get(userId='me', id=message['id']).execute()
        # Asunto del correo:  mail['payload']['headers'][32]['value']
        asunto = mail['payload']['headers'][32]['value']
        remitente = mail['payload']['headers'][38]['value']
        msg_str = base64.urlsafe_b64decode(mail['payload']['parts'][1]['parts'][0]['body']['data']).decode('UTF-8')
        descripcion = sin_etiquetas(msg_str)
        fecha_recibido = mail['payload']['headers'][29]['value']
        #fecha_float = datetime.datetime.strptime(fecha_recibido, "%a, %b %d %Y %H:%M:s %z").strftime("%f")
        correo = dict(description=descripcion, summary=asunto, fecha_recibido=fecha_recibido, remitente=remitente,
                      start=dict(datetime=""), end=dict(datetime=""), location="", id="")
        # Instanciamos cada correo recibido como un objeto de tipo CPUEvents, al que pasamos un diccionario
        #corr = CPUEvents.CPUEvents(correo)


            # Eliminamos la etiqueta de No leído del correo y lo movemos a la carpeta de destino de los ya procesados
            #body = dict(addLabelIds=cpu_ev.etiqueta_carpeta_destino,
            #           removeLabelIds=["UNREAD", cpu_ev.etiqueta_carpeta_origen])

            #service.users().messages().modify(userId='me', id=message['id'], body=body).execute()
            #if mails.index(mail) == 0:
                #print(msg_str)
                #cadena = sin_etiquetas(msg_str)
                #print(cadena) HASTA AQUÍ, CORRECTO
                #print(cadena)
                #sistema = "Sist: " + Clases.CPUEvent.textoEvento(cadena, "Sistema: ", chr(13))
                #print(sistema)
                #modulo = "Mod: " + Clases.CPUEvent.textoEvento(cadena, "Modulo: ", chr(13))

                #break
    return correo