import os
import json
import requests

# Retrieve LeetCode submissions
response = requests.get('https://leetcode.com/api/user_submission_calendar/vijaymanikantareddy/')
data = response.json()

# Generate graph
submissions = data['submissions']
graph_data = [0] * 366  # Initialize the graph with 366 days

for submission in submissions:
    date = submission['date']
    count = submission['count']
    graph_data[date] = count

# Save graph data to a file
with open('leetcode_graph_data.json', 'w') as file:
    json.dump(graph_data, file)
