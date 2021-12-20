# Import modules
from graphics import *
from scenarios import *
from major_reqs import *
import math
    


def presentScenario(scen_x, win_x, img):
  """Apply similar features to all scenarios.

  Keyword arguments:
  scen_x -- the scenario number
  win_x -- the window number
  img -- the scenario image to be shown in the graphics window
  """
  # Import image for scenario x
  scenario_image = Image(Point(400,280), img)
  scenario_image.draw(win_x)  

  # Add scenario title inside scenario 1 window
  s_title = Text(Point(400,47), scen_x.name + ":\n" + scen_x.title) 
  # scen_x.name is a new attribute in scenario.py
  print() 
  s_title.setSize(27)
  s_title.setFace('courier')
  s_title.draw(win_x)

  # Make buttons for three choices : like/neutral/dislike
  rectangle1 = Rectangle(Point(70,480), Point(270,580))
  rectangle1.setFill("#659EC7") # columbia blue
  rectangle1.draw(win_x)
  rectangle1_text = Text(Point(170,530), scen_x.like)
  rectangle1_text.setSize(12)
  rectangle1_text.draw(win_x)

  rectangle2 = Rectangle(Point(300,480), Point (500,580))
  rectangle2.setFill("#FFDB58") # mustard color
  rectangle2.draw(win_x)
  rectangle2_text = Text(Point(400,530), scen_x.neutral)
  rectangle2_text.setSize(12)
  rectangle2_text.draw(win_x)

  rectangle3 = Rectangle(Point(530,480), Point (730,580))
  rectangle3.setFill("#DC381F") # grapefruit color
  rectangle3.draw(win_x)
  rectangle3_text = Text(Point(630,530), scen_x.dislike)
  rectangle3_text.setSize(12)
  rectangle3_text.draw(win_x)

  # Print scenario x on the console
  # Title
  print("\u001b[33;1m\033[1m" + "---------- {}: {} ----------".format(scen_x.name, scen_x.title) + "\u001b[0m\033[0m")
  print() 
  # Description
  print(scen_x.description) 
  print()
  # Question
  print("\u001b[32m\033[1m" + scen_x.question + "\u001b[0m\033[0m") 
  # Options
  print(scen_x.like.replace("\n", " ") + "\n" + scen_x.neutral.replace("\n", " ") + "\n" + scen_x.dislike.replace("\n", " ")) 



def finalCounter():
  """Find the best match major by calculating the greatest counter value."""
  # Create a list for the majors
  majors = ["Astronomy", "Biochemistry", "Biological Sciences", "Chemistry", "Computer Science", "Engineering Science", "Environmental Science and Policy", "Geosciences", "Mathematics & Statistics", "Neuroscience", "Physics", "Statistical and Data Sciences"]

  # Create a list for the major counters
  counters = [astro_counter, biochem_counter, bio_counter, chem_counter, csc_counter, egr_counter, esp_counter, geo_counter, mth_counter, nsc_counter, phy_counter, sds_counter]
  
  # Create a global dictionary of the majors
  global major_dict
  major_dict = {}
  # Combine the majors with their counters using zip
  for major, counter in zip(majors, counters):
    major_dict[major] = counter

  # Create a global variable to hold the greatest counter value
  global greatest_value
  greatest_value = 0
  # Sort through the dictionary to find the greatest value
  for major, counter in major_dict.items():
    if counter > greatest_value:
      greatest_value = counter

  # Create a global variable to hold the major with the greatest counter
  global best_match_major
  best_match_major = ""
  # Sort through the dictionary to find that major
  for major, counter in major_dict.items():
    if counter == greatest_value:
      best_match_major = major

  # Return both variables to be used in the results section
  return best_match_major, greatest_value



def confirmAnswer(win_x, key):
  """Confirm the user's answer by having them enter it again.

  Keyword arguments:
  win_x -- the window number
  key -- the first key the user entered
  """
  # If the user does not enter left, right, or down key then ask user to try again
  incorrect_key = True
  while incorrect_key == True:
    while key not in ['Left', 'Right', 'Down']:
      print(wrong_key_message) # String is in descriptions.py
      key = win_x.getKey()
      print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

    # When the user presses one of the correct keys, they are asked to confirm their decision by pressing the key again or choosing a new one.
    print(confirmation_key_message)
    key = win_x.getKey()
    print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

    # If they choose a correct key, the while loop is exited and the quiz continues.
    if key in ['Left', 'Right', 'Down']:
      incorrect_key = False



