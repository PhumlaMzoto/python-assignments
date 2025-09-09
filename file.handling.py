def simple_file_processor():
    """A simpler version of the file processor."""
    
    try:
        # Get filename from user
        filename = input("Enter filename to read: ").strip()
        
        # Read file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify content (simple example)
        modified_content = content.upper()
        
        # Write to new file
        output_filename = filename.replace('.', '_modified.')
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Success! Modified file saved as: {output_filename}")
        
    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

# Run the simple version
simple_file_processor()