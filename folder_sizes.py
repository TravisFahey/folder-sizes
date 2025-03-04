import os
import argparse

def get_folder_size(folder_path):
    """
    Calculate the total size of all files within a folder including subfolders
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            try:
                total_size += os.path.getsize(file_path)
            except (FileNotFoundError, PermissionError):
                continue
    return total_size

def list_folders_by_size(base_path):
    """
    List all folders in the base path sorted by their size largest to smallest
    """
    if not os.path.exists(base_path):
        print(f"The path {base_path} does not exist.")
        return
    
    folder_sizes = []
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            folder_size = get_folder_size(folder_path)
            folder_sizes.append((folder_name, folder_size))

    # Sort folders by size
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    # Print results
    print("Folder sizes (largest to smallest):")
    for folder_name, size in folder_sizes:
        print(f"{folder_name}: {size / (1024 * 1024):.2f} MB")

def main():
    parser = argparse.ArgumentParser(description="List folders in a directory sorted by size.")
    parser.add_argument("folder", type=str, help="Path to the folder to scan")
    args = parser.parse_args()
    list_folders_by_size(args.folder)

if __name__ == "__main__":
    main()
