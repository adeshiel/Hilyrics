from textgenrnn import textgenrnn 


print("Start of code")
textgen = textgenrnn()
print("Hopefully not stuck")


class gen:

	

	def __init__(self):
		'''Generates file names'''
		print("start of init")
		self.file_names = ['not_afraid.txt']
		self.lyrics = []

	def train(self):
		textgen.reset()
		for file in self.file_names:
			print("training started")
			textgen.train_from_file(file, num_epochs=1, gen_epochs=1)
		textgen.save('lyrics.hdf5')

	def generate_lyrics(self):
		textgen.load('lyrics.hdf5')
		self.lyrics = textgen.generate(n=20, return_as_list=True, temperature=1.0)

	def write_lyrics(self):
		file = open("generated_song.txt", "r")
		for line in self.lyrics:
			file.write(line)
		file.close()



def main():
	song = gen()
	song.train()
	song.generate_lyrics()
	song.write_lyrics()


if __name__ == "__main__":
	main()