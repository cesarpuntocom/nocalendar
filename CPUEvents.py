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
    _fecha_recibido = ""
    ev_id = ""

    def __init__(self):
        self._carpeta_mail = ""
        carpeta_destino_leidos = ""
        etiqueta_carpeta_origen = ""
        etiqueta_carpeta_destino = ""
        remitente = ""
        calendario = ""

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

    def texto_evento(self, mail, tag, *args):
        index_tag = mail.find(tag)
        if index_tag >= 0:
            index_tag_b = index_tag + len(tag)
            if len(args) > 0:
                cadena = mail[index_tag_b:mail.find(args[0], index_tag_b)]
            else:
                cadena = mail[index_tag_b:]
            return cadena
        else:
            return ""

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def fecha_recibido_dat(self):
        return self._fecha_recibido_dat

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

    def rreplace(self, s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)


# calendarId = "tuenti.com_u1g9maijb37jb9i4m55m4el0u8@group.calendar.google.com"