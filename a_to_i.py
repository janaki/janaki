#Method to convert a string representative of an integer. 
# parameters: strvalue, string representation of the integer to convert 
# return value: returns the integer representation of str_value

def a_to_i(strvalue):
    #create a hashmap (python dictionary) for each integer value < 10
    a_to_i_key = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9}
    length = len(strvalue)
    #start with the first value in the string, convert to an integer and store into a variableint_value
    int_value = 10 ** (length - 1) * a_to_i_key[strvalue[0]]   

    #index and value are counters to track movement within the string. 
    index = 0
    value = 0  
    
    #loop through the string,  multiple each value by power of 10, and add to value variable. 
    for i in range(length-1, 0, -1): 
        value += (10**index) * a_to_i_key[strvalue[i]]
        index+=1  
    return int_value + value

#calling the method
string_to_integer = a_to_i("1246")
print (string_to_integer)

#Test Cases: 
#12   =  (10 ** 1) + 2
#22   =  (10 ** 1 * 2)    +  (10 ** 0 * 2)
#35   =  (10 ** 1 * 3)    + (10 ** 0 * 5) 
#246  =  (10 ** 2 * 2)    + (10 ** 1 * 4) + (10 ** 0 * 6)
#1246 =  (10 ** 3 * 1)    + (10 ** 2 * 2) + (10 ** 1 * 4) + (10 ** 0 * 6)  
