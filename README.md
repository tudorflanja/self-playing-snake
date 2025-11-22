# 🐍 Self-Playing Snake AI (Python + Pygame)

This project implements an **autonomous Snake game agent** built using **Python** and **Pygame**.  
Instead of human input, the snake is controlled by a series of **incrementally designed AI behaviors** that allow it to:

- track food  
- avoid collisions with itself  
- choose safe turns  
- evaluate the safest direction to continue  

This game demonstrates **reactive agent behavior**, **grid-based path reasoning**, and basic **environmental sensing** in a dynamic environment.

---

## 🚀 Features

- 🤖 **Fully Autonomous Snake AI** – No keyboard input required; the snake makes all movement decisions  
- 🎯 **Food Tracking Logic** – Snake computes relative distance and pursues food efficiently  
- 🧱 **Self-Collision Avoidance** – Prevents the snake from turning into its own body  
- 🔄 **Predictive Turning** – Detects imminent collisions and turns away before impact  
- 🧠 **Gap Evaluation Algorithm** – Measures available space in all directions and chooses the safest turn strategy  
- 🎮 **Classic Snake Mechanics** – Growth on food, score counter, and smooth frame-based movement  
- 🌈 **Grid Rendering with Pygame** – Visual checkerboard board for readability  

---

## 🧰 Technologies Used

- **Python 3.x** – Main programming language  
- **Pygame** – Game window, graphics rendering, keyboard events  
- **Random module** – Food spawning and initial direction  
- **Modular OOP Architecture** – `Snake`, `Food`, and grid logic classes  

---

## 🛠️ AI Behavior Overview

The AI is built in **four incremental stages**, matching the development documented in the project.

### 1. **Tracking the Food**  
The snake calculates a `(dx, dy)` vector representing its head’s distance to the food and moves in the direction that minimizes this distance.  
This is the foundational pursuit strategy.

---

### 2. **Prevent Turning Into Itself**  
Before turning, the snake checks whether the next tile in the new direction is part of its body.  
It only turns if the move is safe, improving survivability.

---

### 3. **Turn Away Before Collision**  
The snake predicts collisions by inspecting the tile it is *about to* enter based on its current direction.  
If occupied, a `colliding` flag is set (`up`, `down`, `left`, `right`), and the snake immediately turns away to survive.

---

### 4. **Choosing the Best Turn (Gap-Based Logic)**  
For each direction, the snake scans how many free tiles (gaps) exist until it hits its own body.  
It then selects the turn with the **largest available gap**, improving long-term survival and reducing trapping situations.

---

## 💻 How It Works

1. The game starts with a **1-segment snake** positioned in the center.  
2. The AI computes:
   - head position  
   - food position  
   - distance vector `(dx, dy)`  
   - collision state  
   - available gaps in all directions  
3. Based on these factors, the snake autonomously chooses:
   - continue straight  
   - turn left  
   - turn right  
   - move up/down  
4. When food is eaten:
   - the snake grows  
   - score increases  
   - food respawns at a random grid location  
5. The game loop refreshes at a constant 15 FPS, ensuring smooth behavior.

---

## 📂 Project Structure

- `main.py` – Full implementation of the Snake game and AI logic  
- `Snake` class – Handles movement, collision prediction, direction decisions  
- `Food` class – Random food spawning and rendering  
- `drawGrid()` – Renders checkerboard game board  
- `README.md` – Project documentation

---

## ▶️ How to Run the Project

### **Option 1 — Run in VS Code**

1. Install **Python 3.x**
2. Install **Pygame**:

        pip install pygame

3. Open the folder containing `main.py` in VS Code
4. Run the file:

        python main.py


---

### Option 2 — Run from Terminal

1. Install Pygame:

        pip install pygame

2. Run the project:

        python main.py


A new window will open, and the AI snake will begin playing autonomously.


---

## 🧠 Key Concepts Demonstrated

- Autonomous movement in a dynamic environment  
- Collision prediction & avoidance  
- Spatial reasoning across a grid  
- Multi-stage decision-making  
- Real-time Pygame rendering  
- Object-oriented programming in game design  

---

## 📝 Conclusion

The Self-Playing Snake AI showcases how simple rule-based logic and grid analysis can produce believable autonomous behavior.  
Through incremental improvements—food tracking, collision prevention, predictive turning, and gap analysis—the snake evolves from a naive agent to a more robust survivor.

This project demonstrates foundational ideas relevant to:

- 🤖 AI agent design  
- 🧠 Pathfinding strategies (introductory level)  
- 🎮 Game development  
- 🐍 Python OOP and Pygame  

Feel free to modify and extend the AI logic with new strategies, heuristics, or even full-fledged pathfinding algorithms!

---

This project was created in collaboration with Dobre Mircea for the Artificial Intelligence course at the Technical University of Cluj-Napoca (UTCN) 🎓.
