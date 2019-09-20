import numpy as np
from pynput import keyboard
from pynput.keyboard import Listener
from os import system
from threading import Thread
from time import sleep


class Main:
    def __init__(self):
        self.pos_x = 3
        self.field = np.zeros((5, 5))

        self.current_player = 1
        self.max_player = 2

    def main(self):
        show = Thread(target=self.__show_field)
        listener = Listener(on_release=self.move)

        listener.start()
        show.start()

        listener.join()
        show.join()

    def move(self, key):
        try:
            if key.char == 'd':
                self.pos_x += 1

                if self.pos_x > len(self.field[0]) - 1:
                    self.pos_x = 0

            elif key.char == 'a':
                self.pos_x -= 1

                if self.pos_x < 0:
                    self.pos_x = len(self.field[0])

        except AttributeError as exc:
            pass

        if key == keyboard.Key.enter:
            try:
                self.drop_cell()

            except Exception as exc:
                print("Position is occupied!\n", exc)
                sleep(2)

            self.check_win()
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
        while True:
            print(f"Position: {self.pos_x}\n{' ' * (self.pos_x + 5)}|")
            print(self.field)

            sleep(0.1)
            system("cls")

    def check_win(self):
        one_field = self.field.copy()

        diagonal_left = one_field.diagonal()
        diagonal_right = np.diag(np.rot90(one_field))
        sum_number = self.current_player * 4

        if diagonal_left.prod() == sum_number or diagonal_right.prod() == sum_number:
            print("You won!")
            sleep(10)
            exit(0)


if __name__ == '__main__':
    game = Main()
    game.main()
