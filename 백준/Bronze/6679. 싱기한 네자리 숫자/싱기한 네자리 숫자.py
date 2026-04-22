for i in range(2992, 10000) :
  data = i
  sixteen = 0
  while data != 0 :
    sixteen += data % 16
    data //= 16

  data = i
  twelve = 0
  while data != 0 :
    twelve += data % 12
    data //= 12

  data = i
  ten = 0
  while data != 0 :
    ten += data % 10
    data //= 10

  if sixteen == twelve == ten :
    print(i)