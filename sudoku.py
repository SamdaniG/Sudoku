#A humble attempt to create a Sudoku Solver 
"""
Let's lay down ground rules of understanding the sudoku syntax
We shall follow the matrix rule of using rows X columns, and A-I for boxes
It should look something like this

    1   2    3   4   5   6   7   8   9  
    A11	A12	A13	B14	B15	B16	C17	C18	C19 1
    A21	A22	A23	B24	B25	B26	C27	C28	C29 2
    A31	A32	A33	B34	B35	B36	C37	C38	C39 3   
    D41	D42	D43	E44	E45	E46	F47	F48	F49 4
    D51	D52	D53	E54	E55	E56	F57	F58	F59 5   
    D61	D62	D63	E64	E65	E66	F67	F68	F69 6
    G71	G72	G73	H74	H75	H76	I77	I78	I79 7
    G81	G82	G83	H84	H85	H86	I87	I88	I89 8   
    G91	G92	G93	H94	H95	H96	I97	I98	I99 9


"""

#Here we have to initialize all the values to zero, writing them down takes time
a11, a12, a13, b14, b15, b16, c17, c18, c19 = 0, 0, 0, 0, 0, 0, 0, 0, 0
a21, a22, a23, b24, b25, b26, c27, c28, c29 = 0, 0, 0, 0, 0, 0, 0, 0, 0
a31, a32, a33, b34, b35, b36, c37, c38, c39 = 0, 0, 0, 0, 0, 0, 0, 0, 0 
d41, d42, d43, e44, e45, e46, f47, f48, f49 = 0, 0, 0, 0, 0, 0, 0, 0, 0
d51, d52, d53, e54, e55, e56, f57, f58, f59 = 0, 0, 0, 0, 0, 0, 0, 0, 0
d61, d62, d63, e64, e65, e66, f67, f68, f69 = 0, 0, 0, 0, 0, 0, 0, 0, 0
g71, g72, g73, h74, h75, h76, i77, i78, i79 = 0, 0, 0, 0, 0, 0, 0, 0, 0
g81, g82, g83, h84, h85, h86, i87, i88, i89 = 0, 0, 0, 0, 0, 0, 0, 0, 0
g91, g92, g93, h94, h95, h96, i97, i98, i99 = 0, 0, 0, 0, 0, 0, 0, 0, 0

# Creating sets
box_a={a11,a12,a13,a21,a22,a23,a31,a32,a33}
box_b={b14,b15,b16,b24,b25,b26,b34,b35,b36}
box_c={c17, c18, c19, c27, c28, c29, c37, c38, c39}