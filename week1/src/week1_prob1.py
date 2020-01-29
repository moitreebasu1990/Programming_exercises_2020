# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
# are not zero­based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
#
# Output: index1=1, index2=2

#Solution1:
#Complexity n^2

def twoSum1(numbers, target):
    for index1, num1 in enumerate(numbers):
        for index2, num2 in enumerate(numbers[index1+1:]):

            if num1+num2 == target:
                #print(index1+1, index1+2+index2)
                print(f"index1={index1+1}, index2={index1+2+index2}")
                break


#Solution2:
#Complexity nlogn


def twoSum2(numbers, target):
    print("Blank")


def main():
    numbers=[8,5,1,13]
    target=9
    twoSum1(numbers, target)
    twoSum2(numbers, target)

if __name__ == "__main__":
    main()

