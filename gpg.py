import subprocess

# Directory path to loop through
with open('files.txt', 'r') as file:
    i = 0
    # Loop through each line in the file
    for line in file:
        # Process the line
        print(line.strip())
        filename = line.strip()
        # cmd = ["gpg", "--verify", filename]
        # output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        cmd1 = ["cat", "files.txt"]
        cmd2 = ["gpg", "--verify-files"]

        # Run the commands and connect the output of cmd1 to the input of cmd2 using pipes
        p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p2.communicate()
        # Decode the output and error messages from bytes to string
        output = output.decode()
        print(output)
        output_file = "output.txt"
        with open(output_file, "a") as outfile:
            # Write the text to a new line
            outfile.write(f"{output}\n")
            outfile.write(f"i:{i}")
        i+=1