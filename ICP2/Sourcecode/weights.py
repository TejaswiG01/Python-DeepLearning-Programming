# entering range of students
n = int(input("Enter the number of Students:"))
# creating two lists
lbs = []
kgs = []
# loop for entering the weights in lbs
for i in range(0, n):
    lbs.append(int(input("Enter the weight in lbs:")))

# list comprehensive for converting lbs to kg
kgs = [i/2.2046 for i in lbs]

# print both the lists
print("Weights in lbs:", lbs)
print("Weights in kgs:", kgs)
