# maze is represented in a matrix
grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]




def find_path_for_maze_recursive(maze_grid: [[int]], starting_position_x: int, starting_position_y: int ) -> [[int]], bool:
    """Function that find a path for maze
    
    function will modify a int matrix to add 'x' as the path
    Args:
        maze_grid([[int]]): a matrix like
                [[0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1],
                [0, 0, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 1],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 2]]
                #0, means path, 1, means wall, and 2 mean ending
        starting_position_x(int): starting x axis of position
        starting_position_y(int): starting y axis of position

    Returns:
        [[int]], a matrix on top of maze_grid that an "x" means path it took
        bool: boolean to indicate if a solution is found
    """

    if maze_grid[starting_position_y][starting_position_x] == 2:
        #found exit
        maze_grid[starting_position_y][starting_position_x] = 'x'
        return maze_grid, True

