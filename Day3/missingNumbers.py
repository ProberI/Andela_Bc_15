def find_missing(nums1, nums):
    missing = []
    for n in one:
        if n not in two:
            missing.append(n)
    for n in two:
        if n not in one:
            missing.append(n)

    if len(missing) > 0:  # Length being less than 0 would mean no missing numbers
        if len(missing) == 1:
            return missing[0]
        else:
             return missing  # To return multiple numbers where more than one is missing
    else:

        return 0
