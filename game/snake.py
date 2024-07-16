import random
import curses

def create_food(snake, screen_height, screen_width):
    while True:
        food = [random.randint(1, screen_height-2), random.randint(1, screen_width-2)]
        if food not in snake:
            return food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    screen_height, screen_width = stdscr.getmaxyx()
    snake_x = screen_width // 4
    snake_y = screen_height // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    direction = curses.KEY_RIGHT
    food = create_food(snake, screen_height, screen_width)
    
    stdscr.addch(food[0], food[1], curses.ACS_PI)
    
    while True:
        next_key = stdscr.getch()
        direction = direction if next_key == -1 else next_key
        
        if direction == curses.KEY_DOWN:
            new_head = [snake[0][0] + 1, snake[0][1]]
        elif direction == curses.KEY_UP:
            new_head = [snake[0][0] - 1, snake[0][1]]
        elif direction == curses.KEY_LEFT:
            new_head = [snake[0][0], snake[0][1] - 1]
        elif direction == curses.KEY_RIGHT:
            new_head = [snake[0][0], snake[0][1] + 1]
        
        snake.insert(0, new_head)
        
        if snake[0] == food:
            food = create_food(snake, screen_height, screen_width)
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')
        
        if (snake[0][0] in [0, screen_height] or
            snake[0][1] in [0, screen_width] or
            snake[0] in snake[1:]):
            stdscr.addstr(screen_height//2, screen_width//2 - 5, "Game Over")
            stdscr.refresh()
            stdscr.nodelay(0)
            stdscr.getch()
            break
        
        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

curses.wrapper(main)
