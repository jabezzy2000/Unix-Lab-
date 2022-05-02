import sys
#creating a ceaser cypher
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#length = 26
shift = sys.argv
#shift = int(input("Enter the number of shifts you want: "))
message = input("Input the message: ")
message= message.upper()
empty_str = ""
minimum_shift = 27 - shift
for i in sys.stdin:
    if i == " ":
        empty_str += i
    else:
        for j in i:
            position = letters.index(j)
            if position < minimum_shift:
                position = position + shift
                empty_str+= letters[position]
            elif position >= minimum_shift:
                position = positon + shift - 26
                empty_str += letters[position]

length = len(empty_str)
counter = 0


