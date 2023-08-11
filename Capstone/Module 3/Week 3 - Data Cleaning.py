from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

HEADERS ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

movie_data = []


genre = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Film-Noir", "History", "Horror", "Music", "Musical", "Mystery"
         "Romance", "Sci-Fi", "Short", "Sport", "Thriller", "War", "Western"]

for x in genre:
    url = "https://www.imdb.com/search/title/?genres={}&explore=genres&title_type=feature&ref_=ft_movie_0"
    formated_url = url.format(x)
    



# Sending a request to the speciifed URL
    resp = requests.get(formated_url, headers=HEADERS)

# Converting the response to Beautiful Soup Object
    content = BeautifulSoup(resp.content, 'lxml')

# Iterating throught the list of movies 
    for movie in content.select('.lister-item-content'):
        
        try:
        # Creating a python dictonary
            data = {
            
                "title":movie.select('.lister-item-header')[0].get_text().strip(),
                "year":movie.select('.lister-item-year')[0].get_text().strip(),
                "certificate":movie.select('.certificate')[0].get_text().strip(),
                "time":movie.select('.runtime')[0].get_text().strip(),
                "genre":movie.select('.genre')[0].get_text().strip(),
                "rating":movie.select('.ratings-imdb-rating')[0].get_text().strip(),
                "metascore":movie.select('.ratings-metascore')[0].get_text().strip(),
                "simple_desc":movie.select('.text-muted')[2].get_text().strip(),
                "votes":movie.select('.sort-num_votes-visible')[0].get_text().strip()


            
                
                    }
        except IndexError:
            continue

        movie_data.append(data)

        with open(r'C:\Users\User\Desktop\Capstone\Module 3\ Module3.csv', 'w') as csv_file:
            
            for y in movie_data:
                    
                
                writer = csv.DictWriter(csv_file, fieldnames=y.keys())
                
                writer.writerow(y)



 
        
    
    

print(movie_data)
    


    