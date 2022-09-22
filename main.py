import requests
import json
import sys

args = sys.argv
repo = args[1]
branch = args[2]
token = args[3]

headers = {
    'api-token': token
}

response = requests.request(method = "GET", url = f'https://app.codacy.com/api/v3/analysis/organizations/gh/BY-Product-Development/repositories/{repo}?branch={branch}', headers = headers)
#print(response.status_code)
response = response.json()['data']
grade = response['grade']
grade_letter = response['gradeLetter']
issues_percentage = response['issuesPercentage']
complex_files_percentage = response['complexFilesPercentage']
duplication_percentage = response['duplicationPercentage']

print("Results:")
print(f"Grade: {grade}")
print(f"Grade Letter: {grade_letter}")
print(f"Issues Percentage: {issues_percentage}")
print(f"Complex Files Percentage: {complex_files_percentage}")
print(f"Duplication Percentage: {duplication_percentage}")