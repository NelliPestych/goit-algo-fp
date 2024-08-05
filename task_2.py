import turtle

def draw_pythagoras_tree(length, level):
    if level == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    # Draw the main branch
    turtle.forward(length)

    # Draw the left branch
    turtle.left(45)
    draw_pythagoras_tree(length * 0.7, level - 1)

    # Move to the right branch position
    turtle.right(90)
    draw_pythagoras_tree(length * 0.7, level - 1)

    # Return to the original position
    turtle.left(45)
    turtle.backward(length)

def main():
    turtle.speed(0)
    turtle.left(90)  # Start facing upwards
    turtle.up()
    turtle.backward(200)
    turtle.down()

    # Введення рівня рекурсії користувачем
    level = int(input("Введіть рівень рекурсії: "))

    draw_pythagoras_tree(100, level)
    turtle.done()

if __name__ == "__main__":
    main()
