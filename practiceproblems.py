#I am working my way through Elements of Programming Interviews, and my code lives here.

#fizz-buzz
def fizz_buzz(fizz, buzz, n):
    for x in range(0, n):
        if x % fizz == 0 and x % buzz==0:
            print("{}: FizzBuzz".format(x))
        elif x % fizz == 0:
            print("{}: Fizz".format(x))
        elif x % buzz ==0:
            print("{}: Buzz".format(x))



#going off book today and doing one from the interwebz
#Count the occurence of a given character in a string
#input: a string
#parameters: the character we want to count
#output: the number of times that character appears in the string.
def count_chars_naive(x, c):
    count =0
    for ch in x:
        if ch == c:
            count+=1
    return count

#input: an array of positive integers representing the number of citations in a list of publications.
#output: the h-index (the largest value of h s.t. the researcher has published h papers that have been cited at least h times)
def h_index(citations):
    h_value = 0
    count = 0
    #walk through starting with 1
    while count >= h_value:
        h_value = h_value+1
        count = count_h(citations, h_value)
        print("H: {} Count: {}".format(h_value, count))
    return h_value -1

def count_h(citations, h):
    count = 0
    for paper in citations:
        if paper>=h:
            count+=1
    return count


def improved_h_index(citations):
    citations.sort()
    l = len(citations)
    for i, c in enumerate(citations):
        if c >= l-i:
            return l-i
    return 0

def main():
    #citations = [1,4,1,4,2,1,3,5,6]
    #print(improved_h_index(citations))
    #print(count_chars_naive('this is a test', 't'))
    print(fizz_buzz(3, 5, 50))


if __name__ =="__main__":
    main()
