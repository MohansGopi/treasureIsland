print('''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')


print("Welcome to the treassure island ...... !")
print("\nIn this game you play with your luck")
print("\nNow you're in the starting point")
l_r = input("\nThere have a two door, one is right door and \nthe another one is the left door. \nYou have choose L - left door and R - right door : ")
l_r = l_r.lower()
if l_r == "l":
  print("\nYou choose the worng one ....")
elif l_r == "r":
  print("\nGreat choice .....:)")
  print("\nNow the river is flowing around the island...")
  print("\nNow you have two choices, one is wait for any boot or cross the river by swimming.....")
  w_s = input("\nYou have to choose w - wait or s - swim : ")
  w_s = w_s.lower()
  if w_s == 'w':
    print("\nThat was a great choice ....... , you survive the river....:)")
    print("\nNow there are three doors : 'RED','BLUE','GREEN' , You hjave choose one of these")
    rgb = input("\nFor red -r , blue - b, green -g : ")
    rgb = rgb.lower()
    if rgb == "r":
      print("\nYour choice is good but, the room full of man-hunter, they hunt you down")
      print("\nBETTER LUCK NEXT TIME .......")
    elif rgb == 'b' :
      print("\nOMG! You win this game, Now the treasure is your's ......., enjoy the treasure with your friends...")
    elif rgb == 'g':
      print("\nYour choice is good but, the room is full of fire, the fire will fry you......")
    else:
      print("\nwrong input")
  elif w_s == 's':
    print("\nOh, that was a great try but you choose the worng choice, the river dump you")
  else:
    print("\nWrong input")
else:
  print("\nwrong input")
  
  