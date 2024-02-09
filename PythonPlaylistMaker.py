import os
playlist = []
Quit = False

os.system("cls")
print("This is the python playlist maker.")

def help():
	print("Add\n\tadds a new song at the end of your playlist")
	print("\n\nInsert\n\tinserts a new song in a specific point in your playlist")
	print("\n\nRemove\n\tRemoves a song from a specific point in your playlist")
	print("\n\nSearch\n\tSearches your playlist for a specific song and returns True if said song is in your playlist.")
	print("\n\nTotal\n\tReturns the number of total songs in your playlist")
	print("\n\nPrint\n\tPrints your playlist")
	print("\n\nQuit\n\tQuits the program")

def add(song):
	playlist.append(song)
	print(f"Added {song} to your playlist!")

def insert(song, position):
	playlist.insert(position, song)
	print(f"Added {song} to your playlist at {position}")

def remove(song):
	try:
		playlist.remove(song)
		os.system("cls")
		print(f"removed {song} from your playlist")
	except:
		print("You didn't type a song that was in your playlist, please try again.")

def search(song):
	try:
		playlist.index(song)
		print(f"{song} is in your playlist")
	except:
		print(f"{song} isn't in your playlist")

def total():
	print(f"the size of your playlist is {len(playlist)} songs long.")

def printPlaylist():
	for i in range(len(playlist)):
		print(f"[{i}]: {playlist[i]}")

while not Quit:
	print("\n\nCommands: \"help\", \"add\", \"insert\", \"remove\", \"search\", and \"total\"")
	command = input("What would you like to do?\n: ")
	
	os.system("cls")
	if command == "add":
		song = input("What song would you like to add?\n: ")
		add(song)
	elif command == "insert":
		song = input("What song would you like to add?\n: ")
		position = input("Where would you like to add the song in your playlist?\n: ")
		insert(song, position)
	elif command == "remove":
		song = input("What song would you like to remove?\n: ")
		remove(song)
	elif command == "search":
		song = input("What song would you like to search for?\n: ")
		search(song)
	elif command == "total":
		total()
	elif command == "print":
		printPlaylist()
	elif command == "help":
		help()
	elif command == "quit":
		Quit = True
os.system("cls")
print("Playlist maker has quit. Thank you for using Playlist maker today.")