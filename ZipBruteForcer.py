import sys, zipfile
if len(sys.argv) <2:
	print ("Usage=ZipBruteForcer.py ZipFileYouWantToCrack PasswordList" "\n" "Example: ZipBruteForcer.py Video.zip MySuperSuperemePasswordList.txt")
	sys.exit()
def ZipBruteForcer(passwordList,action):
	with open(passwordList, 'rb') as file:
		for line in file:
			for word in line.split():
				try:
					action.extractall(pwd=word)
					print(word.decode())
				finally:
					continue
zip_file = sys.argv[1]
passwordList = sys.argv[2]
action = zipfile.ZipFile(zip_file)
if ZipBruteForcer(passwordList, action) == False:
	sys.exit()
