#Write a Python program to append text to a file and display the text.

def Appendtext(fname):
	with open(fname,'a+') as f:
		f.write('appending line 1, ')
		f.write('appending line 2. ')
	#f.close()
# y=open('file1.txt')
# print(y.read())
Appendtext('test.txt')

x= open('test.txt')
print(x.read())