def playGame():
  """Run the main game."""
  # Initialize the counters
  # Astronomy
  global astro_counter 
  astro_counter = 0
  # Biochemistry
  global biochem_counter 
  biochem_counter = 0
  # Biological Sciences
  global bio_counter 
  bio_counter = 0
  # Chemistry
  global chem_counter 
  chem_counter = 0
  # Computer Science
  global csc_counter 
  csc_counter = 0
  # Engineering Sciences
  global egr_counter 
  egr_counter = 0
  # Environmental Science & Policy
  global esp_counter 
  esp_counter = 0
  # Geosciences
  global geo_counter 
  geo_counter = 0
  # Mathematics & Statistics
  global mth_counter 
  mth_counter = 0
  # Neuroscience
  global nsc_counter
  nsc_counter = 0
  # Physics
  global phy_counter 
  phy_counter = 0
  # Statistical & Data Sciences
  global sds_counter 
  sds_counter = 0

#=====================================================================
  # Start window

  # Text art to start the game
  print("""
  █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀█ █░█ █▀█ 
  ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▄█ █▄█ █▀▄

  █▀ ▀█▀ █▀▀ █▀▄▀█   █▀▄▀█ ▄▀█ ░░█ █▀█ █▀█   █▀▀ ▄▀█ █▀▄▀█ █▀▀
  ▄█ ░█░ ██▄ █░▀░█   █░▀░█ █▀█ █▄█ █▄█ █▀▄   █▄█ █▀█ █░▀░█ ██▄\n""")

  # Create start window
  win0 = GraphWin("STEM MAJOR GAME", 800, 600)
  win0.setBackground('white')

  # Draw a circle for the Play button
  circ = Circle(Point(400, 350), 150)
  circ.setFill('black')
  circ.setOutline('white')
  circ.draw(win0)

  # Import image for the background 
  background1 = Image(Point(400,350), "images/stem.png")
  background1.draw(win0)

  # Draw a triangle for the Play button
  triangle = Polygon(Point(350, 250), Point(350, 450), Point (500, 350))
  triangle.setFill('white')
  triangle.setOutline('white')
  triangle.draw(win0)
  
  # Draw the text in the graphics window
  title = Text(Point(400,70),'STEM-MAJOR EXPLORATION QUIZ')
  title.setSize(22)
  title.setFace('courier')
  subtitle1 = Text(Point(400,100), '(At Smith College)')
  subtitle1.setSize(17)
  subtitle1.setFace('courier')
  subtitle2 = Text(Point(400, 130), 'Click to Play!')
  subtitle2.setSize(14)
  subtitle2.setStyle('bold')
  subtitle2.setFace('courier')
  subtitle2.setFill('#3B9C9C')
  start_text = Text(Point(400, 550), 'START')
  start_text.setStyle('bold')
  start_text.setSize(17)
  start_text.setFace('courier')
  title.draw(win0)
  subtitle1.draw(win0)
  subtitle2.draw(win0)
  start_text.draw(win0) 
  
  # Get the point where the mouse clicks on
  pt1 = win0.getMouse()
  # Get the distance between pt1 and circ using the distance formula
  dx = pt1.getX() - circ.getCenter().getX()
  dy = pt1.getY() - circ.getCenter().getY()
  dist = math.sqrt(dx*dx + dy*dy)

  # If the mouse click isn't in the circle, get it again
  while dist >= circ.getRadius():
    # Get the point where the mouse clicks on again
    pt1 = win0.getMouse()
    # Get the distance between pt1 and circ using the distance formula
    dx = pt1.getX() - circ.getCenter().getX()
    dy = pt1.getY() - circ.getCenter().getY()
    dist = math.sqrt(dx*dx + dy*dy)

  # If the user clicks within the circle, close the window
  win0.close()  

