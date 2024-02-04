# "Question 2 Python:"
def max_character_count(strings):
    """This function is use to count the max repeatable word if there is same repeatability then it will check
    on the basis of word length"""
    
    
    string = strings 
    string_new = string.split(" ")

    try: 

        string2 = []
        set1 = set(string_new)

        for i in set1:
            string2.append([string.count(i),i])
    
        

        value = max(string2)
        print(len(value[1]))
    except:
        print("Program is Not working ")
        
# EXample:
string = 'write write write all the number from from from 1 to 100'
max_character_count(strings=string) 
