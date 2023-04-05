import pandas as pd

# create a dataframe
df = pd.DataFrame({
    "Player" : ["Ram", "Hari", "Shyam", "Gita", "Rita", "Sita"],
    "Medal" : ["Gold", "Silver", "Bronze", "Silver", "Bronze", "Gold"],
    "Gender": ["Male", "Male", "Male", "Female", "Female", "Female", ]
})
print(df)


# perform one hot encoding
# Method 1
encoded_df_1 = pd.get_dummies(df['Medal'])
print(encoded_df_1)

# Method 2
encoded_df_2 = pd.get_dummies(df['Medal'], prefix="Medal")
print(encoded_df_2)

# Method 3
encoded_df_3 = pd.get_dummies(df['Medal'], prefix="Medal", dtype=bool)
print(encoded_df_3)


# Concatenate original df with one hot encoded df
# concated_encoded_df = pd.concat([df, pd.get_dummies(df['Medal'])])
concated_encoded_df = pd.concat([df, encoded_df_2], axis=1)         # without axis gives NaN
print(concated_encoded_df)


# Drop the original column "Medal"
encoded_df = concated_encoded_df.drop("Medal", axis=1)
print(encoded_df)
