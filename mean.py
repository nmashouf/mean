def mean(num_list):
    """Calculates the mean of a list of numbers"""
    try:
        a = return sum(num_list)/len(num_list)
        for i in num_list:
            if isinstance(i, complex):
                return NotImplemented
        return a
    except ZeroDivisionError as detail :
        msg = "The algebraic mean of an empty list is undefined."
        msg += "Please provide a list of numbers."
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined."
        msg += "Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
    for i in num_list:    
        if isinstance(i, complex):
            return NotImplemented
