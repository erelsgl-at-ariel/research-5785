if __name__ == '__main__':
    import sys

    """
    A. Convert the following Java code to one line of Python:
        int[] output = new int[n];
        for (int i = 0; i < n; i++) {
           output[i] = d;
        }
    """
    n,d = map(int, input().split())
    output = "" # Put your line here (my solution: 5 chars)
    print(output)

    """
    B. Given a list v, construct a vector of n-1 differences between adjacent cells.
       Example: v=[1,4,9,16], output=[3,5,7]
    """
    v=eval(input())
    output = "" # Put your line here (my solution: 23 chars)
    print(output)
    
    """
    C. Given a list v and a number n, find *all* indices that contain the given number.
       Example: v=[1,4,9,16,9,4], n=9, output=[2,4], since 9 is found in indices 2 and 4.
    """
    v,n = [f(x) for f,x in zip((eval,int),input().split())]
    output = "" # Put your line here (my solution: 37 chars)
    print(output)

    """
    D. Given a list v and a number n, return a string where each number is replaced with "=" if it equals n and "!" if not.
       Example: v=[1,4,9,16,9,4], n=9, output="!!=!=!"
    """
    v,n = [f(x) for f,x in zip((eval,int),input().split())]
    output = "" # Put your line here (my solution: 42 chars)
    print(output)

    """
    E. Given a list v, return another list in which each element in the original list appears only once, in increasing order.
       Example: v=[16,4,9,16,9,4,1], output=[1,4,9,16]
    """
    v=eval(input())
    output = "" # Put your line here (my solution: 14 chars).
    print(output)

    """
    F. Given two n-dimensional vectors u and v, compute the Euclidean distance between them.
       Round the outcome down to the nearest integer.
       Example: u=[1,2,3,4,5], v=[1,2,0,0,5], output=5 (= the sqrt of (0^2+0^2+3^2+4^2+0^2))
    """
    u,v = map(eval, input().split())
    from math import sqrt 
    output = "" # Put your line here (my solution: 40 chars)
    print(output)

    """
    G. Given a matrix m (a list of two or more lists of the same length), return a single 1-dimensional list that is the concatenation of all rows. 
       Example: m=[[1,2],[3,4],[5,6]], output=[1,2,3,4,5,6]
    """
    m=eval(input())
    output = "" # Put your line here (my solution: 9 chars)
    print(output)

    """
    H. Given a matrix m, return its transpose. 
       Example: m=[[1,2],[3,4],[5,6]], output=[[1,3,5],[2,4,6]]
    """
    m=eval(input())
    output = ""   # Put your line here (my solution: 24 chars. Hint: *m)
    print(output)
