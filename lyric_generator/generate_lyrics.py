from textgenrnn import textgenrnn 



textgen = textgenrnn()



class gen:

	

	def __init__(self, filename):
		'''Generates file names'''
		print("start of init")
		self.file_name = filename
		self.lyrics = []

	def train(self):
		textgen.reset()
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



def main():
	song = gen()
	song.train()
	song.generate_lyrics()
	song.write_lyrics()


if __name__ == "__main__":
	main()