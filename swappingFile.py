global file1_contents,file2_contents
with open('file1.txt') as f1, open('file2.txt') as f2:
    file1_contents = f1.read()
    file2_contents = f2.read()

# write the files, swapping them.
open('file1.txt','w').write(file2_contents)
open('file2.txt','w').write(file1_contents)

print('Successfully swapped the two files!')
print('file 1: {}, file 2: {}!'.format(file1_contents,file2_contents))