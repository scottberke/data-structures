# O(2^n)
def solve_tower_of_hanoi(discs, start, temp, end):
    # If we've got no discs to move just return
    if discs == 0:
        return

    # Move all but one disc to the temp tower
    solve_tower_of_hanoi(discs - 1, start, end, temp)
    # Move the last disc to the end tower
    move(start, end)
    # Move all discs from temp to end tower
    solve_tower_of_hanoi(discs - 1, temp, start, end)

# O(1)
def move(start, end):
    # Grab top disc to move
    disc = start.pop()
    txt = "Moving " + str(disc) + " From " + start.name + " To " + end.name
    print(txt)
    # Append to destination tower
    end.append(disc)
    return
