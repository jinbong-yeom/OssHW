#오픈소스시간에 수행한 파이썬 코딩도장의 회문판별 문제입니다.
class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')
    
    
def palindrome(word):
    if list(word)==list(reversed(word)):
        print(word)
    else:
        raise NotPalindromeError
        
try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
#파이썬 코딩 도장의 시간 클래스 문제입니다.
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @staticmethod
    def is_time_valid(time_string):
        hour,minute,second=map(int,time_string.split(':'))
        return hour<=24 and minute<=59 and second<=60
    @classmethod
    def from_string(cls,time_string):
        hour,minute,second=map(int,time_string.split(':'))
        time=cls(hour,minute,second)
        return time
    time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
#파이썬 코딩 도장의 지뢰찾기 문제입니다
col,row=input().split()
col=int(col)
row=int(row)
matrix=[]
count=0
for i in range(row):
    matrix.append(list(input()))
for j in range(row):
    for k in range(col):
        if j==0 and k==0:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j][k+1]=='*':
                    count+=1
                if matrix[j+1][k+1]=='*':
                    count+=1
                if matrix[j+1][k]=='*':
                    count+=1
                print(count,end='')
                count=0
                    
        elif j==0 and k==col-1:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j][k-1]=='*':
                    count+=1
                if matrix[j+1][k-1]=='*':
                    count+=1
                if matrix[j+1][k]=='*':
                    count+=1
                print(count,end='')
            print()  
            count=0
            break
                    
        elif j==0:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j][k-1]=='*':
                    count+=1
                if matrix[j+1][k-1]=='*':
                    count+=1
                if matrix[j+1][k]=='*':
                    count+=1
                if matrix[j+1][k+1]=='*':
                    count+=1
                if matrix[j][k+1]=='*':
                    count+=1
                print(count,end='')
                count=0
            
        elif j==row-1 and k==0:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j-1][k]=='*':
                    count+=1
                if matrix[j-1][k+1]=='*':
                    count+=1
                if matrix[j][k+1]=='*':
                    count+=1
                print(count,end='')
                count=0
                
        elif j==row-1 and k==col-1:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j-1][k]=='*':
                    count+=1
                if matrix[j-1][k-1]=='*':
                    count+=1
                if matrix[j][k-1]=='*':
                    count+=1
                print(count,end='')
            print()  
            count=0
            break
        
        elif j==row-1:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j][k-1]=='*':
                    count+=1
                if matrix[j-1][k-1]=='*':
                    count+=1
                if matrix[j-1][k]=='*':
                    count+=1
                if matrix[j-1][k+1]=='*':
                    count+=1
                if matrix[j][k+1]=='*':
                    count+=1
                print(count,end='')
                count=0          
            
        elif k==0:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j-1][k]=='*':
                    count+=1
                if matrix[j-1][k+1]=='*':
                    count+=1
                if matrix[j][k+1]=='*':
                    count+=1
                if matrix[j+1][k+1]=='*':
                    count+=1
                if matrix[j+1][k]=='*':
                    count+=1
                print(count,end='')
                count=0
                
        elif k==col-1:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j-1][k]=='*':
                    count+=1
                if matrix[j-1][k-1]=='*':
                    count+=1
                if matrix[j][k-1]=='*':
                    count+=1
                if matrix[j+1][k-1]=='*':
                    count+=1
                if matrix[j+1][k]=='*':
                    count+=1
                print(count,end='')
            print()
            count=0
            break

        else:
            if matrix[j][k]=='*':
                print('*',end='')
            elif matrix[j][k]=='.':
                if matrix[j][k-1]=='*':
                    count+=1
                if matrix[j-1][k-1]=='*':
                    count+=1
                if matrix[j-1][k]=='*':
                    count+=1
                if matrix[j-1][k+1]=='*':
                    count+=1
                if matrix[j][k+1]=='*':
                    count+=1
                if matrix[j+1][k+1]=='*':
                    count+=1
                if matrix[j+1][k]=='*':
                    count+=1
                if matrix[j+1][k-1]=='*':
                    count+=1
                print(count,end='')
                count=0
