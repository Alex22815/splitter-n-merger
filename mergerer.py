import os
import sys

def merge_files(output_file, input_files):
    with open(output_file, 'wb') as outfile:
        for chunk_file in input_files:
            if not os.path.isfile(chunk_file):
                print(f"File {chunk_file} does not exist.")
                return
            
            with open(chunk_file, 'rb') as infile:
                outfile.write(infile.read())
                
            print(f"Merged {chunk_file} into {output_file}")





output_f = sys.argv[1] if len(sys.argv) > 1 else None
input_f = sys.argv[2] if len(sys.argv) > 2 else None
chunks = sys.argv[3] if len(sys.argv) > 3 else None




if output_f is None or input_f is None or chunks is None:
    if sys.argv[1] == "help":
        print(f"merge - merges chunks made by splitter into one file.\n\nHow to use: merge outputFile inputFile chunks.\nMade by alexmiles")
    else:
        print("Missing arguments. Use 'merge.py help'for help.")
    # Handle the missing arguments here, such as printing an error message or exiting the script.
    # You can also return or raise an exception if necessary.
else:
    print(f"INFO: output file = {output_f}, input file = {input_f}, chunks = {chunks}")
    input_files = [f"{input_f}_part_{i+1}" for i in range(int(chunks))]
    merge_files(output_f, input_files)

#output_f = str(input("Enter output file with extention: "))
# input_f = str(input("Enter splitted file name (with original extention): "))
#chunks = int(input("Enter count of chunks: "))

#input_files = [f"{input_f}_part_{i+1}" for i in range(chunks)]  # Replace with the correct number of chunks and file naming pattern
#merge_files(output_f, input_files)
