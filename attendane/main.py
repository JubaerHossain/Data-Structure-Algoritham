import tkinter as tk
from tkinter import Tk, ttk
from tkinter import *
from zk import ZK, const
import requests


def api_response():
    request_link = "https://www.sookh.com/api/72sookh46/online-payment-types"
    response = requests.get(request_link)
    resp_json = response.json()
    return resp_json


class App():
    def __init__(self, master):
        self.master = master
        self.master.title("Sookh Attendance")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        # self.frame = ttk.Frame(self.master)
        # self.frame.pack()
        #
        # self.button = ttk.Button(self.frame, text="Click Me", command=api_response)
        # self.button.pack()


if __name__ == "__main__":
    app = Tk()
    app.title("Sookh Attendance")
    app.geometry("400x400")
    app.resizable(False, False)
    list_d = Listbox(app)
    response = api_response()
    conn = None
    zk = ZK('192.168.001.225', port=5500, timeout=5)
    try:
        print('Connecting to device ...')
        conn = zk.connect()
        print('Disabling device ...')
        conn.disable_device()
        print('Firmware Version: : {}'.format(conn.get_firmware_version()))
        # print '--- Get User ---'
        users = conn.get_users()
        for user in users:
            print(user)
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'

            # print'- UID #{}'.format(user.uid)
            # print '  Name       : {}'.format(user.name)
            # print '  Privilege  : {}'.format(privilege)
            # print '  Password   : {}'.format(user.password)
            # print '  Group ID   : {}'.format(user.group_id)
            # print '  User  ID   : {}'.format(user.user_id)

        print("Voice Test ...")
        conn.test_voice()
        print('Enabling device ...')
        conn.enable_device()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()
    # a = App(app)

    app.mainloop()
