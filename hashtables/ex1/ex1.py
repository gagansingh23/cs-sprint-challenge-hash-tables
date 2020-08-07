def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_idc = {}

    for i in range(length):
        weight_idc[weights[i]] = i 

    for i in range(length):
        goal = limit - weights[i]
        if goal in weight_idc:
            if weight_idc[goal] > i:
                return (weight_idc[goal], i)
            else:
                return (i, weight_idc[goal])

    return None
