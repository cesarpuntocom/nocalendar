from Correo import Correo
import datetime

class CPUEvents:
    carpeta_origen = ""
    carpeta_destino_leidos = ""
    etiqueta_carpeta_origen = ""
    etiqueta_carpeta_destino = ""
    remitente = ""
    calendario = ""
    descrip = ""
    titulo = ""
    fecha_inicio = ""
    fecha_fin = ""
    fecha_recibido = ""
    ev_id = ""

    def __init__(self):
        self._carpeta_mail = ""
        carpeta_destino_leidos = ""
        etiqueta_carpeta_origen = ""
        etiqueta_carpeta_destino = ""
        remitente = ""
        calendario = ""
        print("Se invoca constructor sin parámetros")

    def __init__(self, dic):
        self._carpeta_mail = ""
        carpeta_destino_leidos = ""
        etiqueta_carpeta_origen = ""
        etiqueta_carpeta_destino = ""
        remitente = ""
        calendario = ""
        self._descrip = ""
        self._titulo = ""
        self._fecha_inicio = ""
        self._fecha_fin = ""
        self._fecha_recibido = ""
        self._ev_id = ""
        print("Se invoca constructor con parámetros")

    def texto_evento(mail, tag, hasta):
        cadenaux = ""
        indiceTag = mail.find(tag) + len(tag)
        fin = mail.find(hasta, indiceTag)
        cadena = mail[indiceTag:fin]
        for i in mail:
            aux = cadenaux + i
            cadenaux = aux
        if indiceTag != -1 & fin != -1:
            cadena = mail[indiceTag:fin]
        return cadena

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def fecha_recibido(self):
        return self._fecha_recibido

    @property
    def carpeta_mail(self):
        return self._carpeta_mail

    def start_time_correo(self, correo):
        return self.texto_evento(correo, "", "")

    def end_time_correo(self, correo):
        return self.texto_evento(correo, "", "")


"""
    def __init__(self, event):
        if isinstance(event, dict):
            self._descrip = event['description']
            self._titulo = event['summary']
            self._fecha_inicio = event['start']['datetime']
            self._fecha_fin = event['end']['datetime']
            self._fecha_recibido = self.textoEvento(event['description'], "Fecha de recepcion: ", "\r\n")
            self._n_notif = event['location']
            self._ev_id = event['id']
            
        elif isinstance(event, Correo):
            self._descrip = self.textoEvento(event.descripcion)
            self._titulo = event['summary']
            self._fecha_inicio = event['start']['datetime']
            self._fecha_fin = event['end']['datetime']
            self._fecha_recibido = event.fecha_recibido
            self._n_notif = event['location']
            self._ev_id = event['id']
    
    
"""



# calendarId = "tuenti.com_u1g9maijb37jb9i4m55m4el0u8@group.calendar.google.com"