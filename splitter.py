import os
import sys

def split_file(input_file, mb_size):
    # Ensure the input file exists
    chunk_size=int(mb_size) * 1024 * 1024
    if not os.path.isfile(input_file):
        print(f"File {input_file} does not exist.")
        return
    
    # Get the file size
    file_size = os.path.getsize(input_file)
    
    # Calculate the number of chunks needed
    num_chunks = (file_size // chunk_size) + (1 if file_size % chunk_size != 0 else 0)
    
    with open(input_file, 'rb') as f:
        for i in range(num_chunks):
            # Read a chunk of the file
            chunk_data = f.read(chunk_size)
            
            # Define the chunk file name
            chunk_file_name = f"{input_file}_part_{i + 1}"
            
            print(f"Creating {chunk_file_name}")
            # Write the chunk to a new file
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            
            print(f"Created {chunk_file_name}")


input_f = sys.argv[1] if len(sys.argv) > 1 else None
mb_size = sys.argv[2] if len(sys.argv) > 2 else None

if input_f is None or mb_size is None:
    
    if sys.argv[1] == "help":
        print(f"splitter - splits file to chunks.\n\nHow to use: splitter.py inputFile ChunkSizeInMB.\nMade by alexmiles")
    else:
        print("Missing or unknows arguments. Use 'splitter.py help' for help.")
    # Lil bro got error
else:
    split_file(str(sys.argv[1]), mb_size)
   
#input_file = str(input("Enter path to file: "))
#split_file(input_file)







# 52!!! 
