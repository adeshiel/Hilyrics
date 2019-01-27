from textgenrnn import textgenrnn
from spoti import *
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
CORS(app)

# if __name__ == '__main__':
#    app.run(
#        debug=True,
#    )



textgen = textgenrnn()



class gen:



	def __init__(self, filename):
		'''Generates file names'''
		print("start of init")
		# textgen.reset()
		self.file_name = filename
		self.lyrics = []

	def train(self):
		print("training started")
		textgen.train_from_file(self.file_name, num_epochs=10, gen_epochs=10)
		textgen.save('lyrics.hdf5')

	def generate_lyrics(self):
		textgen.load('lyrics.hdf5')
		self.lyrics = textgen.generate(n=20, return_as_list=True, temperature=1.0)

	def write_lyrics(self):
		file = open("generated_song.txt", "w")
		for line in self.lyrics:
			file.write(line + "\n")
		file.close()


@app.route('/<u>')
def givemetxt(u):
	main(u)
	f = open('generated_song.txt',"r")
	kepp = f.read()
	f.close()
	return kepp


def main(username):
	runall(username)
	time.sleep(45)
	print("here")
	song = gen('lyrical.txt')
	print("sleepy")
	song.train()
	song.generate_lyrics()
	song.write_lyrics()




# if __name__ == "__main__":
# 	main()
