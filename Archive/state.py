import pandas as pd
import random
import json

# Load your dataset
df = pd.read_csv('datasets/OrderReport_archive.csv')

# Malaysian States
states = ['Johor', 'Kedah', 'Kelantan', 'Labuan', 'Melaka', 'Negeri Sembilan', 'Pahang', 'Penang', 'Perak', 'Perlis', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu', 'WP Kuala Lumpur']

# states distribution
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
    'Putrajaya': 0.2,
    'Sabah': 0.03,
    'Sarawak': 0.03,
    'Selangor': 0.8,
    'Terengganu': 0.4,
    'WP Kuala Lumpur': 0.3
}

# Initialize random number generator with a fixed seed for consistency
random.seed(42)

# Sample the same number of states as rows in your existing dataset
existing_rows = len(df)
sampled_states = random.choices(states, weights=states_distribution.values(), k=existing_rows)
# Assign the sampled states to your existing DataFrame
df['State'] = sampled_states

# Save the DataFrame to a CSV file
df.to_csv('datasets/OrderReport_archive.csv', index=False)