#for loop that goes through a short list of movies

films = ['hellraiser', 'it', 'nightmare on elm street', 'c.h.u.d.',\
         'alien', 'nosferatu', 'halloween', 'jaws', 'poltergeist']

intro_line = 'here is a list of fun movies to watch this Halloween season:'

#Example of how to use the capitalize string method
print(intro_line.capitalize())

for movie in films:
    if movie == 'it' or movie == 'c.h.u.d.' or movie == 'e.t.':
        print(movie.upper())
    else:
        print(movie.title())