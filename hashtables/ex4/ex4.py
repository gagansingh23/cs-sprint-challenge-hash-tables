def has_negatives(a):
    """
    YOUR CODE HERE
    """
    corr_neg = {}
    result = []
    for i in a:
        corr_neg[i] = i
        if i != 0 and -i in corr_neg:
            result.append(abs(i))
            print(i)

    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
