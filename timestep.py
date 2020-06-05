"""
Samuel Hohenshell
06/04/2020
"""

# Calculating what the grid will do after one time step
def inc_time(grid, n):
    # Making an updated grid to add changes to
    # This is necessary so that we can keep changes seperate at each time step
    # Could possibly take this out if its taking too long?
    updated_grid = [[False for i in range(n)] for j in range(n)]

    # Going through each cell on the grid
    for r in range(n):
        for c in range(n):

            """
            NOTE: DO I NOT HAVE TO CHECK EDGE CASES? DO WE HAVE TO ESSENTIALLY
            HAVE AN INFINITE BOARD AND ONLY DRAW A SECTION??? I DON'T THINK SO
            BUT KEEP THIS IN MIND!!
            """
            # Calculating number of live neighbors
            live_neighbors = 0
            # Check above-left
            if ((r-1 >= 0) and (c-1 >= 0)): 
                if grid[r-1][c-1]:
                    live_neighbors += 1
            # Check above
            if (r-1 >= 0):
                if grid[r-1][c]:
                    live_neighbors += 1
            # Check above-right
            if ((r-1 >= 0) and (c+1 <= n-1)):
                if grid[r-1][c+1]:
                    live_neighbors += 1
            # Check left
            if (c-1 >= 0):
                if grid[r][c-1]:
                    live_neighbors += 1
            # Check right
            if (c+1 <= n-1):
                if grid[r][c+1]:
                    live_neighbors += 1
            # Check bottom-left
            if ((r+1 <= n-1) and (c-1 >= 0)):
                if grid[r+1][c-1]:
                    live_neighbors += 1
            # Check bottom
            if (r+1 <= n-1):
                if grid[r+1][c]:
                    live_neighbors += 1
            # Check bottom right
            if ((r+1 <= n-1) and (c+1 <= n-1)):
                if grid[r+1][c+1]:
                    live_neighbors += 1

            # Deciding state of this cell in next time step
            # If cell is alive
            if grid[r][c]:
                if (live_neighbors < 2):
                    updated_grid[r][c] = False
                elif ((live_neighbors == 2) or (live_neighbors == 3)):
                    updated_grid[r][c] = True
                else:
                    updated_grid[r][c] = False
            # If cell is dead
            else:
                if (live_neighbors == 3):
                    updated_grid[r][c] = True
                else:
                    updated_grid[r][c] = False

    # Return the fully updated grid after going through each cell
    return updated_grid

