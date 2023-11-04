import pandas as pd
import random
import json

# Load your dataset
df = pd.read_csv('datasets/OrderReport.csv')

# Load JSON data from multiple files
json_data = []
i = ['json_files/johor.json', 'json_files/kedah.json', 'json_files/kelantan.json', 'json_files/labuan.json', 'json_files/melaka.json', 'json_files/negeri_sembilan.json', 'json_files/pahang.json', 'json_files/penang.json', 'json_files/perak.json', 'json_files/perlis.json', 'json_files/putrajaya.json', 'json_files/sabah.json', 'json_files/sarawak.json', 'json_files/selangor.json', 'json_files/terengganu.json', 'json_files/kuala_lumpur.json']

for j in i:
    with open(j) as f:
        json_data.append(json.load(f))

# Initialize random number generator with a fixed seed for consistency
random.seed(42)

# Define the desired distribution of states (adjust proportions as needed)
states_distribution = {
    'Johor': 0.6,
    'Kedah': 0.5,
    'Kelantan': 0.4,
    'Labuan': 0.05,
    'Melaka': 0.7,
    'Negeri Sembilan': 0.5,
    'Pahang': 0.4,
    'Penang': 0.3,
    'Perak': 0.4,
    'Perlis': 0.5,
    'Putrajaya': 0.3,
    'Sabah': 0.05,
    'Sarawak': 0.05,
    'Selangor': 0.8,
    'Terengganu': 0.4,
    'WP Kuala Lumpur': 0.3
}

# Make sure all states are included
states = list(states_distribution.keys())

# Create a list to store the data
data_list = []

# Extract city and postcode from the JSON data and add state
for data in json_data:
    for city_data in data['city']:
        city_data['state'] = data['name']
        data_list.append(city_data)

# in a state, there are multiple cities and postcodes, so use all of them
# to create a dictionary of cities and postcodes and make sure the state is related to the city and the postcode is related to the city

# Sample the same number of states as rows in your existing dataset
existing_rows = len(df)
sampled_states = random.choices(states, weights=states_distribution.values(), k=existing_rows)
# Assign the sampled states to your existing DataFrame
df['State'] = sampled_states

# Save the DataFrame to a CSV file
df.to_csv('datasets/OrderReport.csv', index=False)

# count the number of different states
count = df['State'].value_counts()
print(count)
