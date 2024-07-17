# location of the text file
file_name='C:\Users\Chandra sekhar\Desktop/test_py.txt'

try:
    file=open(file_name,'r')
    content=file.read()
    print(content)
finally:
    file.close()





