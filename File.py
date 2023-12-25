import os
import shutil
import datetime

def copy_files_by_date(source, destination, start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    for root, directories, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = os.path.getmtime(file_path)
            modification_date = datetime.datetime.fromtimestamp(modification_time)

            if start_date <= modification_date <= end_date:
                dest_file_path = os.path.join(destination, os.path.relpath(file_path, source))
                dest_dir = os.path.dirname(dest_file_path)

                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                shutil.copy2(file_path, dest_file_path)
                print("Copied", file_path, "to", dest_file_path)

# Example usage:
source_dir = input("Enter source directory: ")
destination_dir = input("Enter destination directory: ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

copy_files_by_date(source_dir, destination_dir, start_date, end_date)
