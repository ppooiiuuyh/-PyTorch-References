import os


f = open("./test/test.txt", 'w')
''' result log
Traceback (most recent call last):
  File "/root/바탕화면/workspace/pytorch_tutorial/torch_referneces/folder create.py", line 5, in <module>
    f = open("./test/test.txt", 'w')
FileNotFoundError: [Errno 2] No such file or directory: './test/test.txt'
'''



if not os.path.isdir(os.path.join('./test')):
    os.makedirs(os.path.join('./test'), exist_ok=True)
    f = open("./test/test.txt", 'w')
    f.close()