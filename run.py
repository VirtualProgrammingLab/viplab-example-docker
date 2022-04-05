import configparser
import shutil
import json

config = configparser.ConfigParser(allow_no_value=True)
config_file = '/data/shared/params.ini'
config.read(config_file)
print("Your name is", config['about you']['name'])
print("Your currenr age is", config['about you']['age'])
print("Your Christmas Wish is:", config['about you']['christmasWish'])
print("How hot do you like to drink your Coffee?", config['coffee preference']['coffeeTemperature'])
print("You like:", config['about you']['likedThings'])
print("Your favorite Programming Language is", config['about you']['favoritePL'])
print("Your look in the frige:", config['about you']['fridge'])
print("You would dance in the kitchen to:", config['about you']['dancing'])
print("You dislike:", config['about you']['dislikedThings'])
print("Your three random numbers are:", config['about you']['randomNumbers'])

json_file = '/data/shared/code.json'
f = open(json_file, "r")
data = json.loads(f.read(), strict=False)
codeSnippet = data['codeSnippet']
print("The Code you entered:")
print(codeSnippet)
f.close()

shutil.copyfile("/data/output/earth.vtp", "/data/shared/earth.vtp")
shutil.copyfile("/data/output/plotly-test.csv", "/data/shared/plotly-test.csv")
shutil.copyfile("/data/shared/params.ini", "/data/shared/params2.ini")
shutil.copyfile("/data/shared/code.json", "/data/shared/code2.json")
