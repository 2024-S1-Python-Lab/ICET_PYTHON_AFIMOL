filename = input ("enter file name ")
try:
    with open(filename, 'r') as file1:
        
        
        lines = file1.readlines()
        lines = [line.strip() for line in lines] # Remove newline characters from each line
        print("Lines from the file:", lines)
   
except FileNotFoundError:
    
    print(f"Error: The file '{filename}' does not exist.")
""" output
enter file name sample
Error: The file 'sample' does not exist.
enter file name sample.txt
Lines from the file: ['Sheena K M', 'Assistant Professor', 'Department of MCA', 'ICET', 'Muvattupuzha']
"""
