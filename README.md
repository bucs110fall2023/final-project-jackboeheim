[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13227157&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Raycasting Algorithm
## CS110 Final Project  Fall 2023

## Team Members

Jack Boeheim

***

## Project Description

My project is a 3D raycasting algorithm similar to the algorithm used in early 3D games like Wolfenstein 3D and the original DOOM game. 

***    

## GUI Design

### Initial Design

(Because this algorithm is unorignal, I attached an image from another programmer, which served as an inspiration)

![image](https://github.com/bucs110fall2023/final-project-jackboeheim/assets/143842028/6e22b981-487d-4443-8678-0648e44fb923)

### Final Design

<img width="797" alt="image" src="https://github.com/bucs110fall2023/final-project-jackboeheim/assets/143842028/5ead2b0e-3af0-4f87-a589-f57bf89bb20d">


## Program Design

### Features

1. This program allows the user to walk forward and backward and look left and right
2. The program saves the user's data automatically every frame, so whenever the program is launched, the player is in the same position and facing the same direction
3. The program features collision detection, disallowing the user from walking into walls
4. Wall colors can easily be modified in the code and currently 3 different color walls are present
5. Walls are shaded depending upon what face of the wall is being looked at

### Classes

Controller Class:
The controller class contains all of the player data and derivative members of that data. The controller class contains the main while loop and event loop and creates a model class in the run method. The controller class handles user inputs to rotate or move. The controller class updates the save file and overwrites its own data at launch with save data.

Model Class:
The model class's only data is the instance of player, the Controller class, and a screens surface which it defines. The Model class draws the floor and ceiling and performs the raycasting algorithm drawing in all walls appropriately shaded and colored.

## ATP


