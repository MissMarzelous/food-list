# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Food List — Create, Sort, and Display
# DATE WRITTEN: 10/28/2020
#
# PURPOSE: Create a list of food items entered by the user, then display
#          the list in unsorted, ascending sorted, and descending sorted
#          order. All output is written to a user-specified external text file.
#
# VARIABLES (alphabetical):
#   count      - for loop control variable / index
#   fileName   - name of the output text file
#   foodList   - list of food item names (string)
#   item       - individual food item used during display loop
#   numItems   - number of food items to add to the list
#   outFile    - file object used for writing output

# Create an external file to write output from this program
fileName = input("Enter the name of the output file where you wish to write the results\n"
                 "(add the \".txt\" extension to your file name)\n").strip()
outFile = open(fileName, "w")

# Validate and input the number of food items to enter
print("How many items do you wish to enter into your food list?\n"
      "Enter a positive whole numerical value:")

while True:
    try:
        numItems = int(input())
    except ValueError:
        print("WRONG DATA TYPE ENTERED - enter a positive whole number greater than 0.\n")
        continue
    else:
        if numItems <= 0:
            print("Value must be greater than zero - please re-enter.\n")
            continue
        else:
            break
    # end while True loop

# Define the food list with the specified number of slots
foodList = [""] * numItems

# FOR LOOP to populate the food list with user-entered items
for count in range(0, numItems):
    # Validate that the entry is not blank
    while True:
        print("Enter the name of item #" + format(count + 1, "2d") + ":")
        item = input().strip()
        if item == "":
            print("Item name cannot be blank - please re-enter.")
            continue
        foodList[count] = item
        break
    # end for loop

# Write the unsorted food list to the output file
outFile.write("=" * 50 + "\n")
outFile.write(f'{"UNSORTED FOOD LIST":^50s}\n')
outFile.write("=" * 50 + "\n")
for item in foodList:
    outFile.write(f'{item:^50s}\n')
    # end for loop
outFile.write("=" * 50 + "\n\n")

# Sort the list in ascending (A-Z) order
foodList.sort()

# Write the ascending sorted food list to the output file
outFile.write("=" * 50 + "\n")
outFile.write(f'{"SORTED FOOD LIST (ASCENDING A-Z)":^50s}\n')
outFile.write("=" * 50 + "\n")
for item in foodList:
    outFile.write(f'{item:^50s}\n')
    # end for loop
outFile.write("=" * 50 + "\n\n")

# Sort the list in descending (Z-A) order
foodList.sort(reverse=True)

# Write the descending sorted food list to the output file
outFile.write("=" * 50 + "\n")
outFile.write(f'{"SORTED FOOD LIST (DESCENDING Z-A)":^50s}\n')
outFile.write("=" * 50 + "\n")
for item in foodList:
    outFile.write(f'{item:^50s}\n')
    # end for loop
outFile.write("=" * 50 + "\n")

# Close the external output file
outFile.close()
print("Results written to: " + fileName)

# END PROGRAM
