from pathlib import Path 
import argparse
import re

def lookingForFile(extension, directory):
    for file in Path(directory).rglob('*' + extension):
        return file

def lookingForContent(file, pattern=None):    
    fileToRead = open(file, 'r')
    content = fileToRead.read()

    if pattern:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' + pattern
    else:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    matches = re.findall(pattern,content)
    for match in matches:
        print(match)
    fileToRead.close()

def main(extension, directory, pattern=None):
    file = lookingForFile(extension, directory)
    lookingForContent(file, pattern)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Example: searcher.py <extension> <directory>')
    parser.add_argument('extension', help='Extension to search for')
    parser.add_argument('directory', help='Directory to search in')
    parser.add_argument('-p', '--pattern', help='Additional pattern to search for')
    args = parser.parse_args()

    main(args.extension, args.directory, args.pattern)