def modify_content(content):
    """
    Modify the content of the file. In this example, we convert the text to uppercase.
    """
    return content.upper()

def read_and_write_file():
    try:
        # Prompt the user for a filename to read
        input_filename = input("Enter the filename to read from (e.g., 'file.txt'): ").strip()

        # Attempt to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Prompt for the output filename
        output_filename = input("Enter the filename to write the modified content to: ").strip()
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{input_filename}' or writing to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
