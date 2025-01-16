def cal_odd_even(n):
  for i in range (n, n+1):
    if i % 2==0:
      return 'Even'
    else:
      return "You number Odd"
    
result= cal_odd_even(int(input('Enter your number: ')))
print(result)