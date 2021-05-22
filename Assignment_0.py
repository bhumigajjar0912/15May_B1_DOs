import string
#Question 1
print('Question 1')

numbers = [386, 462, 47, 418, 907, 344, 236, 375,
 823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
  758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
   626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
    894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
     958,743, 527]

for i in numbers:
    if i == 237:
        break
    if i%2 == 0:
        print(i)
print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 2
print('Question 2')

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 3
print('Question 3')

s = input('Enter String: ')
alpha_set = set(string.ascii_lowercase)
s = s.lower()
string_list =[]
for i in s:
    if i.isalpha():
        string_list.append(i)
string_list.sort()
# print(string_list)
string_list = set(string_list)
# print(string_list)
if len(alpha_set - string_list) == 0:
    print('The string is PANGRAM!!')
else:
    print('The string is not PANGRAM!!')

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 4
print('Question 4')

n = int(eval(input('Enter an intiger: ')))
print(n+(n*10+n)+(n*100+n*10+n))

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 5
print('Question 5')

s = input('Enter string: ')
s = s.split('#')
s1 = s[0].split()
s2 = s[1].split()
s1 = [int(i) for i in s1]
s2 = [int(i) for i in s2]
print(s1)
print(s2)

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 6
print('Question 6')

s = input('Enter string: ')
s = s.split(',')
s.sort()
print(s)

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 7
print('Question 7')

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
idx = d['Marks'].index(max(d['Marks']))
print(d['Student'][idx])

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 8
print('Question 8')

s = input('Enter string: ')
letter = 0
digits = 0
for i in s:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letter+=1
print('LETTERS '+str(letter))
print('DIGITS '+str(digits))

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 9
print('Question 9')

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
d1 = {}
subject = input('Input: ')

idx = 0
subject_index = []
lst = []
for idx,i in enumerate(d['Subject']):
    if i == subject:
        subject_index.append(idx)
        
d1_keys = ['Name', 'Subject', 'Ratings']
d1_values = ['','','']

for idx,i in enumerate(d.values()):
    lst = []
    for j in subject_index:
        lst.append(i[j])
    d1_values[idx] = lst
print(dict(zip(d1_keys,d1_values)))


print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 10
print('Question 10')

class Generator:
    lst = []
    # def __init__(self):
    #     pass
    def generator(self, n):
        for i in range(0,n):
            if i%7 == 0:
                yield i
        return Generator.lst

m = Generator() 
n = int(eval(input('Enter the value of n: ')))
for i in m.generator(n):
    print(i)

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
#Question 11
print('Question 11')

input_list = []
x = None
print('Enter direction and route(in this format DIRECTION<space>STEPS):')
for _ in range(0,4):
    s = input('')
    x = s.split(' ')
    input_list.append(x)
up_steps = 0
down_steps = 0
left_steps = 0
right_steps = 0

for i in input_list:
    if i[0].upper() == 'UP':
        up_steps = int(i[1]) 
    elif i[0].upper() == 'DOWN':
        down_steps = int(i[1])
    elif i[0].upper() == 'LEFT':
        left_steps = int(i[1])
    elif i[0].upper() == 'RIGHT':
        right_steps = int(i[1])

v_distance = up_steps-down_steps
h_distance = left_steps-right_steps

print(v_distance)
print(h_distance)

total_diatance = round(abs(((v_distance**2)+(h_distance**2))**0.5))
print(total_diatance)

print("_"*15+'END'+"_"*15+'\n\n')
#
#
#
