import pandas as pd
import re


pd.options.display.max_colwidth = 1000

unwanted = '()'
numbers = r'[0-9]'

genres = ['western', 'thriller', 'horror', 'sci-fi', 'mystery', 'film-noir', 'romance', 'musical', 'music', 'drama', 'war', 'sport', 
          'history', 'crime', 'comedy', 'fantasy', 'biography', 'family', 'animation', 'adventure', 'action']

df = pd.read_csv("C:/Users/User/Desktop/Capstone/Module 6/module3.csv", encoding='utf8')

df['New Rating'] = df['IMDB User Rating'] * 10 + df['Metascore Rating']



while True:
    favorite_genre = input('What genre movie do you enjoy watching?').title()
    if favorite_genre.lower() not in genres:
        print("I am sorry but we do not have a movie of that genre. Please choose another.")
        continue
    else:
        break

while True:
    try:    
        age = int(input('How old is the youngest person that will be watching a movie with you?'))
    except ValueError:
        print("I am sorry but that is not a valid response. Please enter a whole number for the age.")
        continue
    else:
        break

if age < 17:    
    while True:        
    
        parent_present = input('Will the child\'s parent or guardian be present during the film?').lower()
        if parent_present not in ['yes', 'no']:
            print('I am sorry but you must enter "yes" or "no" as a valid response.')
            continue
        else:
            break


                               
if age < 13 and parent_present == 'no':
    df2 = df.append(df.loc[df['Rating'] == 'G'])
elif (age < 13 and parent_present == 'yes') or (age < 17 and age > 13 and parent_present == 'no'):
    df2 = df.append(df.loc[df['Rating'] == 'G'])
    df2.append(df.loc[df['Rating'] == 'PG'])
    df2.append(df.loc[df['Rating'] == 'PG-13'])
elif age < 17 and age > 13 and parent_present == 'yes':
    df2 = df.append(df.loc[df['Rating'] == 'G'])
    df2.append(df.loc[df['Rating'] == 'PG'])
    df2.append(df.loc[df['Rating'] == 'PG-13'])
    df2.append(df.loc[df['Rating'] == 'R'])
else:
    df2 = df.append(df)


df3 = df2[df2['Genres'].str.contains(favorite_genre)]


df4 = df3.loc[df3['New Rating'].idxmax()]



result = df4['Movie Title']
result_summary = df4['Description']


result = re.sub(unwanted, '', str(result))
result = re.sub(numbers, '', str(result))





print('Based on your genre preference and the audience, this is your movie recommendation ' + result + ' Here is a brief summary: ' + result_summary)



  