'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''
import pandas as pd
import os
os.chdir('C:\\Users\\Alexander\\Documents\\DAT7\\data')

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
data = pd.read_csv('imdb_1000.csv')

# check the number of rows and columns
data.shape
# check the data type of each column
data.dtypes
# calculate the average movie duration
data.duration.mean() #average duration: 120.98 minutes
# sort the DataFrame by duration to find the shortest and longest movies
data.sort('duration', inplace = True)
data.head(1) #Freaks is the shortest
data.tail(1) #Hamlet is the longest
# create a histogram of duration, choosing an "appropriate" number of bins
data.duration.plot(kind = 'hist', bins = 15)
# use a box plot to display that same data
data.boxplot(column = 'duration')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
data.content_rating.value_counts()
# use a visualization to display that same data, including a title and x and y labels
data.content_rating.value_counts().plot(kind='bar')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
data.content_rating.replace('NOT RATED', 'UNRATED', inplace=True)
data.content_rating.replace('APPROVED', 'UNRATED', inplace=True)
data.content_rating.replace('PASSED', 'UNRATED', inplace=True)
data.content_rating.replace('GP', 'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
data.content_rating.replace('X', 'NC-17', inplace=True)
data.content_rating.replace('TV-MA', 'NC-17', inplace=True)

# count the number of missing values in each column
data.isnull().sum()
# if there are missing values: examine them, then fill them in with "reasonable" values
data[data.content_rating.isnull()]
data.loc[187, 'content_rating'] = 'PG'
data.loc[649, 'content_rating'] = 'PG'
data.loc[936, 'content_rating'] = 'G'

# calculate the average star rating for movies 2 hours or longer,
data[data.duration >= 120].star_rating.mean() #7.95
# and compare that with the average star rating for movies shorter than 2 hours
data[data.duration < 120].star_rating.mean() #7.84
# use a visualization to detect whether there is a relationship between star rating and duration
data.plot(kind='scatter', x='duration', y='star_rating')
# calculate the average duration for each genre
data.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
data.plot(kind='scatter', x='duration', y='star_rating')
# determine the top rated movie (by star rating) for each genre
data.sort(['genre','star_rating'], ascending = False).groupby('genre').head(1)
# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
data[data.title.duplicated()]
data[data.duplicated()]
# calculate the average star rating for each genre, but only include genres with at least 10 movies
data_genre_rating = data.groupby('genre').star_rating
data_genre_rating.agg(['count', 'mean'])[data_genre_rating.count() >= 10 ]
'''
BONUS
'''

# Figure out something "interesting" using the actors data!
