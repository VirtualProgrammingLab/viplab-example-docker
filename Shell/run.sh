#!/bin/bash
source <(grep = $1 | tr -d ' ')
echo "Your name is $name"
echo "Your current age: $age"
echo "Your Christmas Wish is: $christmasWish"
echo "How hot do you like to drink your coffee? $coffeeTemperature"
echo "You like: $likedThings"
echo "Your favorite Programming Language is $favoritePL"
echo "You look in the fridge: $fridge"
echo "You would dance in the kitchen to: $dancing"
echo "You dislike: $dislikedThings"
echo "Your three random numers are: $randomNumbers"
echo "The Code you entered:" 
echo `echo $codeSnippet | base64 -i --decode`
cp /data/output/earth.vtp /data/shared/earth.vtp
cp /data/output/plotly-test.csv /data/shared/plotly-test.csv
cp $1 /data/shared/params2.ini
echo "This is the End of Stdout"
exit 0;