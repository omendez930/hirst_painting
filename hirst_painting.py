import random
from turtle import Turtle, Screen
import colorgram
import random

t= Turtle()
s = Screen()
s.colormode(255)
t.speed(0)
t.penup()
t.ht()
# def color_extraction():
#     """Extracts RGB colors from an image"""
#     colors = colorgram.extract('image.jpg',40)
#     print(colors)
#     print(colors[1].rgb)
#     rgb_colors = []
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#
#     return rgb_colors

color_list = [(252, 251, 244), (254, 247, 252), (241, 253, 246), (245, 248, 253), (245, 235, 46), (195, 12, 34), (220, 160, 71), (42, 80, 177), (237, 40, 138), (32, 40, 156), (238, 229, 5), (40, 215, 69), (21, 150, 23), (209, 73, 21), (204, 32, 96), (66, 10, 28), (217, 163, 11), (218, 137, 191), (189, 15, 9), (55, 15, 10), (77, 211, 153), (68, 72, 221), (86, 189, 222), (14, 94, 64), (237, 158, 213), (99, 234, 198), (20, 20, 51), (216, 87, 52), (4, 229, 240), (14, 68, 46), (173, 177, 235), (89, 229, 238), (241, 168, 158), (4, 245, 232), (250, 7, 52), (28, 52, 233), (11, 91, 110)]

# for i in color_list:
#     print(i)
#t.goto(50,100)
t.setpos(-280,-230)
# print(s.screensize())
num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    t.penup()
    t.dot(20,random.choice(color_list))
    t.forward(10)
    t.forward(50)
    if dot_count % 10 == 0:
        t.penup()
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(600)
        t.right(180)

s.exitonclick()