#====================================================================  
  # Introduction

  # Create intro window 1
  print("\u001b[36m\033[1m---------- INTRODUCTION ----------\u001b[0m \033[0m\n\n(Left-click to continue)")
  win_intro = GraphWin("Introduction", 800, 600)
  win_intro.setBackground('white')

  # Import images for intro window 1

  intro_bg = Image(Point(400,300), "images/Smith.png")
  intro_bg.draw(win_intro)

  student = Image(Point(250,420), "images/student.png")
  student.draw(win_intro)


  # Draw a textbox & text
  textbox = Rectangle(Point(0, 500), Point (800, 600))
  textbox.setFill('white')
  textbox.setOutline('black')
  textbox.draw(win_intro)

  student_text = Text(Point(400,550),'Advisees: Hello! We are your Advisees this school year.\n We know that we are interested in STEM, but we’re not sure \n which STEM field(s) to major in.') 

  student_text.setSize(15)
  student_text.setFace('courier')
  student_text.setStyle('bold')
  student_text.setFill('black')
  student_text.draw(win_intro)


  win_intro.getMouse()

  # New image & textbox & text appears after a mouse click
  teacher = Image(Point(620,380), "images/teacher.png")
  teacher.draw(win_intro)
  
  textbox2 = Rectangle(Point(0, 500), Point (800, 600))
  textbox2.setFill('white')
  textbox2.setOutline('black')
  textbox2.draw(win_intro)

  teacher_text = Text(Point(400,550),'Adviser: Not a Worry! \nWe’ll walk you through several activities to explore STEM \nhere at Smith. Let’s go!')

  teacher_text.setSize(15)
  teacher_text.setFace('courier')
  teacher_text.setStyle('bold')
  teacher_text.setFill('black')
  teacher_text.draw(win_intro)

  print("(Another left-click to get to the scenarios!)\n")
 
  # Click to close intro window
  win_intro.getMouse()
  win_intro.close()
  
#=====================================================================

  # Scenario 1

  # Create an object for scenario 1 
  s1 = Scenario1() 

  # Create scenario 1 window
  win1 = GraphWin("Scenario 1", 800, 600)
  win1.setBackground('white')
  
  # Present the scenario 1
  presentScenario(s1, win1, "images/rocket.png")

  # Note down the user's keypress, and the user know which key they press
  key = win1.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win1, key)

  # Add points to the corresponding counters based on the option chosen by user  
  if key == "Left": # like
  # POSITION ON GRAPH WOULD BE LEFT 
    astro_counter += 2.5
    phy_counter += 3
    egr_counter += 3
  elif key == "Down": # neutral
  # POSITION COORDINATES CENTER 
    astro_counter += 1.25
    phy_counter += 2
    egr_counter += 2
  elif key == "Right": # dislike
  # POSITION COORDINATES TO THE RIGHT 
    astro_counter += -2.5
    phy_counter += -3
    egr_counter += -3

  # Close scenario 1 window
  win1.close()
  print()

#=====================================================================
 
  # Scenario 2

  # Create an object for scenario 2 
  s2 = Scenario2()

  # Create scenario 2 window
  win2 = GraphWin("Scenario 2", 800, 600)
  win2.setBackground('white')

  # Present the scenario 2
  presentScenario(s2, win2, "images/aspirin.png")

  # Note down the user's keypress, and the user know which key they press
  key = win2.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win2, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    chem_counter += 3
    mth_counter += 1
  elif key == "Down": # POSITION COORDINATES CENTER
    chem_counter += 2
    mth_counter += 0.5
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    chem_counter += -3
    mth_counter += -1

  # Close scenario 2 window
  win2.close()
  print() 

#=====================================================================

  # Scenario 3

  # Create an object for scenario 3 
  s3 = Scenario3()

  # Create scenario 3 window
  win3 = GraphWin("Scenario 3", 800, 600)
  win3.setBackground('white')

  # Present the scenario 3
  presentScenario(s3, win3, "images/coweye.png")

  # Note down the user's keypress, and the user know which key they press
  key = win3.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win3, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    bio_counter += 3
    nsc_counter += 2
  elif key == "Down": # POSITION COORDINATES CENTER
    bio_counter += 2
    nsc_counter += 1
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    bio_counter += -3
    nsc_counter += -2

  # Close scenario 3 window
  win3.close()
  print() 

#==================================================================== 

  # Scenario 4

  # Create an object for scenario 4 
  s4 = Scenario4()

  # Create scenario 4 window
  win4 = GraphWin("Scenario 4", 800, 600)
  win4.setBackground('white')

  # Present the scenario 4
  presentScenario(s4, win4, "images/python_code.png")

  # Note down the user's keypress, and the user know which key they press
  key = win4.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win4, key)

  # Add points to the corresponding counters based on the option chosen by user 
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    csc_counter += 5
  elif key == "Down": # POSITION COORDINATES CENTER
    csc_counter += 3
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    csc_counter += -5

  # Close scenario 4 window
  win4.close()
  print() 
  
