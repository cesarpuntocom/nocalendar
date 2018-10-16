"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
# from __future__ import print_function
from datetime import datetime

import DescargaCorreos, CalendarInteract
import ArgentinaGDC, ArgentinaGDI

gdc = ArgentinaGDC.ArgentinaGDC({})
gdi = ArgentinaGDI.ArgentinaGDI({})

# Descargar los IDs de los correos GDC y GDI
mailsGDC = DescargaCorreos.recibir_ids_correos(gdc)
mailsGDI = DescargaCorreos.recibir_ids_correos(gdi)

# mailsGDC ahora es una lista con objetos de tipo Correo que representan los correos recibidos de GDC
# mailsGDI ahora es una lista con objetos de tipo Correo que representan los correos recibidos de GDI


# Descargar de Calendar los eventos de tipo GDC y GDI ya agendados (sólamente los últimos 10 días):
gdc_events_calendar = CalendarInteract.recibirEvents(gdc)
gdi_events_calendar = CalendarInteract.recibirEvents(gdi)

events_gdc = []
events_gdi = []
# Descargar los correos cuyos IDs hemos recibido y convertirlos en objetos GDC
for m in mailsGDC:
    corr = DescargaCorreos.recibir_correos(m, gdc.etiqueta_carpeta_origen)
    ev = ArgentinaGDC.ArgentinaGDC(corr)
    events_gdc.append(ev)

for m in mailsGDI:
    corr = DescargaCorreos.recibir_correos(m, gdi.etiqueta_carpeta_origen)
    ev = ArgentinaGDI.ArgentinaGDI(corr)
    events_gdi.append(ev)

# Combinamos los eventos de Calendar con los recibidos en los mails
for ev in gdc_events_calendar:
    new_event = ArgentinaGDC.ArgentinaGDC(ev)
    events_gdc.append(new_event)

for ev in gdi_events_calendar:
    new_event = ArgentinaGDI.ArgentinaGDI(ev)
    events_gdi.append(new_event)

# Ordenamos los eventos combinados por su parámetro fecha_recibido_dat (es un datetime)
events_gdc_sort = sorted(events_gdc, key=lambda x: x._fecha_recibido_dat, reverse=True)
events_gdi_sort = sorted(events_gdi, key=lambda x: x._fecha_recibido_dat, reverse=True)

# Tomamos el evento con la fecha de recepción más reciente de cada número de notificación
# Para ello, ya que están ordenados de más reciente a menos, tomamos el evento más reciente de cada
# número de notificación, y los demás que tengamos en el array los pondremos en otro array para eliminar
# de Calendar aquellos que procedan de allí, para evitar duplicados
# (los que vienen de Calendar tienen un eventId)
events_gdc_unic = []
events_gdc_delete = []

events_gdc_unic = []
events_gdc_delete = []
esta = False
for ev in events_gdc_sort:
    #print(ev.titulo)
    #print(str(ev._fecha_inicio))
    #print(str(ev._fecha_fin))
    for l in events_gdc_unic:
        if ev.notif_num == l.notif_num:
            esta = True
    if not esta:
        events_gdc_unic.append(ev)
    else:
        events_gdc_delete.append(ev)
    esta = False

events_gdi_unic = []
events_gdi_delete = []
esta = False
for ev in events_gdi_sort:
    #print(ev.titulo)
    #print(str(ev._fecha_inicio))
    #print(str(ev._fecha_fin))
    for l in events_gdi_unic:
        if ev.notif_num == l.notif_num:
            esta = True
    if not esta:
        events_gdi_unic.append(ev)
    else:
        events_gdi_delete.append(ev)
    esta = False


for ev in events_gdc_delete:
    if ev._ev_id != '':
        CalendarInteract.delete_events(ev)

for ev in events_gdc_unic:
    if ev.titulo != '':
        CalendarInteract.add_event(ev)

for ev in events_gdi_delete:
    if ev._ev_id != '':
        CalendarInteract.delete_events(ev)

for ev in events_gdi_unic:
    if ev.titulo != '':
        CalendarInteract.add_event(ev)
