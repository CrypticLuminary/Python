# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = sorted(set(arr), reverse=True)
#     print(result[1])


# def get_second_lowest_score(students):
#     record = sorted(set([score for _, score in students]))
#     sec_lowest_score = record[1]
#     second_lowest = sorted([name for name,score in students if score == sec_lowest_score])
#     return second_lowest

# if __name__ == '__main__':
#     n = int(input())

#     students = []

#     for _ in range(n):
#         name = input()
#         score = float(input())
#         students.append([name,score])

#     print(students)
#     result = get_second_lowest_score(students)
#     for name in result:
#         print(name) 

# first,*fruits = input().split()
# print(first, fruits)

# def average(students_marks,queru_name):
#     score = students_marks[queru_name]
#     avg = sum(score)/len(score)
#     return avg

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

#     average_mark = average(student_marks,query_name)
#     print("{:.2f}".format(average_mark))

    

# if __name__ == '__main__':
#     N = int(input())
#     arr = []
    
#     for _ in range(N):
#         command = input().strip().split()
        
#         if command[0] == "insert":
#             arr.insert(int(command[1]), int(command[2]))
#         elif command[0] == "print":
#             print(arr)
#         elif command[0] == "remove":
#             arr.remove(int(command[1]))
#         elif command[0] == "append":
#             arr.append(int(command[1]))
#         elif command[0] == "sort":
#             arr.sort()
#         elif command[0] == "pop":
#             arr.pop()
#         elif command[0] == "reverse":
#             arr.reverse()


# n = input("Enter anything ").strip().split()
# print(n)

# def swap_case(s):
#     result = ""
#     for char in s:
#         if char.isupper():
#             result += char.lower()
#         elif char.islower():
#             result += char.upper()
#         else:
#             result += char
#     return result

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)






# def split_and_join(line):
#     result = ""
#     for char in line:
#         result = result + "-".join(char.split())
#     return result

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
