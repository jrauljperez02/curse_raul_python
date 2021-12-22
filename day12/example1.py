enemies = 1
def increase_enemies():
    enemies = 2
    print(f"Inside {enemies}")

increase_enemies()
print(f"Outside {enemies}")

"""Local scope"""
def drink_position():
    potion_strength = 2
    print(potion_strength)
"""
This variable just is going to work inside this funtion, and in that way, is called
local variable

"""

"""Global scope"""
player_health = 10
def drink_position():
    potion_strength = 2
    print(player_health)
drink_position()

"""we can declare in this way to have a global variable"""




"""
if we want to modify a global varaiable in a local scope we have to do...
"""
print("")
print("")
print("")
print("")

enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Inside {enemies}")
increase_enemies()
print(f"Outside {enemies}")
