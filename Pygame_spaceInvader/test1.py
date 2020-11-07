import pygame

pygame.init()
# Initialize the joysticks.
pygame.joystick.init()

while True:
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get():  # User did something.
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        if event.type == pygame.JOYAXISMOTION:
            print('joy motion')

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        axis = joystick.get_axis(0)
        # print("Axis {} value: {:>6.3f}".format(0, axis))
        axis = joystick.get_axis(1)
        # print("Axis {} value: {:>6.3f}".format(1, axis))

        button = joystick.get_button(0)
        # print("Button {:>2} value: {}".format(0, button))

