list = ['apple', 'banana', 'kiwi', 'pizza']


for e, i in enumerate(list):
    print(e,i)

''' result 
0 apple
1 banana
2 kiwi
3 pizza
'''

startIndex = 2
for e, i in enumerate(list,startIndex):
    print(e,i)

''' result
2 apple
3 banana
4 kiwi
5 pizza
'''