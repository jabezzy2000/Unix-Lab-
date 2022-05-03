import sys
#creating a ceaser cypher
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#length = 26
shift = int(sys.argv[1])
#shift = int(input("Enter the number of shifts you want: "))
message = input("Input the message: ")
message= message.upper()
empty_str = ""
minimum_shift = 26 - shift
for i in message:
    if i == " ":
        empty_str += i
    else:
        for j in i:
            position = letters.index(j)
            if position < minimum_shift:
                position = position + shift
                empty_str+= letters[position]
            elif position >= minimum_shift:
                position = position + shift - 26
                empty_str += letters[position]



ls = [j for i in empty_str for j in i if j!=" "]
to_print = ""
length = len(ls)-1
counter5 = 0
counter10=0
change = False

for i in range(length):
    if counter5 == 5:
        to_print+=" "
        #to_print+=i
        counter5 =1
        counter10+=1
        change=True
    elif counter10 ==10:
        to_print+="\n"
        counter10 =1
        counter5+=1
        to_print+=ls[i]
    elif change:
        to_print+=ls[i-1]
        to_print+=ls[i]
        change= False
        counter5+=1
    else:
        to_print+=ls[i]
        counter5+=1

print(to_print)
