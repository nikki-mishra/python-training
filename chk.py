# step 1
# write a function that can take input one number and return 1 when it is prime, else 0

# def is_prime(n):
#     prime = 1
#     # logic to check if number n is prime
#
#     for i in range(2, n):
#         if n%i == 0:
#             prime = 0
#             break
#     return prime
#
#
# def count_primes_in_range(start, end, total):
#     # start se lekar end tak check karo kitne primes hain
    # count = 0
    # for i in range(start, end):
    #     x = is_prime(i)
    #     if x == 1:
    #         print(i)
    #         count += 1
    #     if count == total:
    #         break

#
# start = int(input("Start::"))
# end = int(input("End::"))
# total = int(input("Total::"))
#
# count_primes_in_range(start, end, total)
#

# class my:
#     x=4
#     y=7
# a=my()
# print(a.x)
# print(a.y)
class ok():
    def __init__(self, name,lname):
        self.name=name
        self.lname=lname
    def show(self):
        print(self.name,self.lname)
b=ok("nikki","mishra")
b.show()