#=====================================================================

  # Scenario 5

  # Create an object for scenario 5 
  s5 = Scenario5()  

  # Create scenario 5 window
  win5 = GraphWin("Scenario 5", 800, 600)
  win5.setBackground('white')

  # Present the scenario 5
  presentScenario(s5, win5, "images/climate.png")

  # Note down the user's keypress, and the user know which key they press
  key = win5.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win5, key)
  
  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    bio_counter += 3
    esp_counter += 3
    geo_counter += 3
  elif key == "Down": # POSITION COORDINATES CENTER
    bio_counter += 1.5
    esp_counter += 1.5
    geo_counter += 1.5
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    bio_counter += -3
    esp_counter += -3
    geo_counter += -3

  # Close scenario 5 window
  win5.close()
  print() 

#===================================================================== 
  # Scenario 6

  # Create an object for scenario 6 
  s6 = Scenario6()
  
  # Create scenario 6 window
  win6 = GraphWin("Scenario 6", 800, 600)
  win6.setBackground('white')

  # Present the scenario 6
  presentScenario(s6, win6, "images/sheep_brain.png")

  # Note down the user's keypress, and the user know which key they press
  key = win6.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win6, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    biochem_counter += 4
    bio_counter += 3
    chem_counter += 2
    nsc_counter += 4
  elif key == "Down": # POSITION COORDINATES CENTER
    biochem_counter += 2
    bio_counter += 1.5
    chem_counter += 1
    nsc_counter += 2
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    biochem_counter += -4
    bio_counter += -3
    chem_counter += -2
    nsc_counter += -4

  # Close scenario 6 window
  win6.close()
  print() 
    
#=====================================================================

  # Scenario 7

  # Create an object for scenario 7 
  s7 = Scenario7()

  # Create scenario 7 window
  win7 = GraphWin("Scenario 7", 800, 600)
  win7.setBackground('white')

  # Present the scenario 7
  presentScenario(s7, win7, "images/solarpanels.png")

  # Note down the user's keypress, and the user know which key they press
  key = win7.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win7, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    mth_counter += 2
    egr_counter += 3 
  elif key == "Down": # POSITION COORDINATES CENTER
    mth_counter += 1
    egr_counter += 1.5
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    mth_counter += -2
    egr_counter += -3

  # Close scenario 7 window
  win7.close()
  print() 
   
#=====================================================================

  # Scenario 8

  # Create an object for scenario 8 
  s8 = Scenario8()

  # Create scenario 8 window
  win8 = GraphWin("Scenario 8", 800, 600)
  win8.setBackground('white')

  # Present the scenario 8
  presentScenario(s8, win8, "images/regression.png")

  # Note down the user's keypress, and the user know which key they press
  key = win8.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win8, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    mth_counter += 2.5
    csc_counter += 3.5
    sds_counter += 4
  elif key == "Down": # POSITION COORDINATES CENTER
    mth_counter += +1.75
    csc_counter += 2.5
    sds_counter += 2
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    mth_counter += -2.5
    csc_counter += -3
    sds_counter += -4

  # Close scenario 8 window
  win8.close()
  print()     

#=====================================================================

  # Scenario 9

  # Create an object for scenario 9 
  s9 = Scenario9()

  # Create scenario 9 window
  win9 = GraphWin("Scenario 9", 800, 600)
  win9.setBackground('white')

  # Present the scenario 9
  presentScenario(s9, win9, "images/env_plant.png")

  # Note down the user's keypress, and the user know which key they press
  key = win9.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win9, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    sds_counter += 3
    esp_counter += 3
  elif key == "Down": # POSITION COORDINATES CENTER
    sds_counter += 1.5
    esp_counter += 1.5
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    sds_counter += -3
    esp_counter += -3

  # Close scenario 9 window
  win9.close()
  print() 
  
#=====================================================================

  # Scenario 10

  # Create an object for scenario 10 
  s10 = Scenario10()

  # Create scenario 10 window
  win10 = GraphWin("Scenario 10", 800, 600)
  win10.setBackground('white')

  # Present the scenario 10
  presentScenario(s10, win10, "images/stats.png")

  # Note down the user's keypress, and the user know which key they press
  key = win10.getKey()
  print('\u001b[34;1m', '\nYou pressed:', key, '\u001b[0m')

  # Confirm the user's answer
  confirmAnswer(win10, key)

  # Add points to the corresponding counters based on the option chosen by user   
  if key == "Left": # POSITION ON GRAPH WOULD BE LEFT
    mth_counter += 4
    phy_counter += 4
  elif key == "Down": # POSITION COORDINATES CENTER
    mth_counter += 2
    phy_counter += 2
  elif key == "Right": # POSITION COORDINATES TO THE RIGHT
    mth_counter += -3
    phy_counter += -3

  # Close scenario 10 window
  win10.close()
  print() 

