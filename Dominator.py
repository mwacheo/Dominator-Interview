from statistics import mode


def dom_count(item_a):

    #Getting Most frequent value using the mode function from the statistics module
    most_freq_value = mode(item_a)

    # define what i will compare my most frequent value with to ascertain  dominator
    half_ = len(item_a)/2

    #Condition to get dominator
    if item_a.count(most_freq_value)> half_:
        index_list= []

    #Looping through array using indices to determine index of most frequent value
        for i in range(len(item_a)):
            if item_a[i] == most_freq_value:
                index_list.append(i)
        return index_list

    else:
        return -1



if __name__ == '__main__':
    a = [3, 4, 3, 2, 3, -1, 3, 3]
    print(dom_count(item_a = a))
