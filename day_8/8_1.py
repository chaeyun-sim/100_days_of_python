# prime checker

def prime_checker(number):
  for i in range(2, number):
    is_prime = True
    if number % i == 0 and number % 1 == 0:
      is_prime = False
  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)