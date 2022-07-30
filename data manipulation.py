#Data Manipulation
##Creating, Reading and Writing

#1
fruits = pd.DataFrame({'Apples':[30],'Bananas':[21]})

#2
fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])

#3
ingredients = pd.Series(['4 cups','1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'],name='Dinner')

#4
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv",index_col=0)

#5
animals.to_csv('cows_and_goats.csv')

##Indexing, Selecting & Assigning

#1
desc = reviews.description

#2
first_description = desc = reviews.description[0]

#3
first_row = reviews.iloc[0]

#4
first_descriptions = reviews.loc[:9,'description']

#5
sample_reviews = reviews.iloc[[1,2,3,5,8]]

#6
df = reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]

#7
df = reviews.loc[:99,['country','variety']]

#8
italian_wines = reviews.loc[reviews.country == 'Italy']

#9
top_oceania_wines = reviews.loc[(reviews.points>=95) & (reviews.country.isin(['Australia','New Zealand']))]

##Summary Functions and Maps

#1
median_points = reviews.points.median()

#2
countries = reviews.country.unique()

#3
reviews_per_country = reviews.country.value_counts()

#4
centered_price = reviews.price - reviews.price.mean()

#5
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#6
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

#7
def star(row):
    if row.points<85:
        return 1
    elif row.points<95:
        return 2
    return 3

star_ratings = reviews.apply(star,axis="columns")

##Grouping and Sorting

#1
reviews_written=reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

#2
best_rating_per_price = reviews.groupby('price').points.max().sort_index()

#3
price_extremes = reviews.groupby(['variety']).price.agg(['min','max'])

#4
sorted_varieties = price_extremes = reviews.groupby(['variety']).price.agg(['min','max']).sort_values(by=['min','max'],ascending=False)

#5
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

#6
country_variety_counts=reviews.groupby(['country','variety']).variety.count().sort_values(ascending=False)

##Data Types and Missing Values

#1
dtype = reviews.points.dtype

#2
point_strings = reviews.points.astype('str')

#3
n_missing_prices = reviews.price.isnull().sum()

#4
reviews_per_region=reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

##Renaming and Combining

#1
renamed = reviews.rename(columns={'region_1':'region','region_2':'locale'})

#2
reindexed = reviews.rename_axis('wines',axis='index')

#3
combined_products = pd.concat([gaming_products,movie_products])

#4
powerlifting_combined=powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))