# Mind-Game-with-Raspberry-Pi-Pico-WH
📍Project Overview
This project is a memory-based mind game built using Raspberry Pi Pico WH, 3 LEDs, 3 buttons, and an LCD screen. The game challenges players to remember and replicate a sequence of LED colors using buttons, with the difficulty increasing at each level.

🖇️Components Used
-Microcontroller: Raspberry Pi Pico WH
-LEDs: 3 (Red, Green, Blue)
-Buttons: 3 (one for each LED)
-LCD Screen: Used to display messages and game status
-Software IDE: Thonny IDE
-Programming Language: MicroPython

🎮How the Game Works
-Game Start: The game begins by selecting a random LED color.
-Level 1: The selected LED lights up. The player must press the corresponding button to proceed to the next level.
-Level 2: A second LED color is added to the sequence. The player must correctly press both buttons in the right order.
-Level 3 and Beyond: The sequence continues to grow, adding one new random color at each level.
...
🧾Game Rules:
-If the player fails to press the correct button in time, the LCD displays "Time Over", and the game resets.
-If the player presses the wrong button, the LCD displays "Game Over", and the game resets.
-If the player successfully completes all levels, the LCD displays "You Win!".
-Randomized LED sequence: Ensures a unique game experience every time.
-Real-time feedback: LCD screen displays game messages and current status.
-Incremental difficulty: Each level increases in complexity by adding a new LED color to the sequence.

🗂️Installation and Setup
-Install Thonny IDE: Download and install Thonny IDE to program Raspberry Pi Pico WH.
-Set up MicroPython: Ensure MicroPython is installed on the Raspberry Pi Pico WH.
-Connect Components: Wire the LEDs, buttons, and LCD screen to the Raspberry Pi Pico WH.
-Upload the Code: Write and run the MicroPython script in Thonny IDE.
-Start Playing: Press the start button to begin the game.
![lcd_bb](https://github.com/user-attachments/assets/bda688c2-24bd-4316-b4f7-e9917a7ecc6b)



Add sound effects for button presses and game events.

Conclusion

This mind game enhances memory and reflexes by challenging players to recall and replicate an increasing sequence of LED patterns. With its simple yet engaging gameplay, it is an excellent project for learning MicroPython and working with Raspberry Pi Pico WH.
