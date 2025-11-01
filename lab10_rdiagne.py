#Name:Rokhaya Diagne 
#Date: 10/31/2025
#This program reads a text file specified by the user, counts the
#frequency of each word (case-insensitively and ignoring punctuation),
# and prints the results alphabetically. It also handles file not found errors.

def printWds(data):
    # print each word in our data and the respective count, sorted by word
    for x in sorted(data.keys()):
        # Use data[x] to get the count
        print(f'{x} :: {data[x]}') 
    return

def wordFreq(fptr):
    # Use a dictionary to store frequencies
    freq = {}
    
    # Define punctuation characters
    punctChars = (',', '.', ';', ':', '!', '?','"', "'", '(', ')', '[', ']', '{', '}', '-', '–', '—', '/', '\\', '&', '@', '#', '$', '%', '^', '*', '+', '=')
    
    # Read the first line
    line = fptr.readline()

    while line:
        # Remove punctuation
        for c in punctChars:
            line = line.replace(c, "")
            
        # Create a list of separate words
        words = line.split()
        
        for word in words:
            # Convert to lower case
            tmp = word.lower()
            
            # Update the count in the freq dictionary (using get() is correct here)
            freq[tmp] = freq.get(tmp, 0) + 1
        
        # IMPORTANT: Read the next line to prevent an infinite loop
        line = fptr.readline()
        
    # Return the dictionary of word frequencies
    return freq

def main():
    file_name = input("Give me the filename:\n")
    fptr = None # Initialize fptr outside of try block
    try:
        fptr = open(file_name,"r")
        
        # 1. Get the word frequencies
        word_data = wordFreq(fptr)
        
        # 2. Print the results
        printWds(word_data)
        
    except FileNotFoundError as e:
        # Corrected print statement syntax
        print(f"Exception thrown: {e}") 
        
    finally:
        # Close the file if it was successfully opened
        if fptr:
            fptr.close()
    
    return

if __name__=="__main__":
    main()
