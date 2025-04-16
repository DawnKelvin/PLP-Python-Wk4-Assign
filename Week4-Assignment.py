try:
        # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")
        
        # Open and read the file
    with open(input_file, 'r') as file:
         content = file.read()
    print(content)
        # Modify the content (example: add a new line)
    modified_content = content + "\n"
        
        # Write the modified content to a new file
    output_file = "modified_" + input_file
    with open(output_file, 'w') as file:
        file.write(modified_content)
        
    print(f"Modified content written to {output_file}")
    
except FileNotFoundError:
        print("Error: The file does not exist.")
except Exception:
        print("An unexpected error occurred")
except IOError:
        print("Error: The file could not be read or written.")
finally:
      file.close()
