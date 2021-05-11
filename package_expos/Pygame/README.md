# Pygame Package Expo

Presentation [here](https://www.youtube.com/watch?v=UlakTR7c-Fw)

## Pygame Background
Pygame is a set of python modules that are designed for writing video games created in 2000 by Pete Shinners..
it mixes Python and SDL or Simple DirectMedia Layer, which is a cross-platform C library for controlling multimedia and has been used commonly for commercial and open-source games.
pygame can run on almost every single platform and OS, including Linux, Windows, and MacOS. You can also use it on hand held devices and game consoles
this highly accessible library has spawned over 660 projects

## How to Initialize
We install pygame with the pip tool, which Python uses to install packages. Then we import the package to use. We also then need to initialize the pygame modules with the pygame.init(). This automatically initializes all the pygame modules that need to be initialized. We could also initialize individual modules manually by calling the specific module like pygame.mixer.init() which only initializes the module that loads and plays sounds.

Modules that are initialized come equipped with a quit() function. We don’t need to call these functions - pygame will automatically call them and clean up when pygame is exited.

```python
!pip install pygame
import pygame

pygame.init()

pygame.mixer.init()
```

## Pygame Components

### Graphical Window and Surface
Calling the function pygame.display.set_mode() creates a graphical window (which is like a monitor) and a new Surface object. Surface objects are how pygame represents images that are displayed. Any drawing we do to the Surface will become visible on the monitor.

This function also defaults to the best graphics modes for the graphics hardware that is used. users can override these modes and SDL will compensate for what the hardware cannot do.

```python
pygame.display.set_mode()

surface objects = images
```

### Images
Pygame supports a variety of image formats through the SDL_image library, including BMP, JPG, PNG, TGA, and GIF. The function pygame.image.load() takes the image data and places it on the surface. The function surface.blit() draws the images’ movement by copying pixel colors from one image source to place on a destination. Rectangles are used to represent many things in pygame from Surface objects to images to windows. They are so heavily used that a special Rect class handles them.

```python
pygame.image.load()

surface.blit()
```

### Animation
Animation is actually just a series of single images, which when displayed in sequence basically trick the human eye into seeing motion. To animate in pygame, we use an infinite loop (while loop with for loops and if statements) for when the game is initialized. It will check for user input and move the position of the surface object accordingly. We also need to erase the screen by filling it with black between the ball moving to different positions. Otherwise, there would be remnants and evidence of the object as we move positions.

```python
while:
    for:
        if:
screen.fill(black)
```

### Display
We create a Clock object with the function pygame.time.Clock() to track time and control a game’s framerate. Frames per second or FPS refers to the number of frames shown in our game per unit of time. To set the rate of frames per second, we initialize the variable FPS and set a value. We then use the clock.tick() function to specify the runtime speed of the game.

The last thing we do in creating our game is to call the method pygame.display.flip(). This updates the visible display of our screen and only allows us to see completely drawn frames.

```python
pygame.time.Clock()
clock.tick()
pygame.display.flip()
```

## Demo
```python
import sys, pygame
pygame.init()

size = width, height = 1440, 850
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60.0

#shape = pygame.image.load('/Users/brantwhite/Desktop/sampledvd.png')
shape = pygame.Surface((30,30)).convert()
shape.fill((255,0,0))
shaperect = shape.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    shaperect = shaperect.move(speed)
    if shaperect.left < 0 or shaperect.right > width:
        speed[0] = -speed[0]
    if shaperect.top < 0 or shaperect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(shape, shaperect)
    pygame.display.flip()
    clock.tick(FPS)
```

## Conclusion
1. Pygame is comprised of many modules, functions, and methods at the user’s disposal.You could create a simple, functional game in pygame with just a few hours or days’ effort. or you could spend weeks, months, years to make a sophisticated program.


2. The requirements and process to create a game in pygame make it a great exercise to hone your programming logical thinking.


3. Pygame is a free, open-source, cross-platform library available to anyone. It is constantly adapting and getting better with users being able to contribute to the project.

