
import json
from difflib import get_close_matches

data=json.load(open('data.json'))
def translate (g,word):
    n=get_close_matches(word,data)[0]
    #
    # if word in n:
    #     d=print('\n you entered %s but if you mean %s then its meaning is :\n '%g %n)
    #     return data[n]
    # else:
    word=word.lower()
        # return wordjkjkkjcffffd

    if word in data :
       k=print('the meaning of %s is'%g)
       return data[word]

    elif len(get_close_matches(word,data))>0:
         n=get_close_matches(word,data)[0]

         k=input('did you mean %s ? \nEnter "Y" if yes or "N" if NO?:'%n)

         if k in ["Y",'y','YES','yes','yeah','yee']:
            d=print('\nif you mean %s then its meaning is :\n '%n)
            return data[n]

         elif k in ['N','n','no','NO','no']:
              # k=print('fuck you')
              return 'ooh no that was not the meaning '
         else:
              return "print something we understand dude"

    else:
       #l=print('Yoo your crazy Bitch ')
       return "Yoo your crazy my guy please change what you wrote"


g=input("enter the word:")
output=translate(g,g)

if type(output)!=list:
   print(output)

else:
    for item in output:
        print(item,'\n')
