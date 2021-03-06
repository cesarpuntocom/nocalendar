from CPUEvents import CPUEvents
import datetime

class ArgentinaGDC(CPUEvents):
    carpeta_origen = "gdc_notificaciones"
    carpeta_destino_leidos = "INBOX/provisional-GDC"
    etiqueta_carpeta_origen = "Label_2"
    etiqueta_carpeta_destino = "Label_59"
    remitente = "GDC-Notificaciones@tgtarg.com"
    calendario = "tuenti.com_u1g9maijb37jb9i4m55m4el0u8@group.calendar.google.com"

    def __init__(self, dicc):
        if dicc != {}:
            print(str(dicc))
            self.descrip = dicc['description']
            self.titulo = dicc['summary']
            self._ev_id = dicc['id']
            if not 'fecha_recibido' in dicc:
                # Si en el diccionario NO aparece este campo, entonces el evento viene de Calendar
                aux = self.texto_evento(dicc['description'], "Fecha de recepcion: ", "\r\n")
                # Depuramos para eliminar los : del timezone en la cadena fecha, ya que dan problemas
                index = aux.rfind(':')
                if index > 18:
                    # A veces viene con formato YYYY-MM-DDTHH:MM:SS-XX:XX y hay que eliminar esos últimos dos puntos
                    aux = self.rreplace(aux, ':', '', 1)
                print(aux)
                if(aux.find('.000')) > 1:
                    self._fecha_recibido_dat = datetime.datetime.strptime(aux, "%Y-%m-%dT%H:%M:%S.%f%z")
                else:
                    self._fecha_recibido_dat = datetime.datetime.strptime(aux, "%Y-%m-%dT%H:%M:%S%z")
            else:
                # Si en el diccionario SÍ aparece el campo, el evento viene de un correo y tiene fecha de recepción
                # con el formato de GMail
                self._fecha_recibido_dat = datetime.datetime.strptime(dicc['fecha_recibido'], '%a, %d %b %Y %H:%M:%S %z')
            self._fecha_recibido = self._fecha_recibido_dat.isoformat()
            if dicc['start'] == dict(datetime=''):
                str_date_start = self.texto_evento(self.descrip, "Fecha y Hora de Inicio: ", "\r\n")
                #if str_date_start.find(' ') > 0:
                 #   str_date_start = str_date_start.replace(' ', 'T')
                self._fecha_inicio = datetime.datetime.strptime(str_date_start + "-0300", "%d/%m/%Y %H:%Mhs.%z")

            else:
                self._fecha_inicio = dicc['start']
            if dicc['end'] == dict(datetime=''):
                aux = self.texto_evento(self.descrip, "Fecha y Hora Estimada de Solucion: ", "\r\n")
                if aux == "":
                    # Algunos correos indican la hora de fin con "Solución" y otros con "Fin"
                    aux = self.texto_evento(self.descrip, "Fecha y Hora de Fin: ", "\r\n")
                self._fecha_fin = datetime.datetime.strptime(aux + "-0300", "%d/%m/%Y %H:%Mhs.%z")
            else:
                self._fecha_fin = dicc['end']
            self.notif_num = self.texto_evento(self.titulo, "Notificacion Nro ", " - ")

    @property
    def descripcion(self):
        return self._descrip

    @property
    def fecha_recibido(self):
        return self._fecha_recibido

    @property
    def fecha_recibido_dat(self):
        return self._fecha_recibido_dat

    @property
    def carpeta_mail(self):
        return self._carpeta_mail



