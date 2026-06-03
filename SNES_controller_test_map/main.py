import pygame
import sys

pygame.init()
pygame.joystick.init()

# Check for controllers
if pygame.joystick.get_count() == 0:
    print("❌ No controller detected! Plug it in and restart the script.")
    sys.exit()

# Initialize the first controller
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"🎮 Connected to: {joystick.get_name()}")
print("---------------------------------------------")
print("Press buttons or D-pad on your iBuffalo pad.")
print("Look at the console to see their ID numbers!")
print("Press ESCAPE on your keyboard to exit.")
print("---------------------------------------------")

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("iBuffalo Mapper Tool")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check Keyboard Exit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # 1. Check Button Presses (A, B, X, Y, L, R, Select, Start)
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"🟢 Button {event.button} PRESSED")

        if event.type == pygame.JOYBUTTONUP:
            print(f"🔴 Button {event.button} RELEASED")

        # 2. Check D-Pad Movements (Axes)
        if event.type == pygame.JOYAXISMOTION:
            # Filter out tiny accidental movements (deadzone)
            if abs(event.value) > 0.5:
                print(f"🕹️ Axis {event.axis} moved to {event.value:.2f}")

        # 3. Check D-Pad Movements (if your OS reads it as a Hat instead)
        if event.type == pygame.JOYHATMOTION:
            print(f"🎩 Hat {event.hat} moved to {event.value}")

    screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(60)