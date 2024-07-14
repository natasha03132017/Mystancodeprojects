"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + ((width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # left line
    canvas.create_line(GRAPH_MARGIN_SIZE, 0,
                       GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    for year_index, year in enumerate(YEARS):
        canvas_x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(canvas_x, 0,
                           canvas_x, CANVAS_HEIGHT)
        canvas.create_text(int(canvas_x), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=year, anchor=tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for name_index, name in enumerate(lookup_names):
        canvas_xy_list, rank_list = [], []
        for year_index, year in enumerate(YEARS):
            # x coordinate
            canvas_x = get_x_coordinate(CANVAS_WIDTH, year_index)
            if str(year) in name_data[name]:
                # y coordinate
                canvas_y = GRAPH_MARGIN_SIZE + (int(name_data[name][str(year)]) - 1) * \
                           (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
                rank_txt = str(name_data[name][str(year)])
            else:
                # y coordinate
                canvas_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank_txt = '*'

            canvas_xy_list.append(canvas_x)
            canvas_xy_list.append(canvas_y)
            rank_list.append(rank_txt)
            color_index = name_index % len(COLORS)

            # add the name and the rank
            canvas.create_text(canvas_x + TEXT_DX, canvas_y,
                               text=name + ' ' + rank_txt, anchor=tkinter.SW, fill=COLORS[color_index])
        # plot the curve
        canvas.create_line(canvas_xy_list, fill=COLORS[color_index], width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
