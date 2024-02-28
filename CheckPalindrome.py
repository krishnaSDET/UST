class check():
    def check_palindrome(self, num):
        if num == 0:
            return True
        if num < 0 or num % 10 == 0:
            return False

        reverse_value =0
        orginal_value = num
        while num > 0:
            reminder = num % 10
            num =num //10
            reverse_value = reverse_value*10+reminder
        print(reverse_value)
        if reverse_value == orginal_value:
            return True


a = check()
n=int(input("enter a valid number "))
result = a.check_palindrome(n)
if result:
    print("valid palindrome")
else:
    print("not a palindrome")