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

def main():
    citations = [1,4,1,4,2,1,3,5,6]
    print(h_index(citations))


if __name__ =="__main__":
    main()
