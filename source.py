filename1 = input ("enter Source file name ") # Open the source file in read mode
with open(filename1, 'r') as file1:   # Read all lines from the source file
      lines = file1.readlines()
filename2 = input ("enter destination file name ") # Open the destination file in write mode
with open(filename2, 'w') as file2: 
     for i in range(len(lines)):   # Iterate through the lines
         if i % 2 == 0:   # Copy only odd lines 
              file2.write(lines[i])
print("Odd lines copied to 'filename2'.")

with open(filename2, 'r') as file2:
    lines=file2.readlines()
    print (lines)
