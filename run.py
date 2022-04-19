import configparser
import shutil
import json

config = configparser.ConfigParser(allow_no_value=True)
config_file = '/data/shared/params.ini'
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

json_file = '/data/shared/code.json'
f = open(json_file, "r")
data = json.loads(f.read(), strict=False)
codeSnippet = data['codeSnippet']
print("The Code you entered:")
print(codeSnippet)
f.close()

shutil.copyfile("/data/output/earth.vtp", "/data/shared/earth.vtp")
shutil.copyfile("/data/output/coffee-temp.csv", "/data/shared/coffee-temp.csv")
shutil.copyfile("/data/output/coffee.jpg", "/data/shared/image-coffee.jpg")
shutil.copyfile("/data/output/dance.png", "/data/shared/image-dance.png")
shutil.copyfile("/data/shared/params.ini", "/data/shared/input.ini")
shutil.copyfile("/data/shared/code.json", "/data/shared/input.json")
