#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.
import csv



# Sample dictionary
data = {
    'Name': ['Midhun', 'Rasim', 'Mariyam'],
    'Age': [21, 23, 22],
    'City': ['Thrissur', 'Kannur', 'Aroor']
}

# Writing dictionary to CSV
with open('output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()
    for i in range(len(next(iter(data.values())))):
        row = {field: data[field][i] for field in data}
        writer.writerow(row)

print("Dictionary written to CSV file 'output.csv'.")

# Reading CSV file and displaying contents
with open('output.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

