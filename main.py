import numpy as np
from pynput import keyboard
from pynput.keyboard import Listener
from os import system
from time import sleep


class Main:
    def __init__(self):
        self.is_game = True
        self.listener = Listener(on_release=self.move)

        self.pos_x = 3
        self.field = np.zeros((5, 5))

        self.current_player = 1
        self.max_player = 2
        self.win_length = 4

    def main(self):
        self.listener.start()

        while self.is_game:
            self.__show_field()

        self.listener.stop()
        print(f"Player {self.current_player} won!")
        sleep(10)

    def move(self, key):
        try:
            if key.char == 'd':
                self.pos_x += 1

                if self.pos_x > len(self.field[0]) - 1:
                    self.pos_x = 0

            elif key.char == 'a':
                self.pos_x -= 1

                if self.pos_x < 0:
                    self.pos_x = len(self.field[0]) - 1

        except AttributeError as exc:
            print(exc)

        if key == keyboard.Key.enter:
            try:
                self.drop_cell()

            except Exception as exc:
                print("Position is occupied!\n", exc)
                sleep(2)

            if self.check_win():
                self.is_game = False

            self.switch_player()

    def drop_cell(self):
        current_y = len(self.field[self.pos_x]) - 1

        while self.field[current_y][self.pos_x] != 0:
            current_y -= 1

        self.field[current_y][self.pos_x] = self.current_player

    def switch_player(self):
        if self.current_player < self.max_player:
            self.current_player += 1
        else:
            self.current_player = 1

    def __show_field(self):
        print(f"Position: {self.pos_x}\n{' ' * (self.pos_x + 5)}|")
        print(self.field)

        sleep(0.1)
        system("cls")

    def check_win(self):
        for i in range(self.field.shape[0]):
            if self._check_line(self.field[i]):
                return True

            vertical_line = [self.field[0][i]]

            for j in range(1, self.field.shape[0]):
                vertical_line.append(self.field[j][i])

            if self._check_line(vertical_line):
                return True

        if self._check_line(self.field.diagonal()):
            return True

        reversed_field = np.rot90(self.field.copy())

        if self._check_line(reversed_field.diagonal()):
            return True

        return False

    def _check_line(self, line):
        cells_together = 0

        for position in line:
            if position == self.current_player:
                cells_together += 1
            else:
                cells_together = 0

            if cells_together == self.win_length:
                return True

        return False


if __name__ == '__main__':
    game = Main()
    game.main()
