def binary_array_to_number(binary):
    #your code
    #Binary to Decimal
    str_lst = []
    arr = []
    arr = []
    place = 0
    result = 0
    FinalResult = 0

    for i in binary:
        str_lst.append(i)

    for Item in str_lst:
        item = Item
        arr.append(int(item))

    x = len(arr) -1
    for i in range(len(arr)):
        if arr[x] == 1:
            result = 2**place
            FinalResult = FinalResult+result
        x-=1
        place+=1
    return FinalResult


def number_to_binary_array(number):
    number = int(number)
    arr = []
    binary = ""
    while number > 0:
        if number/2 - number //2 > 0.0:
            arr.append(int(1))
        else:
            arr.append(int(0))
        number = number//2

    for Items in arr:
        binary = str(Items)+binary
    return binary

chosen = False

while chosen == False:
    bi_or_de = "Test"
    #bi_or_de = input("Tippe \"Binary\" um Binär in Dezimal zu wandeln. Tippe \"Decimal\" um Dezimal in Binär zu wandeln: \n")

    if bi_or_de == "Binary":
        print(binary_array_to_number(input(str("Gebe eine Binäre Zahl ein: "))))
        chosen = True

    elif bi_or_de == "Decimal":
        print(number_to_binary_array(input("Gebe eine Dezimal Zahl ein: ")))
        chosen = True

    elif bi_or_de == "Test":
        print(number_to_binary_array(42))
        print(binary_array_to_number("101010"))
        chosen = True

    else:
        print("Falsche angabe!")