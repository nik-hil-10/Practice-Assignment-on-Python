import os
import sys
import shutil
from datetime import datetime


def main():
    if len(sys.argv) != 3:
        print("Usage: python q4.py <source_directory> <destination_directory>")
        return
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    
    backup_files(source_dir, destination_dir)

def backup_files(source_dir,destination_dir):
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    if not os.path.isdir(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it.")
        os.makedirs(destination_dir)
    
    
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)

        
        if os.path.isfile(source_file):
            dest_file = os.path.join(destination_dir, file_name)

            
            if os.path.exists(dest_file):
                base, ext = os.path.splitext(file_name)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{base}_{timestamp}{ext}"
                dest_file = os.path.join(destination_dir, file_name)

            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {file_name}")
            except Exception as e:
                print(f"Error copying {file_name}: {e}")
        
        
    
if __name__ == "__main__":
    main()