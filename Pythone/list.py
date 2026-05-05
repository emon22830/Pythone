# a = [12,13,14,15,16]

# # print(a[0:3])
# # print(a[0])

# for i in range(len(a)):
#     print(a[i]);


# for i in a:
#     print(i);

# print(dir(list));

# l = [1,2,3,4,56]

# l.append(78);
# l.insert(1,2)

# print(l)

# l = [-45,67,12,-68,-69, 35]


# print("positive elements are ")
# for i in l:
#     if i >=0:
#         print(i)

#     print("negative elements are")
#     for i in l:
#         if i < 0:
#             print(i)


# l = [12,23,45,6,57,686,77,87]
# sum = 0;

# for i in l:
#     sum = sum+i;
# print(sum/len(l))


l = [12,345,56,7,78,9]

largest=l[0];
index = 0

for i in range (len(l)):
            if l[i] >largest:
                    largest = l[i]
                    index = i 


                    print(f"Your largest number is {largest} at index {index} ");

l = [12,16,13,19, 17]

largest = l[0]
sec_largest = l[0]

for i in l:
        if i > largest:
                sec_largest = largest
                largest = i

        elif i > sec_largest:
                sec_largest = i




                print(sec_largest, largest)


