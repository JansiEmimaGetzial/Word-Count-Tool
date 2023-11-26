To use the Word Count Tool, follow these steps:

1. Run the program.
2. Enter the filename when prompted.
3. The tool will display the word count of the specified file.

## Implementation Details

The main functionality is encapsulated in the word_read() function, which takes the file_name as a parameter. Inside this function:

- The file is opened using the open() command.
- The content of the file is read using file.read().
- The text is split into words using text.split().
- The number of words is determined using len(words).

To enhance user experience, a try-except block is implemented. If the user provides a valid file name, the try block executes; otherwise, the except block handles the FileNotFoundError.

## Example

python
try:
    word_read("sample.txt")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")


This tool ensures a smooth experience for users, gracefully handling potential errors. Happy word counting!
