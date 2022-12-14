from time import time, sleep
from os import system
from sys import platform, argv
import json


class MainSettings:
    FPS = 5


if platform == "win32":
    from ctypes import *
    STD_OUTPUT_HANDLE = -11
    STDHANDLE = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    class COORDSET(Structure):
        _fields_ = [("X", c_long), ("Y", c_long)]

    def set_cursor_position(x: int, y: int) -> None:
        windll.kernel32.SetConsoleCursorPosition(STDHANDLE, COORDSET(x, y))
else:
    def set_cursor_position(x: int, y: int) -> None:
        print(f"\033[{x};{y}H")


class VideoPlayer:
    def __init__(self, frames: list[list[str]]):
        self.frames = frames

    def start(self):
        different_between_time = 1 / MainSettings.FPS

        for frame in self.frames:
            sleep(1 / MainSettings.FPS - different_between_time)
            start_time = time()

            set_cursor_position(0, 0)
            for line in frame:
                print(line)

            end_time = time()
            different_between_time = start_time - end_time


class Video:
    def __init__(self, frames):
        self.frames = frames
        self.player = VideoPlayer(self.frames)

    def start(self):
        self.player.start()


def main():
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]} <file>")

    print("Loading video...")
    with open(argv[1]) as f:
        frames = json.load(f)["data"]
    system("cls")
    print("Successful")
    Video(frames).start()


if __name__ == '__main__':
    main()
