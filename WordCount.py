print("WORD COUNT TOOL")

def word_read(file_name):
    try:
        with open(file_name,'r') as file:
            text = file.read()
            words = text.split()
            word_count=len(words)
        return word_count
    
    except FileNotFoundError:
        return 'File Not Found'
    except Exception as e:
        return f'An Error Occured:'
    
file_name=input("Enter the File Name : ")
word_count= word_read(file_name)
print(f'The file \"{file_name}\" contains {word_count} words.')
