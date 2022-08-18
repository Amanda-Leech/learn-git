def binary_sub(srt1,srt2):
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
    return(result[::-1])

print(binary_sub)
