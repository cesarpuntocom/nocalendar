class Correo():

    def __init__(self, asunto, descripcion, fecha_recibido, remitente):
        self._asunto = asunto
        self._descripcion = descripcion
        self._fecha_recibido = fecha_recibido
        self._remitente = remitente

    @property
    def asunto(self):
        return self._asunto

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def fecha_recibido(self):
        return self._fecha_recibido

    @property
    def remitente(self):
        return self._remitente

    def __str__(self):
        return self.asunto.__str__() + "\n" + "FROM: " + \
               self.remitente + " ON " + self.fecha_recibido + \
               "\n" + self.descripcion
