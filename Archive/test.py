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
    'Johor': 0.1,
    'Kedah': 0.1,
    'Kelantan': 0.1,
    'Labuan': 0.1,
    'Melaka': 0.1,
    'Negeri Sembilan': 0.1,
    'Pahang': 0.1,
    'Penang': 0.1,
    'Perak': 0.1,
    'Perlis': 0.1,
    'Putrajaya': 0.1,
    'Sabah': 0.1,
    'Sarawak': 0.1,
    'Selangor': 0.1,
    'Terengganu': 0.1,
    'WP Kuala Lumpur': 0.1
}

# Add the state followd by the city in the JSON file with the same state
# Make sure all states are included
states = list(states_distribution.keys())

# Create a list to store the data
data_list = []

# Extract city and postcode from the JSON data and add state
for data in json_data:
    for city_data in data['city']:
        city_data['state'] = data['name']
        data_list.append(city_data)

# Sample the same number of states as rows in your existing dataset
existing_rows = len(df)
sampled_states = random.choices(states, weights=states_distribution.values(), k=existing_rows)
# Assign the sampled states to your existing DataFrame
df['State'] = sampled_states

# Sample the same number of cities as rows in your existing dataset
sampled_cities = random.choices(data_list, k=existing_rows)

# Assign the sampled cities to your existing DataFrame based on the state
state = df['State']
df['City'] = [random.choice([i['name'] for i in sampled_cities if i['state'] == j]) for j in state]

# Sample the same number of postcodes as rows in your existing dataset
sampled_postcodes = random.choices(data_list, k=existing_rows)

# Assign the sampled postcodes to your existing DataFrame based on the city
city = df['City']
df['Postcode'] = [random.choice([i['postcode'] for i in sampled_postcodes if i['name'] == j]) for j in city]

# Save the DataFrame to a CSV file
df.to_csv('datasets/OrderReport_Updated.csv', index=False)

