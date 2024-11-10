from pathlib import Path
import argparse
import re


def lookingForFile(extension, directory):
    files = []
    for file in Path(directory).rglob('*' + extension):
        files.append(file)
    return files


def lookingForContent(files,nameOfOutputFile):

    patterns = [
            r'\w+:\w+',
            r'\d+'
            # Add Here your pattern. Example: r'Here your pattern'
    ]

    dictionary = {}
    for file in files:
        fileToRead = open(file, 'r')
        content = fileToRead.read()
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                print(match," - ", file)
                dictionary[match] = file

        fileToRead.close()

    if args.output:
        writeToFile(dictionary, nameOfOutputFile)

def writeToFile(dictionary, nameOfOutputFile):
    with open(nameOfOutputFile,'w') as file :
        for key, value in dictionary.items():
            file.write(f"{key} - {value} \n")

def main(extension, directory, nameOfOutputFile):
    file = lookingForFile(extension, directory)
    lookingForContent(file, nameOfOutputFile)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        usage="searcher.py <extension> <directory>",
        description="If you need an additional pattern, just add it to the list"
    )

    parser.add_argument('-e','--extension', help='Extension to search for')
    parser.add_argument('-d','--directory', help='Directory to search in')
    parser.add_argument('-o','--output', required=False, help='Name of output file')
    args = parser.parse_args()

    main(args.extension, args.directory, args.output)
