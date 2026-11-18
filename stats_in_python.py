import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    count = 0

    with open(filepath, 'r') as infile:
        for line_number, line in enumerate(infile, start=1):
            values = line.strip().split("\t")

            try:
                num = values[column]
                count += 1 

                try:
                    num = float(num)

                    if not math.isnan(num):
                        numbers.append(num)
                
                except ValueError:
                    pass

            except IndexError:
                sys.exit(
                    f"Exiting: There is no valid 'list index' in column "
                    f"{column} in line {line_number} in file: {filepath}"
                )

    return numbers, count





def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
   
   total = sum(numbers)
   average = total / len(numbers)

   return average
   
   
 
def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    maximum = max(numbers)
    minimum = min(numbers)

    return maximum,minimum

    


def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    
    if len(numbers) == 1:
        return 0.0
    
    average = calculate_average(numbers)

    squared_differences = []
    for number in numbers:
        difference = number - average
        squared_differences.append(difference ** 2)

    variance = sum(squared_differences) / (len(numbers) - 1)

    return variance
    



def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    variance = calculate_variance(numbers)
    std_dev = math.sqrt(variance)
    
    return std_dev



def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_numbers = sorted(number)
    length = len(sorted_numbers)

    middle = length // 2

    if length % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        median = float(sorted_numbers[middle])

    return median



