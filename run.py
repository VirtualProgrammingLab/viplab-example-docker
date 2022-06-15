import configparser
import shutil
import os

cwd = os.getcwd()

config = configparser.ConfigParser(allow_no_value=True)
config_file = cwd + '/data/shared/params.ini'
config.read(config_file)

print("Your name is \033[0;35m", config['about you']['name'], "\033[0m")
print("Your current age is", config['about you']['age'])
print("Your Christmas Wish is:", config['about you']['christmasWish'])
print("How hot do you like to drink your Coffee?", config['coffee preference']['coffeeTemperature'])
print("You like: \033[0;32m", config['about you']['likedThings'], "\033[0m")
print("Your favorite Programming Language is", config['about you']['favoritePL'])
print("Your look in the frige:", config['about you']['fridge'])
print("You would dance in the kitchen to:", config['about you']['dancing'])
print("You dislike: \033[0;31m", config['about you']['dislikedThings'], "\033[0m")
print("Your three random numbers are:", config['about you']['randomNumbers'])

code_file = cwd + '/data/shared/code.c'
f = open(code_file, "r")
codeSnippet = f.read()
print("The Code you entered:")
print(codeSnippet)
f.close()

shutil.copyfile(cwd + "/data/output/earth.vtp", cwd + "/data/shared/earth.vtp")
shutil.copyfile(cwd + "/data/output/coffee-temp.csv", cwd + "/data/shared/coffee-temp.csv")
shutil.copyfile(cwd + "/data/output/coffee.jpg", cwd + "/data/shared/image-coffee.jpg")
shutil.copyfile(cwd + "/data/output/dance.png", cwd + "/data/shared/image-dance.png")
shutil.copyfile(cwd + "/data/output/uris.txt", cwd + "/data/shared/uris.txt")
shutil.copyfile(cwd + "/data/shared/params.ini", cwd + "/data/shared/input.ini")
shutil.copyfile(cwd + "/data/shared/code.c", cwd + "/data/shared/input.c")
