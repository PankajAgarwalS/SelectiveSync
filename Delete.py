import os

def find_files_to_delete(source, destination):
    source_files = set(os.listdir(source))
    destination_files = set(os.listdir(destination))

    files_to_delete = destination_files - source_files
    return files_to_delete

def delete_files(destination, files_to_delete):
    for file in files_to_delete:
        file_path = os.path.join(destination, file)
        user_response = input(f"Do you want to delete '{file_path}'? (yes/no): ").lower()

        if user_response == 'yes':
            os.remove(file_path)
            print("Deleted", file_path)
        else:
            print("Skipped deleting", file_path)

# Example usage:
source_dir = input("Enter source directory: ")
destination_dir = input("Enter destination directory: ")

files_to_delete = find_files_to_delete(source_dir, destination_dir)

if not files_to_delete:
    print("No files to delete. Destination folder is in sync with the source folder.")
else:
    print("Files found in destination but not in source:")
    for file in files_to_delete:
        print(file)

    user_confirmation = input("Do you want to proceed with deleting these files? (yes/no): ").lower()

    if user_confirmation == 'yes':
        delete_files(destination_dir, files_to_delete)
    else:
        print("Operation aborted.")
