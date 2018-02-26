# Convert miles to kilometers
# km = miles * 1.60934
# eg: enter miles 5
# 5 miles equals 8.04 kilometers

# Receive user input of miles
miles = input('Enter Miles ')

# Convert miles to int then to KM by the factor given
miles = int(miles)
km = miles * 1.60934

# Print results
print('{} miles equals {} kilometers'.format(miles, km))