# Make a list to store the first 10 cubes
cubes = []

# Calculate the cube of each integer from 1 through 10 and add it to the list
for number in range(1, 11):
    cubes.append(number ** 3)

# Print out the value of each cube using a for loop
for cube in cubes:
    print(cube)
