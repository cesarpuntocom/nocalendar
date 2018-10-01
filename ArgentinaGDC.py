from CPUEvents import CPUEvents
from Correo import Correo


class ArgentinaGDC(CPUEvents):
    carpeta_origen = "gdc_notificaciones"
    carpeta_destino_leidos = "INBOX/provisional-GDC"
    etiqueta_carpeta_origen = "Label_2"
    etiqueta_carpeta_destino = "Label_59"
    remitente = "GDC-Notificaciones@tgtarg.com"
    calendario = "tuenti.com_u1g9maijb37jb9i4m55m4el0u8@group.calendar.google.com"

    def __init__(self, dicc):
        self._descrip = dicc['description']
        self._titulo = dicc['summary']
        self._ev_id = dicc['id']
        if dicc['fecha_recibido'] == "":
            self._fecha_recibido = self.texto_evento(self.descripcion, "Fecha de recepcion", "\r\n")
        if dicc['location'] == "":
            self._n_notif = self.texto_evento(self._titulo, "Notificacion Nro ", " ")
        if dicc['start'] == dict(datetime=""):
            self._fecha_inicio = self.texto_evento(self.descripcion,"Fecha y Hora de Inicio: ", "\r\n")
        if dicc['end'] == dict(datetime=""):
            aux = self.texto_evento(self.descripcion, "Fecha y Hora de Fin: ", "\r\n")
            if aux == "":
                aux = self.texto_evento(self.descripcion, "Fecha y Hora Estimada de Solucion: ", "\r\n")
            self._fecha_fin = aux
        print("Se invoca constructor de subclase con parámetros")

    def __init__(self):
        self._titulo = ""
        print("Se invoca constructor de subclase sin parámetros")

    @property
    def correo(self):
        return self._correo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def fecha_recibido(self):
        return self._fecha_recibido

    @property
    def carpeta_mail(self):
        return self._carpeta_mail

#    @correo.setter
#    def set_correo(self, correo):
#        self.correo = correo
