# Copyright (c) 2015 Frederick Vandenbosch
# Author: Frederick Vandenbosch

import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
import Image
import ImageFont
import ImageDraw
import os

def display_time():
	# Collect current time and date
	current_time = time.strftime("%H:%M")
	current_date = time.strftime("%d/%m/%Y")

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 35)

	# Position time
	x_pos = (disp.width/2)-(string_width(font,current_time)/2)
	y_pos = 2 + (disp.height-4-8)/2 - 35
        
	# Draw time
	draw.text((x_pos, y_pos), current_time, font=font, fill=255)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 8)

	# Position date
	x_pos = (disp.width/2)-(string_width(font,current_date)/2)
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

	# Set font type and size
	font = ImageFont.truetype('Minecraftia.ttf', 8)

	for i in range(0, 4):
		# Position time
		x_pos = 2
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw time
		draw.text((x_pos, y_pos), channels[i], font=font, fill=255)

		# Position date
		x_pos = disp.width - 2 - string_width(font, subscribers[i])
		y_pos = 2 + (((disp.height-4)/5)*i)

		# Draw date
		draw.text((x_pos, y_pos), subscribers[i], font=font, fill=255)

	# Draw the image buffer
	disp.image(image)
	disp.display()

def display_network():
	ipaddress = system.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
	netmask = system.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
	gateway = system.popen("ifconfig wlan0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'").read()
	ssid = system.popen("iwconfig wlan0 | grep 'ESSID'").read()

	# Clear image buffer by drawing a black filled box
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 12)
        
        # Position date
        x_pos = 2
	y_pos = 2

	# Draw date
	draw.text((x_pos, y_pos), ssid, font=font, fill=255)
	
	# Set font type and size
        font = ImageFont.truetype('Minecraftia.ttf', 8)

	# Position time
	x_pos = 2
	y_pos = 2 + 12 + 16/2 - 8/2
        
	# Draw time
	draw.text((x_pos, y_pos), "IP: "+ipaddress, font=font, fill=255)

	# Position date
	y_pos = 2 + 12 + 16 + 16/2 - 8/2

	# Draw date
	draw.text((x_pos, y_pos), "NM: "+netmask, font=font, fill=255)

	# Position date
	y_pos = 2 + 12 + 16 + 16 + 16/2 - 8/2

	# Draw date
	draw.text((x_pos, y_pos), "GW: "+gateway, font=font, fill=255)
	
	# Draw the image buffer
	disp.image(image)
	disp.display()

def string_width(fontType,string):
	string_width = 0

	for i, c in enumerate(string):
		char_width, char_height = draw.textsize(c, font=fontType)
		string_width += char_width

	return string_width

# Set up GPIO with internal pull-up
GPIO.setmode(GPIO.BCM)	
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
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

prev_millis = 0
display = 0

while True:
	millis = int(round(time.time() * 1000))
	if((millis - prev_millis) > 500):
		# Cycle through different displays
		if(not GPIO.input(12)):
			display++
			if(display > 2):
				display = 0
			prev_millis = int(round(time.time() * 1000))

		# Trigger action based on current display
		elif(not GPIO.input(16)):
			if(display == 0):
				# do something
			elif(display == 1):
				# do something
			elif(display == 2):
				# do something
			prev_millis = int(round(time.time() * 1000))

	if(display == 0):
		display_time()
	elif(display == 1):
		display_network()
	elif(display == 2):
		display_social()

	time.sleep(0.1)