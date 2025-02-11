from itertools import permutations as pr
from math import pow, pi as P
from random import randint
class myclass:
    def togramm(gramm):
        ounes = gramm * 28.3495231
        return f"{ounes} ounes"
    def toC(F):
        C = (5/9)*(F-32)
        return f"{C} C"
    def puzzle(n, m):
        x = (4*n-m)/2
        y = (m-2*n)/2
        return f"chickens = {x}, rabbits {y}"
    def prime(mylist):
        Maxn = mylist[0]
        for el in mylist:
            if el <= Maxn:
                Maxn = el
        return f"Maximum is {Maxn}"
    def perm(mylist2):
        mylist2.sort()
        perm = pr(mylist2)# permutations as pr!!!!!

        for el in perm:
            print(*el)
    def reverse_sen(mylist3):
        newlist = mylist3.split()
        newlist.reverse()
        return " ".join(newlist)
    def has_33(mylist4):
        for i in range(1, len(mylist4)-1):
            if mylist4[i-1] == mylist4[i] or mylist4[i] == mylist4[i+1]:
                return True
        if mylist4[0] == mylist4[1] or mylist4[-2] == mylist4[-1]:
            return True
        return False
    def spy_game(mylist5):
        nums07 = "".join(str(i) for i in mylist5 if i == 0 or i == 7)
        return "007" in nums07
    def volume_of_sphere(R):
        if isinstance(R, int) or isinstance(R, float):
            volume = (4*P*pow(R, 3))/3
            return f"{volume:.2f} cm"
        elif isinstance(R, str):
            numbers = []
            for i in R:
                if i.isdigit() or i == ".":
                    numbers.append(i)
            r = "".join(numbers)
            r = float(r) if "." in r else int(r)
            volume = (4*P*pow(float(r), 3))/3
            unit = "cm" if "cm" in R else "mm" if "mm" in R else "km" if "km" in R else "m" if "m" in R else "Syntax eror"
            return f"{volume:.2f} {unit}"
    def myset(mylist6):
        newlist = []
        for i in mylist6:
            if i not in newlist:
                newlist.append(i)
        return newlist
    def ispalindrome(word):
        return word == word[::-1]
    def histogram(mylist7):
        for el in mylist7:
            print("*"*el)
    def game():
        print("Hello! What is your name?")
        name = input()
        print(f"Well, {name}, I am thinking of a number between 1 and 20.")
        print("If your tired enter \"q\"")
        random_number = randint(1, 20)
        number = -1
        quit = "q"
        while number != a:
            print("Take a guess")
            number = input()
            if int(number) == "q":
                print("end")
                break
            elif int(number) < random_number:
                print("Your guess is too more.")
            elif int(number) > random_number:
                print("Your guess is too low.")
            elif int(number) == random_number:
                print("Congratulations, you've won")
                break
        return 
a = myclass
a1 = [1, 2, 3, 3]
a2 = ["apple", "banana", "cherry"]
a3 = "We are ready"
# print(a.togramm(2))               # 1
# print(a.toC(32))                  # 2 
# print (a.puzzle(10, 26))          # 3
# a.isprime(a1)                     # 4
# a.perm(a1)                        # 5
# print(a.reverse_sen(a3))          # 6
# print(a.has_33(a1))               # 7
# print(a.spy_game(a1))             # 8
# print(a.volume_of_sphere("6km"))  # 9 
# print(a.myset(a1))                #10
# print(a.ispalindrome("a3"))       #11
# a.histogram(a1)                   #12
# a.game                            #13
