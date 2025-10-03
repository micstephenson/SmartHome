
# challenge1
class SmartDevice:
    def __init__(self):
        self.switchedOn = False

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn


# task 1
class SmartPlug(SmartDevice):
    def __init__(self, consumptionRate):
        super().__init__()
        self.consumptionRate = consumptionRate

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, newRate):
        if 0 <= newRate <= 150:
            self.consumptionRate = newRate

    def __str__(self):
        str = ""
        if self.switchedOn:
            str += "Smart Plug is switched on "
        else:
            str += "Smart Plug is switched off "
        str += f"with consumption rate {self.consumptionRate}"
        return str


def testSmartPlug():
    myPlug = SmartPlug(45)
    myPlug.toggleSwitch()
    print(myPlug.getSwitchedOn())
    print(myPlug.getConsumptionRate())
    myPlug.setConsumptionRate(70)
    print(myPlug.getConsumptionRate())
    print(myPlug)


# task2
class SmartTv(SmartDevice):
    def __init__(self):
        super().__init__()
        self.channel = 1

    def getChannel(self):
        return self.channel

    def setChannel(self, newChannel):
        if 1 <= newChannel <= 734:
            self.channel = newChannel

    def __str__(self):
        str = ""
        if self.switchedOn:
            str += "Smart Tv is switched on "
        else:
            str += "Smart Tv is switched off "
        str += f"at channel {self.channel}"
        return str


def testSmartTv():
    myTv = SmartTv()
    myTv.toggleSwitch()
    print(myTv.getSwitchedOn())
    print(myTv.getChannel())
    myTv.setChannel(604)
    print(myTv.getChannel())
    print(myTv)


# task 3
class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDeviceAt(self, deviceNum):
        devListLen = len(self.devices)
        if deviceNum <= devListLen:
            return self.devices[(deviceNum - 1)]

    def removeDeviceAt(self, deviceNum):
        deviceNum -= 1
        self.devices.pop(deviceNum)

    def addDevice(self, newDevice):
        self.devices.append(newDevice)

    def toggleSwitch(self, deviceNum):
        deviceNum -= 1
        if 0 <= deviceNum < len(self.devices):
            devToggle = self.devices[deviceNum]
            devToggle.toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            device.toggleSwitch()
            if not device.getSwitchedOn():
                device.toggleSwitch()

    def turnOffAll(self):
        for device in self.devices:
            device.toggleSwitch()
            if device.getSwitchedOn():
                device.toggleSwitch()

    def __str__(self):
        str = ""
        for device in self.devices:
            str += f"{device}\n"
        return str


def testSmartHome():
    myHome = SmartHome()
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    tv1 = SmartTv()
    plug1.toggleSwitch()
    plug1.setConsumptionRate(150)
    plug2.setConsumptionRate(25)
    tv1.setChannel(105)
    myHome.addDevice(plug1)
    myHome.addDevice(plug2)
    myHome.addDevice(tv1)
    myHome.toggleSwitch(2)
    print(myHome)
    myHome.turnOnAll()
    print(myHome)
    myHome.removeDeviceAt(1)
    print(myHome)


# testSmartPlug()
# testSmartTv()
# testSmartHome()
