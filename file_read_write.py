# file_read_write.py

def read_and_write():
    try:
        # Open original file for reading
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify the content (example: make uppercase)
        modified = content.upper()

        # Write to new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified)

        print("File successfully modified and saved as 'output.txt'.")

    except FileNotFoundError:
        print(" 'input.txt' not found. Please create the file first.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Run function
read_and_write()
