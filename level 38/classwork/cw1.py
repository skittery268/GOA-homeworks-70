# 1) https://www.codewars.com/kata/551b4501ac0447318f0009cd

# დავალება: 
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

# შესრულებული დავალება:
def boolean_to_string(b):
    if int(b) == 1:
        return "True"
    else:
        return "False"