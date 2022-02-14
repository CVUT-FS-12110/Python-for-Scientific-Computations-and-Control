# Fun with circles

You are supposed to implement code for the function which should decide the mutual position and possible overlap of two given circles.

For your implementation use the prepared file **circles.py**. There is predefined function called **circles** which accepts two arguments **circle_1** and **circle_2**. These two arguments will be passed as **tuples** where each tuple consists of **3 values**. Respectively **x coordinate** of circle center, **y coordinate** of circle center and **radius**. 

In the predefined function write your code inside the commented block. Do not change the header or return statement of the predefined function.

The return statement of the **circles** function is a tuple of two values. Assign your results to these two values within your implementation.

There are 6 accepted results:

    1. Circles have identical coordinates and radiuses
        * message_out = 'Identical circles'
        * overlap_out is Non-zero

    2. Circles are away from each other. No contact, no overlap.
        * message_out = 'Separated circles'
        * overlap_out = 0

    3. Circles are touching each other from outside. One point of contact, no overlap.
        * message_out = 'Outer contact'
        * overlap_out = 0

    4. Circles are intersecting each other. Two points of contact.
        * message_out = 'Circle intersection'
        * overlap_out is Non-zero

    5. One circle touching the other from inside. One point of contact
        * message_out = 'Inner contact'
        * overlap_out is Non-zero

    6. One circle absorbed the other. No point of contact
        * message_out = 'Absorbed circle'
        * overlap_out is Non-zero

Your implementation of the **circles** function is supposed to detect the correct case for every pair of circles given and assign correct output values to **message_out** and **overlap_out** variables.

During implementation, you can define your own functions if you decide to.

For your implementation you may use functions **sqrt**(square root), **asin**(arcsine) and constant **pi** for exact calculations. They are already imported so you can use them without any import. Do not import anything else you don't need it.

In the prepared file, there is a block of code that consists of several **assert** statements. An assert statement checks whether a condition is true.  If a condition evaluates to True, a program will keep running. If a condition is false, the program will return an AssertionError (it is wise to check the error message). Included asserts are testing if the result of your function is correct for the given input. They should help you to find out if your function is behaving well. Your program has to go through all given asserts before it will be accepted for evaluation (so removing them won't help you). On the other hand, it might be beneficial to add a few more own asserts for specific sets of data.
