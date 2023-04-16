import subprocess

# Directory path to loop through
with open('files.txt', 'r') as file:
    i = 0
    # Loop through each line in the file
    for line in file:
        # Process the line
        print(line.strip())
        filename = "files.txt"
        # Define the command with pipes
        cmd1 = ["cat", "files.txt"]
        cmd2 = ["gpg", "--verify-files"]

        # Run the commands and connect the output of cmd1 to the input of cmd2 using pipes
        p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Pass an empty input
        # p1.stdout.close()
        p1.communicate()
        # p1.wait()
        p2.wait()

        # Get the exit code of the gpg command
        exit_code = p2.returncode

        # Get the output messages from stdout and stderr
        output_messages_stdout = p2.stdout.read().decode()
        output_messages_stderr = p2.stderr.read().decode()

        output_file = "output.txt"
        with open(output_file, "a") as outfile:
            # Write the text to a new line
            outfile.write(f"File: {filename}\n")
            outfile.write(f"Exit code: {exit_code}\n")
            outfile.write(f"Stdout messages:\n{output_messages_stdout}\n")
            outfile.write(f"Stderr messages:\n{output_messages_stderr}\n")
            outfile.write(f"i: {i}\n")
            outfile.write("\n")
        i += 1
