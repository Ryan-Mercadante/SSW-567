"""This module is designed to classify triangles as Right, Equilateral, Isoceles, or Scalene"""
def classify_triangle(a_side,b_side,c_side):
    """Checks if the input is valid, if it is runs check_type if not returns InvalidInput"""
    if not(isinstance(a_side,int) and isinstance(b_side,int) and isinstance(c_side,int)):
        return 'InvalidInput'
    if a_side > 200 or b_side > 200 or c_side > 200:
        return 'InvalidInput'
    if a_side <= 0 or b_side <= 0 or c_side <= 0:
        return 'InvalidInput'
    return check_type(a_side,b_side,c_side)
def check_type(a_side,b_side,c_side):
    """This function decippers the type of triangle if it is not a triangle returns NotATriangle"""
    if (a_side + b_side) >= c_side and (b_side + c_side) >= a_side and (c_side + a_side) >= b_side:
        if ((a_side ^ 2) + (b_side ^ 2)) == (c_side ^ 2):
            return 'Right'
        if a_side == b_side and b_side == c_side:
            return 'Equilateral'
        if(a_side == b_side or b_side == c_side or a_side == c_side):
            return 'Isoceles'
        return 'Scalene'
    return 'NotATriangle'
