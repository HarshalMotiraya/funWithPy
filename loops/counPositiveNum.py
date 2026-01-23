
number = [1,-2,3,-4,5,6,-7,8,9,-10]
postive_number_count = 0
for num in number:
    if num > 0:
        postive_number_count = postive_number_count + 1

length = len(number)
length2 = len(str(postive_number_count))

print("final count of positive number is :",postive_number_count)
print("length of count is :",number)
print("length of count is :",length2)