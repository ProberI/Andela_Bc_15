def find_max_min(numlist):

    maximum = numlist[0]
    minimum = numlist[0]
    array_ = []  # created an array to store output

    for value in numlist:  # the for loop makes it easier to iterate through the list given
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value

    if maximum == minimum:  
        array_.append(len(numlist))
        return array_
    else:
        array_.append(minimum)
        array_.append(maximum)
        return array_
