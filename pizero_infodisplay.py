# Copyright (c) 2015 Frederick Vandenbosch
# Author: Frederick Vandenbosch

import time

#import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Image
import ImageFont
import ImageDraw

def display_network():

	return 0

def display_time():
	# Collect current time and date
	current_time = time.strftime("%H:%M")
	current_date = time.strftime("%d/%m/%Y")

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Position time
	x_pos = (disp.width/2)-(string_width(current_time)/2)
	y_pos = 2

	# Draw time
	draw.text((x_pos, y_pos), current_time, font=font, fill=255)

	# Position date
	x_pos = (disp.width/2)-(string_width(current_date)/2)
	y_pos = disp.height-10

	# Draw date
	draw.text((x_pos, y_pos), current_date, font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_socialmedia():
	# Collect current time and date
	channels = ["YouTube", "Twitter", "Facebook", "Instagram", "Google+"]
	subscribers = [101, 229, 62, 23, 44]

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	for i in range(0, 4):
		# Position time
		x_pos = 2
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw time
		draw.text((x_pos, y_pos), channels[i], font=font, fill=255)

		# Position date
		x_pos = disp.width - 2 - string_width(subscribers[i])
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw date
		draw.text((x_pos, y_pos), subscribers[i], font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def string_width(string):
	string_width = 0

	for i, c in enumerate(string):
		char_width, char_height = draw.textsize(c, font=font)
		string_width += char_width

	return string_width
	
# 128x64 display with hardware I2C
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)

# Initialize library
disp.begin()

# Get display width and height
width = disp.width
height = disp.height

# Clear display
disp.clear()
disp.display()

# Create image buffer
# Make sure to create image with mode '1' for 1-bit color
image = Image.new('1', (width, height))

# Load default font
font = ImageFont.load_default()

# Create drawing object
draw = ImageDraw.Draw(image)


while True:
	# Read buttons

	# Pause briefly before drawing next frame
	time.sleep(0.1)