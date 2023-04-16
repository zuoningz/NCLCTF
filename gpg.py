import subprocess

# Directory path to loop through
with open('file.txt', 'r') as file:
    i = 0
    # Loop through each line in the file
    for line in file:
        # Process the line
        print(line.strip())
        filename = line.strip()
        cmd = ["gpg", "--verify", filename]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        output_file = "output.txt"
        with open(output_file, "a") as outfile:
            # Write the text to a new line
            outfile.write(f"{output}\n")
            outfile.write(f"i:{i}")
        i+=1