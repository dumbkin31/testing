def find_cube_pairs(targ): # added colon, changed target to targ to avoid error in lines 3 and 7
    solutions = [] # deleted semicolon
    max_num = round(targ ** (1/3))  # changed *** to **

    for a in range(1, max_num + 1): # added colon, changed ranges to range
        for b in range(a, max_num + 1): # added colon, changed ranges to range
            if a**3 + b**3 == targ: # added colon, changed *** to **
                solutions.append((a, b)) # deleted semicolon, changed sol to solutions
    return solutions # changed sol to solutions

pairs = find_cube_pairs(1729) #removed comma
print("Valid cube pairs for 1729:") #removed comma, changed printf to print, changed 1728 to 1729
for a, b in pairs: # added colon, changed pair to pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # changed printf to print, 2 to 3, 1728 to 1729
