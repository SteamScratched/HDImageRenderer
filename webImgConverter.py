from PIL import Image
import sys,pyperclip
import tkinter
im = Image.open(sys.argv[1]) #Can be many different formats.
pix = im.load()
if __name__ == "__main__":
	string = ""
	x,y = 0,0
	width = int(input("Width: "))
	height = int(input("Height: "))

	while y<height:
		x = 0
		while x<width:
			rgb = str(pix[x,y][0])+","+str(pix[x,y][1])+","+str(pix[x,y][2])
			string += ","+rgb
			x += 1

		y += 1
	string = string[1:]
	pyperclip.copy(string)
	print("Copied!")