#=====================================================================

  # Results

  # Draw the result window
  win11 = GraphWin("Your Final Result", 800, 600) 
  win11.setBackground('white')

  # Add text to the result window
  result_title = Text(Point(400,250),'Your Final Result')
  result_title.setFace('courier')
  result_title.setSize(30)
  result_title.draw(win11)
  result_subtitle = Text(Point(400,350),'[Enter VIEW or EXIT]')
  result_subtitle.setSize(20)
  result_subtitle.setFace('courier')
  result_subtitle.draw(win11)

  # Print final result in the console
  print("\u001b[36m\033[1m---------- FINAL RESULT ----------\u001b[0m\033[0m\n")
  # Print all the counter values
  finalCounter()
  # Print the best match major, whose counter has the highest points
  for major, counter in major_dict.items():
    print(major + ':',counter)

  # If the user didn't like any scenarios, return an appropriate message (no major will be returned)
  if greatest_value <= 0:
    print('\nOops, you didn’t have a best match STEM major - maybe these classes weren\'t for you. Want to explore non-STEM majors instead?')
  else:
    print('\nYour best match is \u001b[31;1m\033[1m' + best_match_major + '\u001b[0m\033[0m with a value of \u001b[31;1m\033[1m{}\u001b[0m\033[0m\n'.format(greatest_value))
    
    # Allow user to choose whether to see the requirements for the best match major (VIEW) or to skip that and quit the game (QUIT)
    response = input("Do you want to view the major requirements for your best match? (VIEW/SKIP)\n").upper()

    # Ask user to input again if they're not typing in VIEW or EXIT
    while response != "VIEW" and response != "SKIP":
      print("Your input must be VIEW or SKIP. Please try again.\n")
      response = input("Do you want to view the major requirements for your best match? (VIEW/SKIP)\n").upper()

    # If the user inputs VIEW, allow them to see the requirements for the corresponding best match major
    if response == "VIEW":  
      print('\nHere are the requirements for your best match major:')
      if best_match_major == "Astronomy":
        print(astro_req)
      elif best_match_major == "Biochemistry":
        print(biochem_req)
      elif best_match_major == "Biological Sciences":
        print(bio_req)
      elif best_match_major == "Chemistry":
        print(chem_req)
      elif best_match_major == "Computer Science":
        print(csc_req)
      elif best_match_major == "Engineering Science":
        print(egr_req)
      elif best_match_major == "Environmental Science and Policy":
        print(esp_req)
      elif best_match_major == "Geosciences":
        print(geo_req)
      elif best_match_major == "Mathematics & Statistics":
        print(mth_req)
      elif best_match_major == "Neuroscience":
        print(nsc_req)
      elif best_match_major == "Physics":
        print(phy_req)
      elif best_match_major == "Statistical and Data Sciences":
        print(sds_req)

  print()



def endGame():
  """Quit the game."""
  # Draw the ending window
  win12 = GraphWin("End of Game", 800, 600)
  win12.setBackground('white')

  # Add text art to the ending window
  gameover_text = ("""
█████████████████████████████████████
█─▄─▄─█─█─██▀▄─██▄─▀█▄─▄█▄─█─▄█─▄▄▄▄█
███─███─▄─██─▀─███─█▄▀─███─▄▀██▄▄▄▄─█
▀▀▄▄▄▀▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
████████████████████
█▄─▄▄─█─▄▄─█▄─▄▄▀███
██─▄███─██─██─▄─▄███
▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████████████▀█
█▄─▄▄─█▄─▄████▀▄─██▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
██─▄▄▄██─██▀██─▀─███▄─▄███─███─█▄▀─██─██▄─█
▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀""")
  s11_title = Text(Point(400,300),gameover_text)
  s11_title.draw(win12)
   
  # Link to direct user to explore more about STEM majors at Smith
  print("\n🅶 🅰 🅼 🅴  🅾 🆅 🅴 🆁 - 🆃 🅷 🅰 🅽 🅺 🆂  🅵 🅾 🆁  🅿 🅻 🅰 🆈 🅸 🅽 🅶 ❗\n\u001b[1mTo explore further about the different majors at Smith, visit https://www.smith.edu/academics/courses-of-study\u001b[0m")



