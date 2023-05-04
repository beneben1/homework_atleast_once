def pick_color():
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]
    print("Please select a color:")
    for i in range(len(colors)):
        print(f"{i+1}. {colors[i]}")
    color_choice = input("Enter the number of the color you would like to select: ")
    if not color_choice:
        print("No color selected.")
        return None
    color_choice = int(color_choice)
    if color_choice < 1 or color_choice > len(colors):
        print("Invalid selection. Please try again.")
        return pick_color()
    else:
        return colors[color_choice-1]


def pick_number():
    color_choice = pick_color()
    if color_choice is None:
        return pick_number()  # Return to color pick option
    print(f"Please select a number between 1 and 10 for {color_choice}:")
    number_choice = int(input("Enter your number choice: "))
    if number_choice < 1 or number_choice > 10:
        print("Invalid selection. Please try again.")
        return pick_number()
    else:
        print(f"You selected the number {number_choice}")


pick_number()


color_choice = pick_color()
print(f"You selected the color {color_choice}")

number_choice = pick_number(color_choice)
if number_choice is not None:
    print(f"You selected the number {number_choice}")