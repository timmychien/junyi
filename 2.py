def choose_num(number):
  nums=[num for num in range(1,number+1)]
  temp=[]
  for num in nums: 
    if num%15==0:
      temp.append(num)
    elif num%3!=0 and num%5!=0:
      temp.append(num)
  return temp