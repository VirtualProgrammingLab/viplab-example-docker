# viplab-example-docker

Small Docker container, that outputs some information, to show the functionality of ViPLab. 

To execute the container, first build it:

```
docker build -t viplab-example-image .
```

Then run the following command to execute the container:

```
docker run -v ${PWD}/shared:/data/shared -it viplab-example-image
```

Note: If you are on Windows, please use Powershell to run the Container.

After this, the following output should be printed to the console, if you have not adjusted the params.ini file inside the shared folder:
```
Your name is Kathryn
Your current age: 36
Your Christmas Wish is: COFFEE! In that nebula!
How hot do you like to drink your coffee? 75
You like: programming,music,books
Your favorite Programming Language is Java
You look in the fridge: never
You would dance in the kitchen to: Last Christmas
You dislike: Spiders
Your three random numers are: 25,50,75
The Code you entered:
int main(int argc, char **argv) { // Print 'Hello World' }
```