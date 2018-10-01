"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
# from __future__ import print_function
from datetime import datetime

import DescargaCorreos, CalendarInteract
import ArgentinaGDC, ArgentinaGDI

gdc = ArgentinaGDC.ArgentinaGDC({})
#gdi = ArgentinaGDI.ArgentinaGDI()

mailsGDC = DescargaCorreos.recibir_ids_correos(gdc)
#mailsGDI = DescargaCorreos.recibir_correos(gdi)

# mailsGDC ahora es una lista con objetos de tipo Correo que representan los correos recibidos de GDC
# mailsGDI ahora es una lista con objetos de tipo Correo que representan los correos recibidos de GDI


# Para GDC:
eventos_gdc = []
for m in mailsGDC:
    corr = DescargaCorreos.recibir_correos(m)
    ev = ArgentinaGDC.ArgentinaGDC(corr)
    eventos_gdc.append(ev)

for ev in eventos_gdc:
    print("Título: " + ev.titulo)


# Descargar ahora los eventos de los últimos 10 días del calendario correspondiente
# (un calendario por cada tipo)

eventsGDC = CalendarInteract.recibirEvents(gdc)
print("CPU Events de Calendar: " + str(eventsGDC.pop().titulo))
print("CPU Events de los correos: " + str(mailsGDC.pop().titulo))
#    eventsGDI = CalendarInteract.recibirEvents(gdi.calendario)

# Ya tenemos los eventos de GDC de los últimos 10 días almacenados en eventsGDC
for m in eventsGDC:
    print(str(m.titulo))
    print("Fecha de creación: " + m.fecha_recibido)
    print("Fecha de inicio: " + m.fecha_inicio)
    print("Fecha de fin: " + m.fecha_fin)

# Convertir tanto estos eventos descargados como los correos recibidos en CPUEvents

