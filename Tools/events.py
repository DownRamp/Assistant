from __future__ import print_function

import datetime
import os.path
from tkinter import *
import tkinter.messagebox
from pysondb import db
from google import *
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


# Add events
def add_event(win):
    frame = Frame(win)
    # show possible day tasks
    label = Label(frame, text="Enter event", font=('Aerial 12'))
    label.pack()
    label1 = Label(frame, text="name", font=('Aerial 12'))
    label1.pack()
    ent1 = Entry(frame)
    ent1.pack()
    label2 = Label(frame, text="Description", font=('Aerial 12'))
    label2.pack()
    ent2 = Entry(frame)
    ent2.pack()
    label3 = Label(frame, text="Date", font=('Aerial 12'))
    label3.pack()
    ent3 = Entry(frame)
    ent3.pack()
    enter = Button(frame, text='Enter', width=25, command=lambda: save_task(ent1.get(), ent2.get(), ent3.get()))
    enter.pack()
    frame.pack()


# update events
def update_event(win):
    frame = Frame(win)
    frame.grid()
    # show possible tasks with ids
    # enter id, updated task, updated quad
    Label(frame, text="Enter id, name, description, and date", font=('Aerial 12')).grid(row=1)
    ent1 = Entry(frame)
    ent1.grid(row=2)
    ent2 = Entry(frame)
    ent2.grid(row=3)
    ent3 = Entry(frame)
    ent3.grid(row=4)
    ent4 = Entry(frame)
    ent4.grid(row=5)
    Button(frame, text='Enter', width=25, command=lambda: update_task(ent1.get(), ent2.get(), ent3.get(), ent4.get())).grid(row=6)

    # add suggestions here
    Label(frame, text="List of events", font=('Aerial 12')).grid(row=7)
    # fetch to-do list
    events = db.getDb("Events/events.json")
    event_list = events.getAll()
    for i, item in enumerate(event_list):
        w = Text(frame, width=15, height=2)
        w.grid(row=(i + 8))
        value = f'{item["name"]} {item["date"]}'
        w.insert(END, value)


def update_task(id, name, description, date):
    update = {"name": name, "description": description, "date": date}
    todo = db.getDb("Events/events.json")
    todo.updateById(pk=id, new_data=update)
    # call google events
    tkinter.messagebox.showinfo("Update Event", "SUCCESS")


def save_task(name, date):
    todo = db.getDb("Events/events.json")
    todo.add({"name": name, "date": date})
    # call google events
    tkinter.messagebox.showinfo("Save Event",  "SUCCESS")


# check google events
def check_google():
    print()


# update google events
def update_google():
    print()


# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#
#     try:
#         service = build('calendar', 'v3', credentials=creds)
#
#         # Call the Calendar API
#         now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         print('Getting the upcoming 10 events')
#         events_result = service.events().list(calendarId='primary', timeMin=now,
#                                               maxResults=10, singleEvents=True,
#                                               orderBy='startTime').execute()
#         events = events_result.get('items', [])
#
#         if not events:
#             print('No upcoming events found.')
#             return
#
#         # Prints the start and name of the next 10 events
#         for event in events:
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(start, event['summary'])
#
#     except HttpError as error:
#         print('An error occurred: %s' % error)
#
#
# if __name__ == '__main__':
#     main()