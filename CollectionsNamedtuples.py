from collections import namedtuple
n = input()
bin_names = ' '.join(raw_input().split()) 
Student = namedtuple('Student', bin_names)

student_list = []

for i in range(n):
    student_list.append(int(Student(*[i for i in raw_input().split()]).MARKS))
    
print float(sum(student_list))/float(n)
