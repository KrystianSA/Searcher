from pathlib import Path
import argparse
import re


def lookingForFile(extension, directory):
    files = []
    for file in Path(directory).rglob('*' + extension):
        files.append(file)
    return files


def lookingForContent(files):

    patterns = [
            r'\w+:\w+',
            r'\d+'
            # Add Here your pattern. Example: r'Here your pattern'
    ]

    for file in files:
        fileToRead = open(file, 'r')
        content = fileToRead.read()
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                print(match)
        fileToRead.close()


def main(extension, directory):
    file = lookingForFile(extension, directory)
    lookingForContent(file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        usage="searcher.py <extension> <directory>",
        description="If you need an additional pattern, just add it to the list"
    )

    parser.add_argument('extension', help='Extension to search for')
    parser.add_argument('directory', help='Directory to search in')
    args = parser.parse_args()

    main(args.extension, args.directory)
