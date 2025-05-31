# first non repeating character in the string
def non_repeat(str):
    sample = []
    for char in str:
        if str.count(char) == 1:
            sample.append(char)

    return sample   



str = "programming"
print(non_repeat(str))        


