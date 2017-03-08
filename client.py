import sys

#def commands():
if(len(sys.argv) != 2):
    print "usage: a.out port filename"
    exit(1);

print sys.argv[0]
print sys.argv[1]


try:
	f = open(sys.argv[1]);
	for line in f:
		line = line.strip('\n')
		words = line.split(' ')
		for w in words:
			print w

	f.close()

except Exception as ex:
	print ex
	exit(1);



print("hello world")
