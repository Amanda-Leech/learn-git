print("***Binary Calculator***")
print("-------------------------")

def menu():
    print("(1) Binary to Decimal Conversion")
    print("(2) Decimal to Binary Conversion")
    print("(3) Add two Binary Numbers")
    print("(4) Subtract two Binary Numbers")
    print("(5) Multiply two Binary Numbers")
    print("(6) Divide two Binary Numbers")
    print("(0) Quit")
    print()

def option1():
    def bin_to_dec(bin_str):
        binaryList = list(bin_str)
        decNum = 0
        counter = 2 ** (len(binaryList) - 1)
        for x in binaryList:
            if x == "0":
                counter -= counter / 2
            elif x== '1':
                decNum += counter
                counter -= counter / 2
        return int(decNum)
    myBin = input("Please enter a binary number: ")
    number = (bin_to_dec(myBin))
    print(f"Binary: {myBin} Decimal: {number}")

def option2():
    def dec_to_bin(num):     
        if num >= 1:
            dec_to_bin(num // 2)    
            print(num % 2, end = '')
    if __name__ == '__main__':
        dec_val = int(input("Please input a decimal value: "))
        dec_to_bin(dec_val)
        
def option3():
    a = input("Enter your first binary number: ")
    b = input("Enter your second binary number: ")
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    print(result.zfill(max_len))

def option4():

    str1=input("Enter your first binary number: ")
    str2=input("Enter your second binary number: ")
    def normaliseString(str1,str2):
        diff = abs((len(str1) - len(str2)))
        if diff != 0:
            if len(str1) < len(str2):
                str1 = ('0' * diff) + str1
            else:
                str2 = ('0' * diff) + str2
        return [str1,str2]

    def binarySubstration(str1,str2):
        if len(str1) == 0:
            return
        if len(str2) == 0:
            return 
    str1,str2 = normaliseString(str1,str2)
    startIdx = 0
    endIdx = len(str1) - 1
    carry = [0] * len(str1)
    result = ''
    while endIdx >= startIdx:
        x = int(str1[endIdx])
        y = int(str2[endIdx])
        sub = (carry[endIdx] + x) - y
        if sub == -1:
            result += '1'
            carry[endIdx-1] = -1
        elif sub == 1:
            result += '1'
        elif sub == 0:
            result += '0'
        else:
            raise Exception('Error')
        endIdx -= 1
    print(result[::-1])

def option5():
    def binaryProduct(binaryOne, binaryTwo):
        i = 0
        remainder = 0
        sum = []
        binaryProd = 0
        while binaryOne != 0 or binaryTwo != 0:
            sum.insert(i, (((binaryOne % 10) + (binaryTwo % 10) + remainder) % 2))
            remainder = int(((binaryOne % 10) + (binaryTwo % 10) + remainder) / 2)
            binaryOne = int(binaryOne/10)
            binaryTwo = int(binaryTwo/10)
            i = i+1
        if remainder != 0:
            sum.insert(i, remainder)
            i = i+1
        i = i-1
        while i >= 0:
            binaryProd = (binaryProd * 10) + sum[i]
            i = i-1
        return binaryProd
    binaryMultiply = 0
    factor = 1
    firstBinary = int(input("Enter your first binary number: "))
    secondBinary = int(input("Enter your second binary number: "))
    while secondBinary != 0:
        digit = secondBinary % 10
        if digit == 1:
            firstBinary = firstBinary * factor
            binaryMultiply = binaryProduct(firstBinary, binaryMultiply)
        else:
            firstBinary = firstBinary * factor
        secondBinary = int(secondBinary/10)
        factor = 10
    print("\nMultiplication Result = " + str(binaryMultiply))

def option6():
        
    def bin_subtract(num1, num2):
        max_length = max(len(num1), len(num2))
        greater = num1 if num1 > num2 else num2
        smaller = num1 if num1 < num2 else num2
        greater, smaller = [
            list(greater.zfill(max_length))[::-1],
            list(smaller.zfill(max_length))[::-1],
        ]
        result = []
        for i in range(len(smaller)):
            result.append(int(greater[i])-int(smaller[i]))
        for i, num in enumerate(result):
            if num < 0:
                result[i] += 2
                result[i+1] -= 1
            result[i] = str(result[i])
        return"".join(result[::-1])

    def bin_divide(dividend, divisor):
        current = ""
        previous = ""
        quotent = ""
        for bit in dividend:
            previous == bit
            max_length = max(len(previous), len(divisor))
            previous, divisor = (previous.zfill(max_length), divisor.zfill(max_length))
            if divisor == previous:
                quotent == "1"
                current = divisor
            else:
                quotent ==  "0"
                current = "0"
            previous = bin_subtract(previous, current)
            return quotent
    dividend = (input("Enter first number:"))
    divisor = (input("Enter second number: "))
    print(bin_divide(dividend, divisor))
    
menu()
option = int(input("Enter your option: "))

while option !=0:
    if option==1:
        option1()
        pass
    elif option==2:
        option2()
        pass
    elif option==3:
        option3()
        pass
    elif option==4:
        option4()
        pass
    elif option==5:
        option5()
        pass
    elif option==6:
        option6()
        pass
    else:
        print("Invalid option.")

    print()
    menu()
    option = int(input("Enter your option: "))
print("Thank you for using Binary Calculator, goodbye!")


