# https://en.wikipedia.org/wiki/One-hot#Natural_language_processing
# Categorial data -> Nominal, Ordinal

# in this case
# Catergoies
#   # Nominal
#       - Gold
#       - Silver
#       - Bronze

import pandas as pd

# create a sample dataframe with medal data
medals = pd.DataFrame({
    'Athlete': ['John', 'Mary', 'Bob', 'Sarah', 'Tom'],
    'Medal': ['Gold', 'Silver', 'Bronze', 'Silver', 'Gold']
})
print(medals)

# perform one hot encoding
one_hot_encoded = pd.get_dummies(medals['Medal'], prefix='Medal')
print(one_hot_encoded)

# combine the original dataframe with the one hot encoded dataframe
medals_encoded = pd.concat([medals, one_hot_encoded], axis=1)
print(medals_encoded)

# drop the original categorical column
medals_encoded = medals_encoded.drop('Medal', axis=1)

print(medals_encoded)
