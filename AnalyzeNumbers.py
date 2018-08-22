
num = int(input('How many numbers to analyze: '))
total_sum = 0

for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers

avg = total_sum/num 

print('Sum of ', num, ' numbers is:', total_sum)
print('Average of ', num, ' numbers is:', avg)

