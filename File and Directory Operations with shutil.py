#Name: Jose Alcala
#Date: 9/23/2025
#Class: CIS 188 

#Description: A script to perform file and directory operations using shutil

import shutil
import os

OPT_COPY_FILE = 1
OPT_COPY_DIRECTORY = 2
OPT_MOVE_FILE_OR_DIRECTORY = 3
OPT_DISK_USAGE = 4
OPT_QUIT = 5

def copy_file():
    """Copies source file to destination."""
    while True:
        src = input("Enter source file path: ")
        dst = input("Enter destination file path: ")
        try:
            shutil.copy(src, dst)
            print(f"File copied from '{src}' to '{dst}'.")
            break
        except FileNotFoundError:
            print("** File not found. Please try again.")
        except Exception as e:
            print(f"** Error: {e}")
            break

def copy_directory():
    """Copies source directory to destination."""
    while True:
        src = input("Enter source directory path: ")
        dst = input("Enter destination directory path: ")
        try:
            shutil.copytree(src, dst)
            print(f"Directory copied from '{src}' to '{dst}'.")
            break
        except FileNotFoundError:
            print("** Directory not found. Please try again.")
        except FileExistsError:
            print("** Destination directory already exists. Please try again with a different name.")
        except Exception as e:
            print(f"** Error: {e}")
            break

def move_file_or_directory():
    """Moves file or directory to another location."""
    while True:
        src = input("Enter source file/directory path: ")
        dst = input("Enter destination path: ")
        try:
            shutil.move(src, dst)
            print(f"Moved '{src}' to '{dst}'.")
            break
        except FileNotFoundError:
            print("** File or directory not found. Please try again.")
        except Exception as e:
            print(f"** Error: {e}")
            break

def display_disk_usage():
    """Displays disk usage for specified path."""
    while True:
        path = input("Enter path to check disk usage: ")
        try:
            usage = shutil.disk_usage(path)
            print(f"Disk usage for '{path}':")
            print(f"  Total: {usage.total} bytes")
            print(f"  Used: {usage.used} bytes")
            print(f"  Free: {usage.free} bytes")
            break
        except FileNotFoundError:
            print("** Path not found. Please try again.")
        except Exception as e:
            print(f"** Error: {e}")
            break

def main():
    while True:
        print(f"\n{OPT_COPY_FILE}.\tCopy File")
        print(f"{OPT_COPY_DIRECTORY}.\tCopy Directory")
        print(f"{OPT_MOVE_FILE_OR_DIRECTORY}.\tMove File or Directory")
        print(f"{OPT_DISK_USAGE}.\tDisplay Disk Usage")
        print(f"{OPT_QUIT}.\tExit Script")

        try:
            usr_option = int(input("Enter menu option: "))
        except ValueError:
            print("** Only integer option values accepted.")
            continue

        if usr_option == OPT_QUIT:
            print("Goodbye!")
            break
        elif usr_option == OPT_COPY_FILE:
            copy_file()
        elif usr_option == OPT_COPY_DIRECTORY:
            copy_directory()
        elif usr_option == OPT_DISK_USAGE:
            display_disk_usage()
        elif usr_option == OPT_MOVE_FILE_OR_DIRECTORY:
            move_file_or_directory()
        else:
            print("** Unrecognized menu option.")

if __name__ == "__main__":
    main()
