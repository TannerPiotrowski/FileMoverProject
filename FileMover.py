import os
import shutil

print("\n")
print("What would you like this program to do for you?")
print("\n")
print("1. Move files from one directory to another.")
print("2. Create sub folders in a pre-existing directory.")
print("3. Move files from one directory to another and create sub folders in the directory the files were moved to.")
print("\n")
choice = input("Please select one of the above options: ")
print("\n")


def moveFiles():

    filesFrom = input("Enter the path of the folder you wish to have your files moved from: ")
    filesTo = input("Enter the path of the folder you wish to move your files to: ")
    print("\n")

    files = os.listdir(filesFrom)

    # moves files from one folder to another
    for file in files:
        srcPath = os.path.join(filesFrom, file)
        destPath = os.path.join(filesTo, file)

        if os.path.exists(destPath):
            print(f"File '{file}' already exists in the '{filesTo}' folder. Skipping.")
        else:
            shutil.move(srcPath, destPath)
            print(f"Moved '{file}' to '{filesTo}'")

    return filesTo


def createSubFolders(filesTo):

    # Organize the destination folder. sort by file type
    # List all files in the destination folder
    files = os.listdir(filesTo)

    # Organize the destination folder by sorting files into subfolders based on file type
    for file in files:
        filePath = os.path.join(filesTo, file)
        fileType = os.path.splitext(file)[1][1:]  # Extract file extension without the dot

        # If the file has no extension, consider it as 'misc'
        if not fileType:
            #fileType = 'misc'  # With this in, program tries to move folders inside of themselves
            continue

        typeFolder = os.path.join(filesTo, fileType)
        
        # Create the subfolder if it doesn't exist
        if not os.path.exists(typeFolder):
            os.makedirs(typeFolder)

        # Move the file into the respective subfolder
        shutil.move(filePath, os.path.join(typeFolder, file))
        print(f"Moved '{file}' to '{typeFolder}'")



if choice == '1':
    filesTo = moveFiles()
    print("\n")
    print(f"Files have been moved to {filesTo}")
elif choice == '2':
    directory = input("Which directory do you wish to organize: ")
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist. Try again.")
    else:
        createSubFolders(directory)
        print("\n")
    print(f"Sub-folders have been created in '{directory}'")
elif choice == '3':
    destination = moveFiles()
    print("\n")
    print(f"Files have been moved to {destination}")
    createSubFolders(destination)
    print("\n")
    print(f"Sub-folders have been created in '{destination}'")
else:
    print("Invalid option. Please select a valid option to proceed. Try again.")