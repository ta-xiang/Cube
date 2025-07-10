import numpy as np


class Cube:
    # U：上
    # D：下
    # F：前
    # B：后
    # L：左
    # R：右
    FACES = list("UDFBLR")
    COLORS = {0: "BLACK", 1: "YELLOW", 2: "WHITE", 3: "GREEN", 4: "BLUE", 5: "ORANGE"}

    cube = {}

    def __init__(self):
        self.reset()


    def reset(self):
        for color,face in enumerate(self.FACES):
            self.cube[face] = np.full((3, 3), color)

    def show(self):
        
        translation = {"U":"上","D":"下","F":"前","B":"后","L":"左","R":"右"}
        for face in self.cube.keys():
            print(translation[face])
            print(self.cube[face])
            print()

    def face_rotation(self,direction):
        match direction:
            #向上翻，左侧面看逆时针
            case up:
                self.cube["R"].T[:, ::-1]
                self.cube["L"]
                self.cube["F"],self.cube["U"],self.cube["B"],self.cube["D"] = self.cube["D"],self.cube["F"],self.cube["U"],self.cube["B"]
                
    
    # def layer_rotation(self):

if __name__ == "__main__":
    a = Cube()
    a.face_rotation("up")
    a.show()