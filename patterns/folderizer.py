import os

def describe_folder_structure(base_folder, output_file):
    """
    Describe the folder structure, including subfolders and file contents,
    and save the description to a text file.

    Args:
        base_folder (str): The path of the folder to be described.
        output_file (str): The path to save the output description.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as out:
            # Write a header to the output file
            out.write(f"Folder Structure for '{base_folder}'\n")
            out.write("=" * 50 + "\n\n")
            
            # Walk through the directory tree
            for root, dirs, files in os.walk(base_folder):
                # Write the current folder path
                out.write(f"Current Folder: {root}\n")
                out.write("-" * 50 + "\n")
                
                # Write the list of subfolders
                if dirs:
                    out.write("Subfolders:\n")
                    for subfolder in dirs:
                        out.write(f"  - {subfolder}\n")
                else:
                    out.write("Subfolders: None\n")
                
                # Write the list of files
                if files:
                    out.write("\nFiles:\n")
                    for file in files:
                        file_path = os.path.join(root, file)
                        out.write(f"  - {file}\n")
                        
                        # Attempt to read the file contents
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                out.write(f"\n    Contents of {file}:\n")
                                out.write(f"    {'-' * 40}\n")
                                out.write(content + "\n")
                                out.write(f"    {'-' * 40}\n")
                        except Exception as e:
                            # Handle cases where the file cannot be read
                            out.write(f"    [ERROR] Could not read {file}: {str(e)}\n")
                else:
                    out.write("\nFiles: None\n")
                
                # Add spacing between folders
                out.write("\n" + "=" * 50 + "\n\n")
        
        print(f"Folder structure and contents saved to {output_file}")
    except Exception as e:
        print(f"[ERROR] An error occurred while writing to the output file: {str(e)}")


# Specify the folder to scan and the output file
base_folder = input("Enter the folder path to analyze: ")
output_file = "folder_structure_description.txt"

# Run the function
describe_folder_structure(base_folder, output_file)
