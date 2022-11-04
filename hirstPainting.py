#import colorgram
import turtle as turtle_module
import random
#rgb_colors = []
#colors = colorgram.extract('images.jpg', 30)
#for color in colors:
 #   r = color.rgb.r
  #  g = color.rgb.g
   # b = color.rgb.b
    #new_color = (r, g, b)
    #rgb_colors.append(new_color)

#print(rgb_colors)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.penup()
color_list = [(53, 243, 235), (81, 162, 234), (67, 103, 239), (73, 234, 243), (32, 172, 156), (26, 102, 199),
              (32, 129, 119), (173, 176, 233)]

tim.setheading(220)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.penup()

screen = turtle_module.Screen()
screen.exitonclick()