def restartPrompt():
  """Ask the user if they want to restart the game."""
  # Ask the user whether to restart the game or to quit
  again = input("Do you want to play the game again? (YES/NO)\n").upper()   

  # If user input is neither YES nor NO, ask the user to key in the appropriate input
  while again != "YES" and again != "NO":
    print("Your input must be YES or NO. Please try again.\n")
    again = input("Do you want to play the game again? (YES/NO)\n").upper()

  # Return the value of again to use the while loop in main()
  return again



def main():
  """Call other functions to start, end, and restart the game."""
  # Call playGame to allow user to play the first round
  playGame()

  # Call restartPrompt to check if the user wants to play again
  again = restartPrompt()

  # Create a loop to allow user to continue the game as long as again == "YES"
  while again == "YES":
    print("\n\u001b[46m******************** 🅡 🅔 🅛 🅞 🅐 🅓 🅘 🅝 🅖 ********************\u001b[0m\n")
    playGame()
    # Call restartPrompt to check if the user wants to play again
    again = restartPrompt()   
  
  # Quit the game if again == "NO"
  if again == "NO":
    endGame()  


if __name__ == "__main__":
  main()

# REFERENCES:

# How to draw a rectangle: https://www.geeksforgeeks.org/draw-square-and-rectangle-in-turtle-python/

# How to check whether clicks are within a graphics object: https://stackoverflow.com/questions/30136270/checking-if-clicks-are-within-a-graphic-object-python-graphics-module

# How to print in bold in Python: https://www.kite.com/python/answers/how-to-print-in-bold-in-python

# How to print colored text in Python: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

# Descriptions of the major and major requirements at Smith are mostly obtained from: https://www.smith.edu/academics/courses-of-study and https://catalog.smith.edu/index.php?mode=dept
  # Biological Sciences: https://docs.google.com/document/d/1Y471H_H6W678bSrFxwW_q7ETJJ87NLR_WDjTmnC9-j8/edit
  # Engineering Science: https://catalog.smith.edu/index.php?mode=dept
  # Environmental Science: https://www.smith.edu/sites/default/files/media/Documents/ESP/ENV_ChecklistFocusStatement.pdf


# Text Art: https://fsymbols.com/text-art/

# Citations for Images Used:

# Title page:
  # Play button: https://toppng.com/show_download/190695/stem-icon-image-stem-medicina-regenerativa/large


# Introduction:
  # Cartoon College Students: https://www.vhv.rs/viewpic/ximRxh_college-student-cartoon-png-transparent-png/
  # Cartoon Teacher: https://pngtree.com/so/female-teacher
  # Smith college background: https://www.britannica.com/topic/Smith-College#/media/1/549929/197995

# Scenarios:

  # Scenario 1 Image: https://icon2.cleanpng.com/20180212/ytw/kisspng-rocket-flat-design-icon-vector-cartoon-rocket-5a81ff95f08047.3417871815184690139851.jpg

  # Scenario 2 Image: http://chemskills.com/?q=aspirin

  # Scenario 3 Image 1: https://www.deviantart.com/tiggerbaby1122/art/Cow-Eye-Dissection-176456822 

  # Scenario 3 Image 2: https://quizlet.com/109690646/a-p-1-lab-exam-4-flash-cards/

  # Scenario 4 Image: https://www.youtube.com/watch?v=pofWfJc3Zog

  # Scenario 5 Image: https://www.iberdrola.com/environment/impacts-of-climate-change

  # Scenario 6 Image: https://learning-center.homesciencetools.com/article/brain-dissection-project/

  # Scenario 7 Image: https://image.freepik.com/free-vector/solar-cell-diagram-house-system-isometric-vector_255805-35.jpg

  # Scenario 8 Image: https://miro.medium.com/max/1776/1*6mykSFbcG4K_JhrCm9tSdg.jpeg

  # Scenario 9 Image: https://www.muhlenberg.edu/media/contentassets/images/academics/envisci/environmentalscience-header-1440x617.jpg

  # Scenario 10 Image: (Problems & Solutions to Statistical Physics of Particles by Mehran Kardar, MIT): https://www.academia.edu/13247291/Problems_and_Solutions_for_Statistical_Physics_of_Particles?auto=download 

