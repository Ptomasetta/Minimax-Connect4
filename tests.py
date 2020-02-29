
"""Test boards for Connect4

Place test boards in this module to help test your code.  Note that ince connect4.GameState
stores board contents as a 0-based list of lists, these boards are reversed to they can be written
right side up here.
"""


board1 = list(reversed([ [  0,  0,  0,  0,  0,  0,  0 ],  # You should modify these!
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  1, -1,  0,  0,  0,  0,  0 ],
                    [  1, -1,  0,  0,  0,  0,  0 ],
                    [  1, -1,  0,  0,  0,  0,  0 ] ]))

board2 = list(reversed([ [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0, -1, -1, -1,  0,  0 ],
                    [  0,  0,  1,  1,  1,  0,  0 ] ]))

board3 = list(reversed([ [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  1, -1,  1,  0,  0 ] ]))

board4 = list(reversed([ [  0,  0,  0,  0,  0,  0,  0 ],
                    [  -1,  -1,  1,  1,  0,  -1,  -1 ],
                    [  -1,  1,  1,  -1,  1,  1,  -1 ],
                    [  1,  -1,  1,  1,  -1,  -1,  -1 ],
                    [  -1,  1,  -1,  1,  1,  -1,  1 ],
                    [  1,  1,  -1, 1,  -1,  -1,  1 ] ]))

board5 = list(reversed([ [  0,  0,  0,  0,  0,  0,  0 ],
                    [  0,  0,  0,  0,  0,  0,  -1 ],
                    [  -1,  0,  1,  0,  1,  0,  -1 ],
                    [  1,  -1,  1,  1,  -1,  -1,  -1 ],
                    [  -1,  1,  -1,  1,  1,  -1,  1 ],
                    [  1,  1,  -1, 1,  -1,  -1,  1 ] ]))


