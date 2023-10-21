
class Robot:
    
    # constructor
    def __init__(self, baterie, delka_rukou):
        self.bat = baterie
        self.del_ruk = delka_rukou
        self.ukony_do_kontroly = 1000

    def krok_vpred(self):
        print("Robot udelal krok vpred.")
        self.ukony_do_kontroly -= 1
        print(f"Ukony do kontroly: {self.ukony_do_kontroly}")

    def krok_vzad(self):
        print("Robot udelal krok vzad.")
        self.ukony_do_kontroly -= 1
        print(f"Ukony do kontroly: {self.ukony_do_kontroly}")

robot_1 = Robot(24, 0.7)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(72, 1.2)
robot_4 = Robot(96, 0.2)


robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()



#print(robot_2.bat)
#print(robot_2.del_ruk)
#print(robot_2.dny_do_opravy)

#print(robot_3.bat)
#print(robot_3.del_ruk)
#print(robot_3.dny_do_opravy)

#print(robot_4.bat)
#print(robot_4.del_ruk)
#print(robot_4.dny_do_opravy)
















