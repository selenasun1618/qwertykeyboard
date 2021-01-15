#Calls on qwerty.py to display a QWERTY keyboard
import sys, pygame
from qwerty import Qwerty

qwerty = Qwerty()

def main():
	qwerty.keypad()

if __name__ == '__main__':
	main()