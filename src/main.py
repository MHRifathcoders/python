def cal_odd_even(n):
  odd=[]
  even=[]
  for i in range (1, n+1):
    if i % 2==0:
      odd.append(i)
    else:
      even.append(i)
  print('odd number', *odd)
  print('even number', *even)
    
cal_odd_even(int(input('Enter your number: ')))
