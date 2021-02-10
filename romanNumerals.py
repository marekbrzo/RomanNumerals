# Roman Numeral Calculator
## Author: Marek Brzozowski
## Input a Roman Numeral as a String then convert it to an integer.
### Difficulty is creating a calculator that can consider modern roman terminology of IV, IX, XL, and so forth. 
### These values do not follow sequencing order thus the smaller value is before the larger value.

class RomanNumerals:
    ''' Roman Numeral Class Contains Necessary Functions'''

    def __init__(self,roman,letters = ['I','V','X','L','C','D','M'],value=[1,5,10,50,100,500,1000]):
        ''' Create instances'''
        self.roman = roman
        self.letters = letters
        self.value = value

    def split(self):
        '''Splitting characters into list'''
        return [char for char in self.roman]

    def romanLetterCheck(self):
        '''Check to determine if the string is a Roman Numeral'''
        splitter = self.split()
        
        # Check to determine if the roman numerals are found in the inputted string.
        check = all(item in self.letters for item in splitter)

        # Return statement
        if check is True:
            print('The string inputted {} has the proper letters'.format(splitter))
            return True
        else:
            print('The item(s) within the string {} is incorrect. Please input the proper lettering, exampled as {}'.format(splitter,self.letters))
            return False
    
    def romanToInt(self):
        '''Converting roman numeral to arabic numeral'''
        # Zipping roman letters with arabic numbers.
        dictValue = dict(zip(self.letters,self.value))
        splitter = self.split()

        # Empty list to input values with the help of the zipped dictionary.
        val =[]
        for item in splitter:
            val.append(dictValue[item])
        return val

    def romanCalculator(self,number):
        '''Adding the arabic numerals'''
        # Variable sum, index
        sum_new = 0
        length = len(number)

        # Adding zero to the end, prevent out-of-index condition.
        number.append(0)
        while True:
            index =len(number)-length-1
            
            # Heart of calculator. 
            # Calculator determines if the next value of the list is smaller than the previous. If so then the value adds to the sum_new variable.
            # If the value is greater, than it changes the next value on the list. Subtracts the value with the next value.
            if number[index] > number[index+1]:
                sum_new += number[index]
            elif number[index] == number[index+1]:
                sum_new += number[index]
            else:
                number[index+1] = number[index+1] - number[index]
            
            length -= 1
            if length == 0:
                break

        return print(sum_new)

        

def main():
    ''' Main Roman converter'''
    while True:
        romanString = input('Please input a Roman Numeral: \n')
        romanString = romanString.upper()
        if romanString == "EXIT":
            break

        RomanNumerals(romanString).romanLetterCheck()
        RomanNumerals(romanString).romanCalculator(RomanNumerals(romanString).romanToInt())
        
        print('To end type EXIT:')

main()