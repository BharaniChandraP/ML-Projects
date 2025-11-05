# main.py
# (This file is provided by freeCodeCamp)

import RPS_game
from RPS_game import play, mrugesh, abbey, kris, quincy
from RPS import player
import test_module

# --- Play against each bot ---
print("--- Playing against Quincy (1000 games) ---")
play(player, quincy, 1000)

print("\n--- Playing against Abbey (1000 games) ---")
play(player, abbey, 1000)

print("\n--- Playing against Kris (1000 games) ---")
play(player, kris, 1000)

print("\n--- Playing against Mrugesh (1000 games) ---")
play(player, mrugesh, 1000)

# --- Run the tests ---
# Uncomment the line below to run the unit tests
# test_module.test_player(player)
