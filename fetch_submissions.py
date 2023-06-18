import subprocess

# Install matplotlib using pip
subprocess.check_call(['pip', 'install', 'matplotlib'])

import os
import json
import requests
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Retrieve LeetCode submissions
response = requests.get('https://leetcode.com/api/user_submission_calendar/vijaymanikantareddy/')
data = response.json()

# Extract submission data
submissions = data['submissions']
dates = [submission['date'] for submission in submissions]
counts = [submission['count'] for submission in submissions]

# Convert dates to matplotlib format
formatted_dates = [date[:4] + '-' + date[4:6] + '-' + date[6:] for date in dates]
formatted_dates = [plt.datetime.strptime(date, "%Y-%m-%d").date() for date in formatted_dates]

# Generate the graph
fig, ax = plt.subplots()
ax.plot(formatted_dates, counts, color='blue')
ax.xaxis.set_major_formatter(DateFormatter("%b '%y"))
ax.set_xlabel('Date')
ax.set_ylabel('Submissions')
ax.set_title('LeetCode Submissions')

# Save the graph as SVG
plt.savefig('leetcode_graph.svg')
