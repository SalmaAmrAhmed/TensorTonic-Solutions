def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here

    i = 0
    x_curr = x0
    while i < steps:
        x_ = (2*a*x_curr) + b
        x_new = x_curr - (lr * x_)
        x_curr = x_new
        i+=1


    return(x_new)