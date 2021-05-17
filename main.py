from tkinter import *
from tkcalendar import *
from datetime import datetime
import requests
import webbrowser
import config

# CONSTANTS
URL = config.URL
TOKEN = config.TOKEN
USERNAME = config.USERNAME
ID = config.ID
BGCOLOR = "#bfcba8"
now = datetime.today()
TODAY = now.date().strftime("%Y%m%d")
header = {
    "X-USER-TOKEN": TOKEN
}

# Setting an Account in Pixela
pixela_endpoint = "https://pixe.la/v1/users"
pixela_para = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Setting Purpose of this project
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_para = {
#     "id": ID,
#     "name": "Coding graph",
#     "unit": "hour",
#     "type": "float",
#     "color": "shibafu"
# }


# initializing Window
root = Tk()
root.title("Calender")
root.iconphoto(True, PhotoImage(file="python_103279.png"))
root.resizable(width=False, height=False)
root.config(padx=40, pady=40, bg=BGCOLOR)

# Calendar
calender = Calendar(selectmode="day", date_pattern="ymmdd")
calender.grid(row=0, column=0, columnspan=2)


def add_pixel():
    date = calender.get_date()
    quantity = f"{entry_hour.get()}.{int(entry_minute.get()):02}"
    pixel_para = {
        "date": date,
        "quantity": quantity
    }
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
    response = requests.post(url=pixel_endpoint, json=pixel_para, headers=header)
    print(response.text)


def delete_pixel():
    date = calender.get_date()
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"
    response = requests.delete(url=delete_endpoint, headers=header)
    print(response.text)


def update_pixel():
    quantity = f"{entry_hour.get()}.{int(entry_minute.get()):02}"
    update_para = {
        "quantity": quantity
    }
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{calender.get_date()}"
    response = requests.put(url=update_endpoint, json=update_para, headers=header)
    print(response.text)


def journey_pixel():
    webbrowser.open(URL)


# Labels
label_hour = Label(text="Time(in Hours):", bg=BGCOLOR)
label_hour.grid(row=3, column=0, sticky="w")

label_minute = Label(text="Time(in Minutes):", bg=BGCOLOR)
label_minute.grid(row=4, column=0, sticky="w")

# Entries

entry_hour = Entry()
entry_hour.grid(row=3, column=1, pady=10)

entry_minute = Entry()
entry_minute.grid(row=4, column=1, pady=10)

# Buttons

add_button = Button(text="Add", command=add_pixel)
add_button.grid(row=5, column=0, pady=10, sticky='ew')

delete_button = Button(text="Delete", command=delete_pixel)
delete_button.grid(row=5, column=1, pady=10, padx=14, sticky='ew')

update_button = Button(text="Update", command=update_pixel)
update_button.grid(row=6, column=0, sticky='ew')

journey_button = Button(text="Journey", command=journey_pixel)
journey_button.grid(row=6, column=1, padx=14, sticky='ew')

root.mainloop()
