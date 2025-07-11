import numpy as np


class Cube:
    # U：上
    # D：下
    # F：前
    # B：后
    # L：左
    # R：右
    FACES = list("UDFBLR")

    # 魔方的数据结构定义:十字展开图定义

    cube = {}

    def __init__(self):
        self.reset()

    def reset(self):
        for color, face in enumerate(self.FACES):
            self.cube[face] = np.full((3, 3), color)

    def show(self):

        cube = self.cube.copy()
        # cube["R"] = cube["R"][::-1]
        # cube["D"] = cube["D"][::-1]
        # cube["B"] = cube["B"][::-1]
        translation = {"U": "上", "D": "下", "F": "前", "B": "后", "L": "左", "R": "右"}
        # COLORS = {0: "ORANGE", 1: "RED", 2: "WHITE", 3: "YELLOW", 4: "GREEN", 5: "BLUE"}
        COLORS = {0: "橙", 1: "红", 2: "白", 3: "黄", 4: "绿", 5: "蓝"}

        for face in cube.keys():
            print(translation[face])
            for layer in cube[face]:
                for block in layer:
                    print(COLORS[block], end="")
                print()
            print()

    # 面旋转,共有六种方向的旋转,分别是 "up","down","left","right","clockwise","counterclockwise"
    # 允许简写输入

    def face_rotation(self, direction):
        match direction:
            # 向上翻，左侧面看逆时针
            case "up":
                self.cube["R"] = self.cube["R"].T[:, ::-1]
                self.cube["L"] = self.cube["L"].T[::-1]
                self.cube["F"], self.cube["U"], self.cube["B"], self.cube["D"] = (
                    self.cube["D"].copy(),
                    self.cube["F"].copy(),
                    self.cube["U"].copy(),
                    self.cube["B"].copy(),
                )
            # 向下翻，左侧面看顺时针
            case "down":
                self.cube["R"] = self.cube["R"].T[::-1]
                self.cube["L"] = self.cube["L"].T[:, ::-1]
                self.cube["F"], self.cube["U"], self.cube["B"], self.cube["D"] = (
                    self.cube["U"].copy(),
                    self.cube["B"].copy(),
                    self.cube["D"].copy(),
                    self.cube["F"].copy(),
                )
            # 向左翻，上侧面看顺时针
            case "left":
                self.cube["U"] = self.cube["U"].T[:, ::-1]
                self.cube["D"] = self.cube["D"].T[::-1]
                (
                    self.cube["F"],
                    self.cube["R"],
                    self.cube["B"][::-1, ::-1],
                    self.cube["L"],
                ) = (
                    self.cube["R"].copy(),
                    self.cube["B"][::-1, ::-1].copy(),
                    self.cube["L"].copy(),
                    self.cube["F"].copy(),
                )
            # 向右翻，上侧面看逆时针
            case "right":
                self.cube["U"] = self.cube["U"].T[::-1]
                self.cube["D"] = self.cube["D"].T[:, ::-1]
                (
                    self.cube["F"],
                    self.cube["R"],
                    self.cube["B"][::-1, ::-1],
                    self.cube["L"],
                ) = (
                    self.cube["L"].copy(),
                    self.cube["F"].copy(),
                    self.cube["R"].copy(),
                    self.cube["B"][::-1, ::-1].copy(),
                )
            # 顺时针翻
            case "clockwise":
                self.cube["F"] = self.cube["F"].T[:, ::-1]
                self.cube["B"] = self.cube["B"].T[::-1]
                self.cube["U"], self.cube["R"], self.cube["D"], self.cube["L"] = (
                    self.cube["R"].T[:,::-1].copy(),
                    self.cube["D"].T[:,::-1].copy(),
                    self.cube["L"].T[:,::-1].copy(),
                    self.cube["U"].T[:,::-1].copy(),
                )
            # 逆时针翻
            case "counterclockwise":
                self.cube["F"] = self.cube["F"].T[::-1]
                self.cube["B"] = self.cube["B"].T[:, ::-1]
                self.cube["U"], self.cube["R"], self.cube["D"], self.cube["L"] = (
                    self.cube["R"].T[::-1].copy(),
                    self.cube["D"].T[::-1].copy(),
                    self.cube["L"].T[::-1].copy(),
                    self.cube["U"].T[::-1].copy(),
                )
            # 简写输入
            case "U":
                self.face_rotation("up")
            case "D":
                self.face_rotation("down")
            case "L":
                self.face_rotation("left")
            case "R":
                self.face_rotation("right")
            case "C":
                self.face_rotation("clockwise")
            case "CC":
                self.face_rotation("counterclockwise")

    # 层旋转,共有八中旋转方式,分别是 "rightup","rightdown","leftup","leftdown","upright","upleft","downright","downleft"
    # 允许简写输入
    # ※※※其中"UL","UR","DL","DR"四种操作因为展开图的原因,"B"(后)层涉及行需要进行行倒置和元素倒置
    def layer_rotation(self, direction):
        match direction:
            # 右层上拧
            case "rightup":
                self.cube["R"] = self.cube["R"].T[:, ::-1]
                (
                    self.cube["F"][:, -1],
                    self.cube["U"][:, -1],
                    self.cube["B"][:, -1],
                    self.cube["D"][:, -1],
                ) = (
                    self.cube["D"][:, -1].copy(),
                    self.cube["F"][:, -1].copy(),
                    self.cube["U"][:, -1].copy(),
                    self.cube["B"][:, -1].copy(),
                )
            # 右层下拧
            case "rightdown":
                self.cube["R"] = self.cube["R"].T[::-1]
                (
                    self.cube["F"][:, -1],
                    self.cube["U"][:, -1],
                    self.cube["B"][:, -1],
                    self.cube["D"][:, -1],
                ) = (
                    self.cube["U"][:, -1].copy(),
                    self.cube["B"][:, -1].copy(),
                    self.cube["D"][:, -1].copy(),
                    self.cube["F"][:, -1].copy(),
                )
            # 左层上拧
            case "leftup":
                self.cube["L"] = self.cube["L"].T[::-1]
                (
                    self.cube["F"][:, 0],
                    self.cube["U"][:, 0],
                    self.cube["B"][:, 0],
                    self.cube["D"][:, 0],
                ) = (
                    self.cube["D"][:, 0].copy(),
                    self.cube["F"][:, 0].copy(),
                    self.cube["U"][:, 0].copy(),
                    self.cube["B"][:, 0].copy(),
                )
            # 左层下拧
            case "leftdown":
                self.cube["L"] = self.cube["L"].T[:, ::-1]
                (
                    self.cube["F"][:, 0],
                    self.cube["U"][:, 0],
                    self.cube["B"][:, 0],
                    self.cube["D"][:, 0],
                ) = (
                    self.cube["U"][:, 0].copy(),
                    self.cube["B"][:, 0].copy(),
                    self.cube["D"][:, 0].copy(),
                    self.cube["F"][:, 0].copy(),
                )
            # 上层左拧
            case "upleft":
                self.cube["U"] = self.cube["U"].T[:, ::-1]
                (
                    self.cube["F"][0],
                    self.cube["R"][0],
                    # 此处特别注意
                    self.cube["B"][-1, ::-1],
                    self.cube["L"][0],
                ) = (
                    self.cube["R"][0].copy(),
                    self.cube["B"][-1, ::-1].copy(),
                    self.cube["L"][0].copy(),
                    self.cube["F"][0].copy(),
                )
            # 上层右拧
            case "upright":
                self.cube["U"] = self.cube["U"].T[::-1]
                (
                    self.cube["F"][0],
                    self.cube["R"][0],
                    self.cube["B"][-1, ::-1],
                    self.cube["L"][0],
                ) = (
                    self.cube["L"][0].copy(),
                    self.cube["F"][0].copy(),
                    self.cube["R"][0].copy(),
                    self.cube["B"][-1, ::-1].copy(),
                )
            # 下层左拧
            case "downleft":
                self.cube["D"] = self.cube["D"].T[::-1]
                (
                    self.cube["F"][-1],
                    self.cube["R"][-1],
                    self.cube["B"][0, ::-1],
                    self.cube["L"][-1],
                ) = (
                    self.cube["R"][-1].copy(),
                    self.cube["B"][0, ::-1].copy(),
                    self.cube["L"][-1].copy(),
                    self.cube["F"][-1].copy(),
                )
            # 下层右拧
            case "downright":
                self.cube["D"] = self.cube["D"].T[:, ::-1]
                (
                    self.cube["F"][-1],
                    self.cube["R"][-1],
                    self.cube["B"][0, ::-1],
                    self.cube["L"][-1],
                ) = (
                    self.cube["L"][-1].copy(),
                    self.cube["F"][-1].copy(),
                    self.cube["R"][-1].copy(),
                    self.cube["B"][0, ::-1].copy(),
                )
            case "RU":
                self.layer_rotation("rightup")
            case "RD":
                self.layer_rotation("rightdown")
            case "LU":
                self.layer_rotation("leftup")
            case "LD":
                self.layer_rotation("leftdown")
            case "UR":
                self.layer_rotation("upright")
            case "UL":
                self.layer_rotation("upleft")
            case "DR":
                self.layer_rotation("downright")
            case "DL":
                self.layer_rotation("downleft")


if __name__ == "__main__":
    a = Cube()

    # a.show()

    # print("向上翻")
    # a.face_rotation("U")
    # print("向下翻")
    # a.face_rotation("D")
    # print("向左翻")
    # a.face_rotation("L")
    # print("向右翻")
    # a.face_rotation("R")
    # print("顺时针翻")
    # a.face_rotation("C")
    # print("逆时针翻")
    # a.face_rotation("CC")

    # print("右层上拧")
    # a.layer_rotation("RU")
    # print("右层下拧")
    # a.layer_rotation("RD")
    # print("左层上拧")
    # a.layer_rotation("LU")
    # print("左层下拧")
    # a.layer_rotation("LD")
    print("上层左拧")
    a.layer_rotation("UL")
    a.layer_rotation("RD")
    a.layer_rotation("UL")
    a.layer_rotation("RD")
    a.layer_rotation("UL")
    a.layer_rotation("RD")
    a.face_rotation("U")
    a.face_rotation("CC")
    a.face_rotation("R")

    a.show()
