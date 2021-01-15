import sys, pygame
import threading, time
from pygame.locals import *
from sys import exit

pygame.init()
width = pygame.display.Info().current_w
height = int(width / 3 + width / 15) #Qwerty width:height ratio is 3:1, add space for the text bar
SCREEN_SIZE = (width, height)

#KEYPAD INFO
KEYPAD_ORIGIN = (width / 40, width / 15) #leaves margins
KEY_SIZE = (int(width - 2 * KEYPAD_ORIGIN[0]) / 15, int(width - 2 * KEYPAD_ORIGIN[0]) / 15) #standard square key size
COLOR_DOWN = (158, 183, 235)
COLOR_UP = (225, 225, 225)
COLOR_TEXT = (0, 0, 0)
KEYPAD_NUM_KEYS = 61

#TEXT BAR INFO
KEYPAD_TEXT_BAR_POSITION = (KEYPAD_ORIGIN[0], width / 150)
KEYPAD_TEXT_BAR_SIZE = (width - 2 * KEYPAD_ORIGIN[0], int(0.8 * width  / 15))
KEYPAD_TEXT_BAR_COLOR = (158, 183, 235)
KEYPAD_TEXT_BAR_BACKGROUND_COLOR = (0, 0, 0)

#MESSAGE INFO
MESSAGE_FONT_SIZE = int(0.8 * KEYPAD_TEXT_BAR_SIZE[1])
MESSAGE_FONT_POSITION = (KEYPAD_TEXT_BAR_POSITION[0] + width / 100, KEYPAD_TEXT_BAR_POSITION[1] + KEYPAD_TEXT_BAR_SIZE[1] / 4)


