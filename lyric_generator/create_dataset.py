from textgenrnn import textgenrnn 
from keras.utils.data_utils import get_file

textgen = textgenrnn()

def gen_2dlist():
	song = []
	file = open("not_afraid.txt", "r")
	for line in file:
		song.append(line.replace('\n', ''))
		

	file.close()
	return song

def gen_lyrics(arg):
	textgen.reset()
	# textgen.train_on_texts(arg, num_epochs=15, gen_epochs=15)
	textgen.train_from_file('not_afraid.txt', num_epochs=1, gen_epochs=1)
	textgen.save('lyrics.hdf5')
	
def gen():
	textgen_2 = textgenrnn('lyrics.hdf5')
	lyrics = textgen_2.generate(n=20, return_as_list=True, temperature=1.0)
	print(lyrics)




def new_model():
	textgen.reset()
	textgen.train_from_file('not_afraid.txt',
							 new_model=True,
							 rrn_bidirectional=True,
							 dim_embeddings=300,
							 num_epochs=5)

	print(textgen.model.summary())



def large_files():
	text = get_file('not_afraid.txt', origin='https://www.google.com/search?q=not+afraid+lyrics&rlz=1C1CHBF_enUS719US719&oq=not+a&aqs=chrome.0.69i59j69i60l2j69i57j69i60j0.1472j0j1&sourceid=chrome&ie=UTF-8')
	textgen.reset()
	textgen.train_from_largetext_file(text, new_model=True, num_epochs=1)


def main():
	song = gen_2dlist()
	print(type(song))
	gen_lyrics(song)
	gen()
	# tensor = my_func(song)
	# print(tensor)
	# new_model()
	# large_files()



if __name__ == "__main__":
	main()