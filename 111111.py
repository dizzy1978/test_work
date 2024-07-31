



with open(r"film_data\temp\film_data_temp.txt", "r") as file:
    for string in file:
        data = string.split(';')

saved_title = data[0].strip().strip(")")
saved_rating = data[1].strip()
saved_year = data[2].strip()

print(saved_title)
print(saved_rating)
print(saved_year)



