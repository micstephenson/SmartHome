from tkinter import *
from backend import SmartPlug, SmartTv, SmartHome
from backend import SmartDevice


class SmartHomeSystem:
    def __init__(self, myHome):
        self.smartHome = myHome
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("250x100")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )
        self.i = 1

    def run(self):
        self.showDevices()
        self.createWidgets()
        self.addButton()
        self.win.mainloop()

    def createWidgets(self):
        btnTurnOnAll = Button(
            self.mainFrame,
            text="Turn on all",
            width=15,
            justify="left",
            highlightthickness=1,
            highlightbackground="black",
            command=self.turnOnAllAndUpdateLabels
        )
        btnTurnOnAll.grid(column=0, row=0)

        btnTurnOffAll = Button(
            self.mainFrame,
            text="Turn off all",
            width=18,
            justify="left",
            highlightthickness=1,
            highlightbackground="black",
            command=self.turnOffAllAndUpdateLabels
        )
        btnTurnOffAll.grid(column=3, row=0, columnspan=2)

    def addButton(self):
        num_devices = len(self.smartHome.getDevices())
        add_button_row = num_devices + 2

        btnAdd = Button(
            self.mainFrame,
            text="Add",
            width=10,
            justify="left",
            highlightthickness=1,
            highlightbackground="black",
            command=self.addNewDevice
        )
        btnAdd.grid(column=0, row=add_button_row)

    def showDevices(self):
        for device in self.smartHome.getDevices():
            dev_name = f"dev_{self.i}"
            globals()[dev_name] = StringVar()
            if isinstance(device, SmartTv):
                if device.getSwitchedOn():
                    globals()[dev_name].set(f"Tv: on, Channel: {device.getChannel()}")

                    lblTvDevice = Label(
                        self.mainFrame,
                        textvariable=globals()[dev_name],
                        width=30,
                        font=("Helvetica", 20),
                        anchor="w"
                    )
                    lblTvDevice.grid(column=0, row=self.i, columnspan=2)
                else:
                    globals()[dev_name].set(f"Tv: off, Channel: {device.getChannel()}")

                    lblTvDevice = Label(
                        self.mainFrame,
                        textvariable=globals()[dev_name],
                        width=30,
                        font=("Helvetica", 20),
                        anchor="w"
                    )
                    lblTvDevice.grid(column=0, row=self.i, columnspan=2)

            elif isinstance(device, SmartPlug):
                if device.getSwitchedOn():
                    globals()[dev_name].set(f"Plug: on, Consumption Rate: {device.getConsumptionRate()}")

                    lblPlugDevice = Label(
                        self.mainFrame,
                        textvariable=globals()[dev_name],
                        width=30,
                        font=("Helvetica", 20),
                        anchor="w"
                    )
                    lblPlugDevice.grid(column=0, row=self.i, columnspan=2)
                else:
                    globals()[dev_name].set(f"Plug: off, Consumption Rate: {device.getConsumptionRate()}")

                    lblPlugDevice = Label(
                        self.mainFrame,
                        textvariable=globals()[dev_name],
                        width=30,
                        font=("Helvetica", 20),
                        anchor="w"
                    )
                    lblPlugDevice.grid(column=0, row=self.i, columnspan=2)

            btnToggle = Button(
                self.mainFrame,
                text="Toggle",
                width=7,
                justify="left",
                highlightthickness=1,
                highlightbackground="black",
                command=lambda idx=self.i: self.toggleDevice(idx)
            )
            btnToggle.grid(column=3, row=self.i)

            btnEdit = Button(
                self.mainFrame,
                text="Edit",
                width=4,
                justify="left",
                highlightthickness=1,
                highlightbackground="black",
                command=lambda idx=self.i: self.editDevice(idx)
            )
            btnEdit.grid(column=4, row=self.i)

            btnDelete = Button(
                self.mainFrame,
                text="Delete",
                width=7,
                justify="right",
                highlightthickness=1,
                highlightbackground="black",
                command=lambda idx=self.i: self.deleteRow(idx)
            )
            btnDelete.grid(column=5, row=self.i)
            self.i += 1

    def addNewDevice(self):
        addDevWin = Toplevel(self.win)
        addDevWin.title("Add New Device")

        Label(addDevWin, text="Choose a device (Smart Plug or Smart TV):").grid(row=0, column=0)

        def create_smart_device(device_type):
            if device_type == "Smart Plug":
                consumption_rate_entry = Entry(addDevWin)
                consumption_rate_entry.grid(row=1, column=0)
                Label(addDevWin, text="Consumption Rate:").grid(row=1, column=0)

                def add_smart_plug():
                    consumption_rate = consumption_rate_entry.get()
                    if consumption_rate.isdigit():
                        consumption_rate = int(consumption_rate)
                        if 0 <= consumption_rate <= 150:
                            new_smart_plug = SmartPlug(consumption_rate)
                            self.smartHome.addDevice(new_smart_plug)

                            dev_name = f"dev_{self.i}"
                            globals()[dev_name] = StringVar()
                            globals()[dev_name].set(f"Plug: off, Consumption Rate: {new_smart_plug.getConsumptionRate()}")

                            lblPlugDevice = Label(
                                self.mainFrame,
                                textvariable=globals()[dev_name],
                                width=30,
                                font=("Helvetica", 20),
                                anchor="w"
                            )
                            lblPlugDevice.grid(column=0, row=self.i, columnspan=2)

                            btnToggle = Button(
                                self.mainFrame,
                                text="Toggle",
                                width=7,
                                justify="left",
                                highlightthickness=1,
                                highlightbackground="black",
                                command=lambda idx=self.i: self.toggleDevice(idx)
                            )
                            btnToggle.grid(column=3, row=self.i)

                            btnEdit = Button(
                                self.mainFrame,
                                text="Edit",
                                width=4,
                                justify="left",
                                highlightthickness=1,
                                highlightbackground="black",
                                command=lambda idx=self.i: self.editDevice(idx)
                            )
                            btnEdit.grid(column=4, row=self.i)

                            btnDelete = Button(
                                self.mainFrame,
                                text="Delete",
                                width=7,
                                justify="right",
                                highlightthickness=1,
                                highlightbackground="black",
                                command=lambda idx=self.i: self.deleteRow(idx)
                            )
                            btnDelete.grid(column=5, row=self.i)
                            self.addButton(self.i)
                            self.i += 1

                            addDevWin.destroy()

                Button(addDevWin, text="Add Smart Plug", command=add_smart_plug).grid(row=2, column=0)

            elif device_type == "Smart TV":
                new_smart_tv = SmartTv()
                self.smartHome.addDevice(new_smart_tv)

                dev_name = f"dev_{self.i}"
                globals()[dev_name] = StringVar()
                globals()[dev_name].set(f"TV: off, Channel: {new_smart_tv.getChannel()}")

                lblTvDevice = Label(
                    self.mainFrame,
                    textvariable=globals()[dev_name],
                    width=30,
                    font=("Helvetica", 20),
                    anchor="w"
                )
                lblTvDevice.grid(column=0, row=self.i, columnspan=2)

                btnToggle = Button(
                    self.mainFrame,
                    text="Toggle",
                    width=7,
                    justify="left",
                    highlightthickness=1,
                    highlightbackground="black",
                    command=lambda idx=self.i: self.toggleDevice(idx)
                )
                btnToggle.grid(column=3, row=self.i)

                btnEdit = Button(
                    self.mainFrame,
                    text="Edit",
                    width=4,
                    justify="left",
                    highlightthickness=1,
                    highlightbackground="black",
                    command=lambda idx=self.i: self.editDevice(idx)
                )
                btnEdit.grid(column=4, row=self.i)

                btnDelete = Button(
                    self.mainFrame,
                    text="Delete",
                    width=7,
                    justify="right",
                    highlightthickness=1,
                    highlightbackground="black",
                    command=lambda idx=self.i: self.deleteRow(idx)
                )
                btnDelete.grid(column=5, row=self.i)
                self.addButton(self.i)
                self.i += 1

                addDevWin.destroy()

        device_options = ["Smart Plug", "Smart TV"]

        for i, device_type in enumerate(device_options, start=1):
            Button(addDevWin, text=device_type, command=lambda device=device_type: create_smart_device(device)).grid(
                row=i, column=0)

        for widget in self.mainFrame.winfo_children():
            grid_info = widget.grid_info()
            if grid_info['row'] > self.i:
                updated_row = grid_info['row'] + 1
                widget.grid_configure(row=updated_row)

        b = self.i
        self.addButton(b)

    def deleteRow(self, idx):
        for widget in self.mainFrame.winfo_children():
            grid_info = widget.grid_info()
            if grid_info['row'] == idx:
                widget.destroy()

        # Update the indices of toggle and edit buttons after deleting a row
        for widget in self.mainFrame.winfo_children():
            grid_info = widget.grid_info()
            if grid_info['row'] > idx:
                updated_row = grid_info['row'] - 1
                widget.grid_configure(row=updated_row)
        self.i -= 1

    def turnOnAllAndUpdateLabels(self):
        for device in self.smartHome.getDevices():
            if isinstance(device, SmartPlug) and not device.getSwitchedOn():
                device.toggleSwitch()
            elif isinstance(device, SmartTv) and not device.getSwitchedOn():
                device.toggleSwitch()

        for i, device in enumerate(self.smartHome.getDevices(), start=1):
            dev_name = f"dev_{i}"
            if isinstance(device, SmartTv):
                if device.getSwitchedOn():
                    globals()[dev_name].set(f"Tv: on, Channel: {device.getChannel()}")
                else:
                    globals()[dev_name].set(f"Tv: off, Channel: {device.getChannel()}")
            elif isinstance(device, SmartPlug):
                if device.getSwitchedOn():
                    globals()[dev_name].set(f"Plug: on, Consumption Rate: {device.getConsumptionRate()}")
                else:
                    globals()[dev_name].set(f"Plug: off, Consumption Rate: {device.getConsumptionRate()}")

    def turnOffAllAndUpdateLabels(self):
        for device in self.smartHome.getDevices():
            if isinstance(device, SmartPlug) and device.getSwitchedOn():
                device.toggleSwitch()
            elif isinstance(device, SmartTv) and device.getSwitchedOn():
                device.toggleSwitch()

        for i, device in enumerate(self.smartHome.getDevices(), start=1):
            dev_name = f"dev_{i}"
            if isinstance(device, SmartTv):
                if device.getSwitchedOn():
                    globals()[dev_name].set(f"Tv: on, Channel: {device.getChannel()}")
                else:
                    globals()[dev_name].set(f"Tv: off, Channel: {device.getChannel()}")
            elif isinstance(device, SmartPlug):
                if device.getSwitchedOn():
                    globals()[dev_name].set(f"Plug: on, Consumption Rate: {device.getConsumptionRate()}")
                else:
                    globals()[dev_name].set(f"Plug: off, Consumption Rate: {device.getConsumptionRate()}")

    def toggleDevice(self, deviceNum):
        deviceIndex = deviceNum - 1
        if 0 <= deviceIndex < len(self.smartHome.getDevices()):
            self.smartHome.toggleSwitch(deviceNum)

            # Update the corresponding label text
            dev_name = f"dev_{deviceNum}"
            if isinstance(self.smartHome.getDeviceAt(deviceNum), SmartPlug):
                if self.smartHome.getDeviceAt(deviceNum).getSwitchedOn():
                    globals()[dev_name].set(f"Plug: on, Consumption Rate: {self.smartHome.getDeviceAt(deviceNum).getConsumptionRate()}")
                else:
                    globals()[dev_name].set(f"Plug: off, Consumption Rate: {self.smartHome.getDeviceAt(deviceNum).getConsumptionRate()}")
            elif isinstance(self.smartHome.getDeviceAt(deviceNum), SmartTv):
                if self.smartHome.getDeviceAt(deviceNum).getSwitchedOn():
                    globals()[dev_name].set(f"TV: on, Channel: {self.smartHome.getDeviceAt(deviceNum).getChannel()}")
                else:
                    globals()[dev_name].set(f"TV: off, Channel: {self.smartHome.getDeviceAt(deviceNum).getChannel()}")

            for i in range(deviceNum):
                btnToggle = self.mainFrame.nametowidget(f".!frame.!button{i + 2}")
                btnToggle.configure(command=lambda i=i: self.toggleDevice(i))
                btnRemove = self.mainFrame.nametowidget(f".!frame.!button{i + 2}.1")
                btnRemove.configure(command=lambda i=i: self.removeDevice(i))

    def editDevice(self, idx):
        device = self.smartHome.getDeviceAt(idx)

        editWin = Toplevel(self.win)
        editWin.title("Edit Device")

        if isinstance(device, SmartTv):
            Label(editWin, text="Channel:").grid(row=0, column=0)
            channel_entry = Entry(editWin)
            channel_entry.insert(0, str(device.getChannel()))
            channel_entry.grid(row=0, column=1)

        elif isinstance(device, SmartPlug):
            Label(editWin, text="Consumption Rate:").grid(row=0, column=0)
            consumption_entry = Entry(editWin)
            consumption_entry.insert(0, str(device.getConsumptionRate()))
            consumption_entry.grid(row=0, column=1)

        def saveChanges():
            if isinstance(device, SmartTv):
                new_channel = int(channel_entry.get())
                device.setChannel(new_channel)
            elif isinstance(device, SmartPlug):
                new_consumption = int(consumption_entry.get())
                device.setConsumptionRate(new_consumption)

            # Update the label
            dev_name = f"dev_{idx}"
            if isinstance(device, SmartTv):
                globals()[dev_name].set(
                    f"Tv: on, Channel: {device.getChannel()}" if device.getSwitchedOn() else f"Tv: off, Channel: {device.getChannel()}")
            elif isinstance(device, SmartPlug):
                globals()[dev_name].set(
                    f"Plug: on, Consumption Rate: {device.getConsumptionRate()}" if device.getSwitchedOn() else f"Plug: off, Consumption Rate: {device.getConsumptionRate()}")

            editWin.destroy()

        Button(editWin, text="Save Changes", command=saveChanges).grid(row=1, columnspan=2)

        editWin.mainloop()


def setUpHome():
    myHome = SmartHome()
    valid_inputs = 5
    while valid_inputs > 0:
        device = input("Which device would you like to add?: Smart(P)lug or Smart(T)v \n (Choose P or T): ").lower()
        while device != "p" and device != "t":
            print("Invalid input, try again. \n ")
            device = input("Which device would you like to add?: Smart(P)lug or Smart(T)v \n (Choose P or T): ").lower()
        if device == "p":
            valid_consumption = False
            while not valid_consumption:
                rate = input("Set consumption rate (Between 0 and 150): ")
                if rate.isdigit():
                    rate = int(rate)
                    if 0 <= rate <= 150:
                        plugDevice = SmartPlug(rate)
                        myHome.addDevice(plugDevice)
                        valid_inputs -= 1
                        valid_consumption = True
                    else:
                        print("Consumption rate is invalid")
                else:
                    print("Invalid input, try again:")
        elif device == "t":
            tvDevice = SmartTv()
            myHome.addDevice(tvDevice)
            valid_inputs -= 1
    return myHome


def main():
    myHome = setUpHome()
    mySmartHomeSystem = SmartHomeSystem(myHome)
    mySmartHomeSystem.run()


main()