import json

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


class App:
	def __init__(self):
		self.root = Tk()
		self.root.title("YT-MP3-DOWNLOADER")
		self.root.iconbitmap("yt.ico")
		self.frm = ttk.Frame(self.root, padding=40)
		self.frm.grid()

		ttk.Label(self.frm, text="Insert YT URL").grid(column=0, row=0)
		self.url = StringVar()
		self.url_entry = ttk.Entry(self.frm, width=70, textvariable=self.url).grid(column=1, row=0)
		ttk.Button(self.frm, text="Download", command=self.download).grid(column=2, row=0)

		ttk.Label(self.frm, text="Download Folder").grid(column=0, row=1)
		self.dw_path = StringVar(self.root, json.load(open('config.json'))['save_path'])
		ttk.Label(self.frm, textvariable=self.dw_path ).grid(column=1, row=1)
		ttk.Button(self.frm, text="Select", command=self.setFolder).grid(column=2, row=1)

		self.root.mainloop()


	def download(self, *args):
		config = json.load(open('config.json'))
		YouTube(self.url.get()).streams.filter(only_audio=True).first().download(output_path=config['save_path'])


	def setFolder(self, *args):
		self.path = filedialog.askdirectory()
		self.dw_path.set(self.path)
		self.setPath(str(self.path))


	def setPath(self, path):
		with open("config.json", "w") as outfile:
			json.dump({"save_path": path}, outfile)


if __name__ == '__main__':
	App()