from __future__ import print_function
import datetime
import CPUEvents
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    #flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
nowDate = datetime.datetime.utcnow()
now = nowDate.isoformat() + 'Z'  # 'Z' indicates UTC time
timemin = datetime.datetime.toordinal(nowDate)
timemin -= 100
timemin_dat = datetime.datetime.fromordinal(timemin).isoformat() + 'Z'

def recibirEvents(cpu_ev):
    events_result = service.events().list(
        calendarId=cpu_ev.calendario,
        timeMin=timemin_dat,
        timeMax=None,
        singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events

def delete_events(cpu_ev):
    service.events().delete(calendarId=cpu_ev.calendario, eventId=cpu_ev._ev_id).execute()


def add_event(cpu_ev):
    if type(cpu_ev._fecha_inicio) is dict:
        start_date = cpu_ev._fecha_inicio['dateTime']
        end_date = cpu_ev._fecha_fin['dateTime']
    else:
        start_date = cpu_ev._fecha_inicio.isoformat()
    if type(cpu_ev._fecha_fin) is dict:
        end_date = cpu_ev._fecha_fin['dateTime']
    else:
        end_date = cpu_ev._fecha_fin.isoformat()

    event = {
        'summary': cpu_ev.titulo,
        'description': cpu_ev.descrip + '\r\nFecha de recepcion: '
                       + cpu_ev._fecha_recibido + '\r\nNOCALENDAR',
        'start': {'dateTime': start_date},
        'end': {'dateTime': end_date}
    }
    event = service.events().insert(calendarId=cpu_ev.calendario,
                                    body=event).execute()

#start_date = datetime.datetime(
#        2017, 09, 01, 00, 00, 00, 0).isoformat() + 'Z'
#    end_date = datetime.datetime(2017, 09, 30, 23, 59, 59, 0).isoformat() + 'Z'



#events = recibirEvents("tuenti.com_u1g9maijb37jb9i4m55m4el0u8@group.calendar.google.com")

#for event in events:
#   start = event['start'].get('dateTime', event['start'].get('date'))
#   print(start, event['summary'])

# Call the Calendar API

#print('Getting the upcoming 10 events')
#events_result = service.events().list(calendarId='primary', timeMin=now,
#                                          maxResults=10, singleEvents=True,
#                                          orderBy='startTime').execute()
#events = events_result.get('items', [])

#if not events:
#    print('No upcoming events found.')
#for event in events:
#    start = event['start'].get('dateTime', event['start'].get('date'))
#    print(start, event['summary'])


def dt_to_json(obj):
    if isinstance(obj, datetime.datetime):
        return {
            "__type__": "datetime",
            "year": obj.year,
            "month": obj.month,
            "day": obj.day,
            "hour": obj.hour,
            "minute": obj.minute,
            "second": obj.second,
            "microsecond": obj.microsecond,
            "tz": (obj.tzinfo.tzname(obj), obj.utcoffset().total_seconds())
        }


#if __name__ == '__main__':
#    main()
