#I am working my way through Elements of Programming Interviews, and my code lives here.

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
    citations = [1,4,1,4,2,1,3,5,6]
    print(improved_h_index(citations))

if __name__ =="__main__":
    main()
