from pathlib import Path 
import argparse
def main(extension, directory):
    for file in Path(directory).rglob('*' + extension):
        print(file)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Example: searcher.py <extension> <directory>')
    parser.add_argument('extension', help='Extension to search for')
    parser.add_argument('directory', help='Directory to search in')
    args = parser.parse_args()

    main(args.extension, args.directory)