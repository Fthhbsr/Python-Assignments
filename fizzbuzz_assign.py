for i in range(1, 101) :
  if not i % 15 :
    print(i, ": FizzBuzz")
  elif not i % 3 :
    print(i, ": Fizz")
  elif not i % 5 :
    print(i, ": Buzz")
  else :
    print(i)
