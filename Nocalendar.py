"""
Shows basic usage of the Gmail API.

Lists the user's Gmail labels.
"""
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import Clases
from apiclient import errors

import base64

# Setup the Gmail API
SCOPES = 'https://mail.google.com/'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

mails = []

# Mails:
try:
    response = service.users().messages().list(userId='me',
                                               q='from:GDC-Notificaciones@tgtarg.com').execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me', q='from:GDC-Notificaciones@tgtarg.com',
                                                   pageToken=page_token).execute()
        messages.extend(response['messages'])
except errors.HttpError as error:
    print('An error occurred: %s' % error)

# Tenemos los correos en messages, pero no se puede acceder a su contenido salvo al ID, para descargarlos uno a uno.
if not messages:
    print('No messages found.')
else:
    print('Messages:')
    for message in messages:
        mail = service.users().messages().get(userId='me', id=message['id']).execute()

        # Asunto del correo:  mail['payload']['headers'][32]['value']
        #print(mail['payload']['headers'][32]['value'])

        mails.append(mail)
        msg_str = base64.urlsafe_b64decode(mail['payload']['parts'][1]['parts'][0]['body']['data']).decode('UTF-8')
        if mails.index(mail) == 0:
            #print(msg_str)
            cadenas = Clases.Correo.sinEtiquetas(msg_str)
            #for cad in cadenas:
                #print(cad)
            break

        # Tenemos la parte html del correo en msg_str, y un array con todos los correos referenciado por mails[].


