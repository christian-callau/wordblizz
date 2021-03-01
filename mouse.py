import pyautogui


class MouseController:
    def __init__(self, base, size):
        self.base = base
        self.size = size

    def drag(self, coords, speed=.01):
        coords = self.translate(coords)
        pyautogui.moveTo(coords[0][1], coords[0][0])
        pyautogui.mouseDown()
        for coord in coords[1:]:
            pyautogui.moveTo(coord[1], coord[0], speed)
        pyautogui.mouseUp()

    def translate(self, coords):
        x0 = self.base[0] + self.size // 2
        y0 = self.base[1] + self.size // 2
        return [[x0 + coord[0] * self.size, y0 + coord[1] * self.size] for coord in coords]
