def escapeGhosts(ghosts: list[list[int]], target: list[int]) -> bool:
    my_distance = abs(target[0]) + abs(target[1])

    ghosts_distances = [abs(cords[0] - target[0]) + abs(cords[1] - target[1]) for cords in ghosts]
    ghosts_distances = min(ghosts_distances)

    if my_distance < ghosts_distances:
        return True
    else:
        return False
    

print(escapeGhosts(ghosts = [[1,0]], target = [2,0]))