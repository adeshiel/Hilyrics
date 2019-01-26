import tensorflow as tf 



def gen_2dlist():
	song = []
	file = open("not_afraid.txt", "r")
	line = []
	for word in file.read().split():
		line.append(word)
		if len(line) == 10:
			song.append(line)
			line = []

	file.close()
	return song



def my_func(arg):
	arg = tf.convert_to_tensor(arg, dtype=tf.string)
	return arg










def main():
	song = gen_2dlist()
	print(song)
	for l in song:
		print(len(l))
	tensor = my_func(song)
	print(tensor)



if __name__ == "__main__":
	main()