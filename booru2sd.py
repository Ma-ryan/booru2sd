import re

def modify_text_file(filepath):
    """
    Reads a text file, adds a comma after each entry,
    replaces underscores with spaces, adds a backslash before each bracket,
    and writes the modified content back.

    Args:
        filepath: The path to the text file.
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        # Split the content into entries
        entries = re.split(r'\s+', content)

        modified_entries = []
        for entry in entries:
            entry = entry.strip()
            entry = entry.replace('_', ' ')

            # Add backslash before each bracket
            entry = entry.replace('(', '\(')
            entry = entry.replace(')', '\)')

            entry += ','
            modified_entries.append(entry)

        modified_content = ' '.join(modified_entries)

        with open(filepath, 'w') as file:
            file.write(modified_content)

        print(f"File '{filepath}' modified successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'tags.txt'  # Replace with your file path
modify_text_file(file_path)