KEYPAD_KEY_POSITION_LIST = [

	#FIRST ROW
	(KEYPAD_ORIGIN[0] + 0 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 1.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 2.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 3.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # SPACEBAR
	(KEYPAD_ORIGIN[0] + 10 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 11.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 12.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 13.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 4 * KEY_SIZE[1]), # empty

	#SECOND ROW
	(KEYPAD_ORIGIN[0] + 0 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 2.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # Z
	(KEYPAD_ORIGIN[0] + 3.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # X
	(KEYPAD_ORIGIN[0] + 4.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # C
	(KEYPAD_ORIGIN[0] + 5.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # V
	(KEYPAD_ORIGIN[0] + 6.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # B
	(KEYPAD_ORIGIN[0] + 7.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # N
	(KEYPAD_ORIGIN[0] + 8.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # M
	(KEYPAD_ORIGIN[0] + 9.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # ,
	(KEYPAD_ORIGIN[0] + 10.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # .
	(KEYPAD_ORIGIN[0] + 11.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # /
	(KEYPAD_ORIGIN[0] + 12.25 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 3 * KEY_SIZE[1]), # empty

	#THIRD ROW
	(KEYPAD_ORIGIN[0] + 0 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 1.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # A
	(KEYPAD_ORIGIN[0] + 2.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # S
	(KEYPAD_ORIGIN[0] + 3.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # D
	(KEYPAD_ORIGIN[0] + 4.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # F
	(KEYPAD_ORIGIN[0] + 5.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # G
	(KEYPAD_ORIGIN[0] + 6.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # H
	(KEYPAD_ORIGIN[0] + 7.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # J
	(KEYPAD_ORIGIN[0] + 8.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # K
	(KEYPAD_ORIGIN[0] + 9.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # L
	(KEYPAD_ORIGIN[0] + 10.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # ;
	(KEYPAD_ORIGIN[0] + 11.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # “
	(KEYPAD_ORIGIN[0] + 12.75 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 2 * KEY_SIZE[1]), # ENTER

	#FOURTH ROW
	(KEYPAD_ORIGIN[0] + 0 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # empty
	(KEYPAD_ORIGIN[0] + 1.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # Q
	(KEYPAD_ORIGIN[0] + 2.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # W
	(KEYPAD_ORIGIN[0] + 3.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # E
	(KEYPAD_ORIGIN[0] + 4.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # R
	(KEYPAD_ORIGIN[0] + 5.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # T
	(KEYPAD_ORIGIN[0] + 6.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # Y
	(KEYPAD_ORIGIN[0] + 7.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # U
	(KEYPAD_ORIGIN[0] + 8.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # I
	(KEYPAD_ORIGIN[0] + 9.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # O
	(KEYPAD_ORIGIN[0] + 10.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # P
	(KEYPAD_ORIGIN[0] + 11.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # [
	(KEYPAD_ORIGIN[0] + 12.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # ]
	(KEYPAD_ORIGIN[0] + 13.5 * KEY_SIZE[0], KEYPAD_ORIGIN[1] + 1 * KEY_SIZE[1]), # \

	#FIFTH ROW
	(KEYPAD_ORIGIN[0] + 0 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # empty
	(KEYPAD_ORIGIN[0] + 1 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 1
	(KEYPAD_ORIGIN[0] + 2 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 2
	(KEYPAD_ORIGIN[0] + 3 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 3
	(KEYPAD_ORIGIN[0] + 4 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 4
	(KEYPAD_ORIGIN[0] + 5 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 5
	(KEYPAD_ORIGIN[0] + 6 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 6
	(KEYPAD_ORIGIN[0] + 7 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 7
	(KEYPAD_ORIGIN[0] + 8 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 8
	(KEYPAD_ORIGIN[0] + 9 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 9
	(KEYPAD_ORIGIN[0] + 10 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # 0
	(KEYPAD_ORIGIN[0] + 11 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # -
	(KEYPAD_ORIGIN[0] + 12 * KEY_SIZE[0], KEYPAD_ORIGIN[1]), # =
	(KEYPAD_ORIGIN[0] + 13 * KEY_SIZE[0] ,KEYPAD_ORIGIN[1]) # DEL
]

KEYPAD_KEY_SIZE_LIST = [

	#FIRST ROW
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]), #empty
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]),
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]),
	(KEY_SIZE[0] * 6.25, KEY_SIZE[1]), # SPACEBAR
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]),
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]),
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]),
	(KEY_SIZE[0] * 1.25, KEY_SIZE[1]),

	#SECOND ROW
	(KEY_SIZE[0] * 2.25, KEY_SIZE[1]),
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	(KEY_SIZE[0] * 2.75, KEY_SIZE[1]),

	#THIRD ROW
	(KEY_SIZE[0] * 1.75, KEY_SIZE[1]),
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	(KEY_SIZE[0] * 2.25, KEY_SIZE[1]), #ENTER

	#FOURTH ROW
	(KEY_SIZE[0] * 1.5, KEY_SIZE[1]),
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	(KEY_SIZE[0] * 1.5, KEY_SIZE[1]), # \

	#FIFTH ROW
	(KEY_SIZE[0] * 1, KEY_SIZE[1]),
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	KEY_SIZE,
	(KEY_SIZE[0] * 2.0, KEY_SIZE[1]) #DEL
]

KEYPAD_KEY_VALUE_LIST = [
"","",""," ","","","","",
"","Z","X","C","V","B","N","M",",",".","/","",
"","A","S","D","F","G","H","J","K","L",";","'","ENTER",
"","Q","W","E","R","T","Y","U","I","O", "P", "[", "]","\\",
"","1","2","3","4","5","6","7","8","9","0","-","=","DEL"
]


class Qwerty:
	#Initializing call
	def __init__ (self):
		pygame.init()
		self.screen = pygame.display.set_mode(SCREEN_SIZE)
		pygame.display.set_caption('Qwerty Keyboard');

		#KEYPAD
		self.key_font = pygame.font.SysFont("Arial", round(KEY_SIZE[1] / 2), bold=False, italic=False)
		self.key_rect_list = []
		self.key_text_list = []
		for i in range(KEYPAD_NUM_KEYS):
			self.key_rect_list.append(pygame.Rect(KEYPAD_KEY_POSITION_LIST[i], KEYPAD_KEY_SIZE_LIST[i]))
			self.key_text_list.append(self.key_font.render(str(KEYPAD_KEY_VALUE_LIST[i]), True, COLOR_TEXT))

		#Draw text bar
		self.text_bar_rect = pygame.Rect(KEYPAD_TEXT_BAR_POSITION, KEYPAD_TEXT_BAR_SIZE)

		#Message font settings
		self.message_font = pygame.font.SysFont("Arial", MESSAGE_FONT_SIZE, bold=False, italic=False)

	#Code borrowed & edited from display_service.py
	#Draws the QWERTY keyboard on the display
	def _draw_keypad(self, key_status_list):
			self.key_textpos_list = []
			for i in range(KEYPAD_NUM_KEYS):
				left, top = KEYPAD_KEY_POSITION_LIST[i]
				self.key_textpos_list.append(pygame.Rect((left + (KEY_SIZE[0] * 9 / 25), top + (KEY_SIZE[0] * 9 / 25)), KEY_SIZE)) # to center character
				if key_status_list[i]:
				# key has been pressed
					key_color = COLOR_DOWN
					pygame.draw.rect(self.screen, key_color, self.key_rect_list[i])
				else:
				# key has not been pressed
					key_color = COLOR_UP
					pygame.draw.rect(self.screen, key_color, self.key_rect_list[i], 5)
				self.screen.blit(self.key_text_list[i], self.key_textpos_list[i])

	#Code borrowed & edited from display_service
	#Draws the text box on the display, above the keyboard
	def _draw_message(self, message_text, message_color=(0, 0, 0)):
			self.screen.fill((255,255,255))
			font = self.message_font.render(message_text, True, message_color)
			pygame.draw.rect(self.screen, KEYPAD_TEXT_BAR_COLOR, self.text_bar_rect, 5)
			self.screen.blit(font, MESSAGE_FONT_POSITION)

	#Code inspired by event_service.py
	#Gets mouse clicks
	def get_clicks(self):
		ACCEPTED_MOUSE_EVENTS = [pygame.MOUSEBUTTONDOWN]
		self.mouse_events = []
		self.event_list_lock = threading.Lock()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.display.quit()
				pygame.quit()
				sys.exit()
			if event.type in ACCEPTED_MOUSE_EVENTS:
				with self.event_list_lock:
					self.mouse_events.append(event)
		with self.event_list_lock:
			mouse_events = self.mouse_events.copy()
			self.mouse_events = []
		return mouse_events

	#Code borrowed & edited from display_service
	#QWERTY Keyboard: click on letters to type, press 'ENTER' to print to console and clear text bar
	def keypad(self):
			pygame.init()
			key_status_list = [False] * 61
			entered_val = ""

			while True: #Exits when 'Enter' is pressed
				self._draw_message(entered_val)
				self._draw_keypad(key_status_list)
				pygame.display.update()
				entered_val_text = self.key_font.render(entered_val, True, KEYPAD_TEXT_BAR_COLOR)
				pygame.draw.rect(self.screen, KEYPAD_TEXT_BAR_BACKGROUND_COLOR, self.text_bar_rect)
				self.screen.blit(entered_val_text, self.text_bar_rect)
				for event in self.get_clicks():
					 if event.type == pygame.MOUSEBUTTONDOWN:
					 		for i, key_rect in enumerate(self.key_rect_list):
					 			if (key_rect.collidepoint(event.pos)):
					 				key_status_list = [False] * KEYPAD_NUM_KEYS #Unpress keys
					 				key_status_list[i] = True
					 				key_val = KEYPAD_KEY_VALUE_LIST[i]
					 				if key_val is "DEL":
					 					entered_val = entered_val[0:len(entered_val) - 1]
					 				elif key_val is "ENTER":
					 					print(entered_val)
					 					entered_val = ""
					 				else:
					 					entered_val += KEYPAD_KEY_VALUE_LIST[i]

