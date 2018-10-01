from __future__ import print_function
import datetime

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import CPUEvents

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'


"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
nowDate = datetime.datetime.utcnow()
now = nowDate.isoformat() + 'Z'  # 'Z' indicates UTC time
timemin = datetime.datetime(nowDate.date().year, nowDate.date().month,
                                nowDate.date().day - 10, nowDate.time().hour,
                                nowDate.time().minute, nowDate.time().second,
                                nowDate.time().microsecond).isoformat() + 'Z'

def recibirEvents(cpu_ev):
    eventsResult = service.events().list(
        calendarId=cpu_ev.calendario,
        timeMin=timemin,
        timeMax=None,
        singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    cpu_events = []
    for ev in events:
        cpu_events.append(CPUEvents.CPUEvents(ev))
    return cpu_events
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





#if __name__ == '__main__':
#    main()
