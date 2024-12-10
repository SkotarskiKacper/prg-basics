class SmartPhone:
    States=[
        "OFF",
        "Low Power",
        "Normal"
    ]

    def __init__(self,Battery,isOn):
        self.battery=Battery
        self.isOn=isOn
        self.state=self.DetermineState()
    
    def DetermineState(self):
        if not self.isOn:
            return self.States[0]
        elif self.battery>15:
            return self.States[2]
        elif self.battery<=0:
            self.battery=0
            return self.States[0]
        else:
            return self.States[1]

    def ChangeBattery(self,newCharge):
        self.battery=newCharge
        self.state=self.DetermineState()

    def PushPowerButton(self):
        if self.isOn:
            self.isOn=False
        else:
            self.isOn=True
        self.state=self.DetermineState()

    def DisplayInfo(self):
        print(f"Battery:{self.battery}%, CurrentState:{self.state}")

def main():

    MyPhone=SmartPhone(50,True)
    MyPhone.DisplayInfo()
    MyPhone.ChangeBattery(10)
    MyPhone.DisplayInfo()
    MyPhone.PushPowerButton()
    MyPhone.DisplayInfo()
    MyPhone.PushPowerButton()
    MyPhone.ChangeBattery(-5)
    MyPhone.DisplayInfo()

if __name__=="__main__":
    main()

