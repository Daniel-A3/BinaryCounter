import time, sys, os

def main():
	byte = [0, 0, 0, 0, 0, 0, 0, 0]
	
	while True:
		userInput = input("Welcome to Daniel's binary counter, 'q' to stop, enter to continue : ")

		if userInput == "":
			for i in range(0, 256):
				byte[7] = 1
				# decimal 1
				if i == 0 or i % 2 == 0:
					byte[7] = 0
				else:
					byte[7] = 1
				# decimal 2
				if float(i) % 2 == 0 and i != 0:
					if byte[6] == 0:
						byte[6] = 1
					else:
						byte[6] = 0
				#decimal 4
				if float(i) % 4 == 0 and i != 0:
					if byte[5] == 0:
						byte[5] = 1
					else:
						byte[5] = 0
				#decimal 8
				if float(i) % 8 == 0 and i != 0:
					if byte[4] == 0:
						byte[4] = 1
					else:
						byte[4] = 0
				#decimal 16
				if float(i) % 16 == 0 and i != 0:
					if byte[3] == 0:
						byte[3] = 1
					else:
						byte[3] = 0
				#decimal 32
				if float(i) % 32 == 0 and i != 0:
					if byte[2] == 0:
						byte[2] = 1
					else:
						byte[2] = 0
				#decimal 64
				if float(i) % 64 == 0 and i != 0:
					if byte[1] == 0:
						byte[1] = 1
					else:
						byte[1] = 0
				#decimal 128
				if float(i) % 128 == 0 and i != 0:
					if byte[0] == 0:
						byte[0] = 1
					else:
						byte[0] = 0

				print(byte)
				time.sleep(0.5)
				os.system('cls' if os.name == 'nt' else 'clear')

		elif userInput.upper() == "Q":
			break

if __name__ == "__main__":
	main()