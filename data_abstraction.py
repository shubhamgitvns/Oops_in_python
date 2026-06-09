class Remote:
    def press_power_button(self):
        self.__connect_circuit()
        print("TV turned on")
        
    def press_powerOof_button(self):
        self.__disconect_circuit()
        print("TV turned of")    

    #private function / hide complexity
    def __connect_circuit(self): 
        print("Internal circuit connected")
        
    def __disconect_circuit(self):
        print("Internal circuit disconnected")

remote = Remote()
remote.press_power_button()

remote.press_powerOof_button()
