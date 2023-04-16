import subprocess

# Directory path to loop through
cmd1 = ["cat", "files.txt"]
cmd2 = ["gpg", "--verify-files"]

# Run the commands and connect the output of cmd1 to the input of cmd2 using pipes
p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
with open('files.txt', 'r') as file:
    i = 0
    # Loop through each line in the file
    for line in file:
        # Process the line
        print(line.strip())
        filename = line.strip()
        # cmd = ["gpg", "--verify", filename]
        # output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        p1.stdout.close()
        p1.wait()
        p2.wait()
        output_messages_stdout = p2.stdout.read().decode()
        output_messages_stderr = p2.stderr.read().decode()
        output_file = "output.txt"
        with open(output_file, "a") as outfile:
            # Write the text to a new line
            outfile.write(f"{output_messages_stdout}\n")
            outfile.write(f"{output_messages_stderr}\n")
            outfile.write(f"i:{i}")
        i+=1