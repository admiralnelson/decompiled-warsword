# -*- coding: UTF-8 -*-
####################################################################################################################
# Generated by Warband Module Decompiler
# All rights of the module belong to their respective owners
####################################################################################################################

from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction", "No_Faction", 0, 0.0, [("no_faction", 0.9)], []),
  ("commoners", "Commoners", 0, 0.0, [("commoners", 0.1),("outlaws", -0.6),("player_faction", 0.1),("mountain_bandits", -0.2),("forest_bandits", -0.2),("undeads", -0.7)], []),
  ("outlaws", "Outlaws", max_player_rating(-30), 0.0, [("commoners", -0.6),("outlaws", 0.5),("innocents", -0.05),("merchants", -0.5),("player_faction", -0.15),("player_supporters_faction", -0.5),("kingdom_1", -0.05),("kingdom_2", -0.05),("kingdom_3", -0.05),("kingdom_4", -0.05),("kingdom_5", -0.5),("kingdom_6", -0.5),("kingdom_7", -0.5),("kingdom_8", -0.05),("kingdom_9", -0.05),("kingdom_10", -0.05),("kingdom_11", -0.05),("kingdom_12", -0.05),("kingdom_13", -0.05),("kingdom_14", -0.05),("kingdom_15", -0.5),("kingdom_16", -0.5),("kingdom_17", -0.5),("kingdom_18", -0.5),("manhunters", -0.6),("invaders", -0.4),("chaos_invaders", -0.4)], [], 0x888888),
  ("neutral", "Neutral", 0, 0.0, [("neutral", 0.1)], [], 0xFFFFFF),
  ("innocents", "Innocents", ff_always_hide_label, 0.0, [("outlaws", -0.05),("innocents", 0.5),("dark_knights", -0.9)], []),
  ("merchants", "Merchants", ff_always_hide_label, 0.0, [("outlaws", -0.5),("merchants", 0.5),("deserters", -0.5),("mountain_bandits", -0.5),("forest_bandits", -0.5)], []),
  ("dark_knights", "{!}Dark_Knights", 0, 0.0, [("innocents", -0.9),("dark_knights", 0.5),("player_faction", -0.4)], []),
  ("culture_1", "{!}culture_1", 0, 0.0, [("culture_1", 0.9)], []),
  ("culture_2", "{!}culture_2", 0, 0.0, [("culture_2", 0.9)], []),
  ("culture_3", "{!}culture_3", 0, 0.0, [("culture_3", 0.9)], []),
  ("culture_4", "{!}culture_4", 0, 0.0, [("culture_4", 0.9)], []),
  ("culture_5", "{!}culture_5", 0, 0.0, [("culture_5", 0.9)], []),
  ("culture_6", "{!}culture_6", 0, 0.0, [("culture_6", 0.9)], []),
  ("culture_7", "{!}culture_7", 0, 0.0, [("culture_7", 0.9)], []),
  ("culture_8", "{!}culture_8", 0, 0.0, [("culture_8", 0.9)], []),
  ("culture_9", "{!}culture_9", 0, 0.0, [("culture_9", 0.9)], []),
  ("culture_10", "{!}culture_10", 0, 0.0, [("culture_10", 0.9)], []),
  ("culture_11", "{!}culture_11", 0, 0.0, [("culture_11", 0.9)], []),
  ("culture_12", "{!}culture_12", 0, 0.0, [("culture_12", 0.9)], []),
  ("culture_13", "{!}culture_13", 0, 0.0, [("culture_13", 0.9)], []),
  ("culture_14", "{!}culture_14", 0, 0.0, [("culture_14", 0.9)], []),
  ("culture_15", "{!}culture_15", 0, 0.0, [("culture_15", 0.9)], []),
  ("culture_16", "{!}culture_16", 0, 0.0, [("culture_16", 0.9)], []),
  ("culture_17", "{!}culture_17", 0, 0.0, [("culture_17", 0.9)], []),
  ("culture_18", "{!}culture_18", 0, 0.0, [("culture_18", 0.9)], []),
  ("player_faction", "Player_Faction", 0, 0.0, [("commoners", 0.1),("outlaws", -0.15),("dark_knights", -0.4),("player_faction", 0.9),("player_supporters_faction", 1),("black_khergits", -0.3),("manhunters", 0.1),("deserters", -0.1),("mountain_bandits", -0.15),("forest_bandits", -0.15),("invaders", -0.4),("chaos_invaders", -0.4),("undeads", -0.5),("peasant_rebels", -0.4)], []),
  ("player_supporters_faction", "Player's_Supporters", 0, 0.0, [("outlaws", -0.5),("player_faction", 1),("player_supporters_faction", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("invaders", -0.5),("chaos_invaders", -0.5),("peasant_rebels", -0.1)], [], 0x99600),
  ("kingdom_1", "Empire_of_Sigmar", 0, 0.0, [("outlaws", -0.05),("kingdom_1", 0.9),("black_khergits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xDD8844),
  ("kingdom_2", "Dwarfs", 0, 0.0, [("outlaws", -0.05),("kingdom_2", 0.9),("black_khergits", -0.02),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xCCBB99),
  ("kingdom_3", "High_Elven_Kingdom", 0, 0.0, [("outlaws", -0.05),("kingdom_3", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xFFFFFFFF),
  ("kingdom_4", "Chaos_Dwarf_Colonies", 0, 0.0, [("outlaws", -0.05),("kingdom_4", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.3),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xCC9900),
  ("kingdom_5", "Realm_Of_Chaos", 0, 0.0, [("outlaws", -0.5),("kingdom_5", 0.9),("deserters", -0.02),("forest_bandits", -0.3),("invaders", -0.4),("chaos_invaders", 1),("peasant_rebels", -0.1)], [], 0xFF0000),
  ("kingdom_6", "Tomb_Kings_of_Nehekhara", 0, 0.0, [("outlaws", -0.5),("kingdom_6", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x8B7900),
  ("kingdom_7", "Lizardmen_Empire", 0, 0.0, [("outlaws", -0.5),("kingdom_7", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xFFCC),
  ("kingdom_8", "Night_Goblins", 0, 0.0, [("outlaws", -0.05),("kingdom_8", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x33CC33),
  ("kingdom_9", "Sultanate_of_Araby", 0, 0.0, [("outlaws", -0.05),("kingdom_9", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xDDDD33),
  ("kingdom_10", "Orcs", 0, 0.0, [("outlaws", -0.05),("kingdom_10", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x336E00),
  ("kingdom_11", "Kingdom_of_Bretonnia", 0, 0.0, [("outlaws", -0.05),("kingdom_11", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x33BFFF),
  ("kingdom_12", "Dark_Elven_Kingdom", 0, 0.0, [("outlaws", -0.05),("kingdom_12", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x7A54AE),
  ("kingdom_13", "Skaven_Underworld", 0, 0.0, [("outlaws", -0.05),("kingdom_13", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x660000),
  ("kingdom_14", "Tsardom_of_Kislev", 0, 0.0, [("outlaws", -0.05),("kingdom_14", 0.9),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xFFAAAAFF),
  ("kingdom_15", "Beastmen", 0, 0.0, [("outlaws", -0.5),("kingdom_15", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.3),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0x663300),
  ("kingdom_16", "Nippon_Colonies", 0, 0.0, [("outlaws", -0.5),("kingdom_16", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.3),("invaders", -0.4),("chaos_invaders", -0.4),("peasant_rebels", -0.1)], [], 0xDB7093),
  ("kingdom_17", "Vampire_Counts_of_Sylvania", 0, 0.0, [("outlaws", -0.5),("kingdom_17", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.3),("invaders", -0.5),("chaos_invaders", -0.5),("peasant_rebels", -0.1)], [], 0x747374),
  ("kingdom_18", "Wood_Elven_Kingdom", 0, 0.0, [("outlaws", -0.5),("kingdom_18", 0.9),("deserters", -0.02),("mountain_bandits", -0.3),("forest_bandits", -0.3),("invaders", -0.5),("chaos_invaders", -0.5),("peasant_rebels", -0.1)], [], 0xADFF2F),
  ("kingdoms_end", "{!}kingdoms_end", 0, 0.0, [], []),
  ("robber_knights", "{!}robber_knights", 0, 0.0, [("robber_knights", 0.1)], []),
  ("khergits", "{!}Khergits", 0, 0.0, [("khergits", 0.5)], []),
  ("black_khergits", "{!}Black_Khergits", 0, 0.0, [("player_faction", -0.3),("kingdom_1", -0.02),("kingdom_2", -0.02),("black_khergits", 0.5)], []),
  ("manhunters", "Manhunters", 0, 0.0, [("outlaws", -0.6),("player_faction", 0.1),("manhunters", 0.5),("deserters", -0.6),("mountain_bandits", -0.6),("forest_bandits", -0.6)], []),
  ("deserters", "Deserters", 0, 0.0, [("merchants", -0.5),("player_faction", -0.1),("player_supporters_faction", -0.02),("kingdom_1", -0.02),("kingdom_2", -0.02),("kingdom_3", -0.02),("kingdom_4", -0.02),("kingdom_5", -0.02),("kingdom_6", -0.02),("kingdom_7", -0.02),("kingdom_8", -0.02),("kingdom_9", -0.02),("kingdom_10", -0.02),("kingdom_11", -0.02),("kingdom_12", -0.02),("kingdom_13", -0.02),("kingdom_14", -0.02),("kingdom_15", -0.02),("kingdom_16", -0.02),("kingdom_17", -0.02),("kingdom_18", -0.02),("manhunters", -0.6),("deserters", 0.5)], [], 0x888888),
  ("mountain_bandits", "Mountain_Bandits", 0, 0.0, [("commoners", -0.2),("merchants", -0.5),("player_faction", -0.15),("player_supporters_faction", -0.05),("kingdom_1", -0.05),("kingdom_2", -0.3),("kingdom_3", -0.3),("kingdom_4", -0.05),("kingdom_6", -0.3),("kingdom_7", -0.3),("kingdom_8", -0.3),("kingdom_9", -0.3),("kingdom_10", -0.05),("kingdom_11", -0.3),("kingdom_12", -0.3),("kingdom_13", -0.3),("kingdom_14", -0.05),("kingdom_15", -0.3),("kingdom_16", -0.3),("kingdom_17", -0.3),("kingdom_18", -0.3),("manhunters", -0.6),("mountain_bandits", 0.5)], [], 0x888888),
  ("forest_bandits", "Forest_Bandits", 0, 0.0, [("commoners", -0.2),("merchants", -0.5),("player_faction", -0.15),("player_supporters_faction", -0.05),("kingdom_1", -0.05),("kingdom_2", -0.05),("kingdom_3", -0.05),("kingdom_4", -0.3),("kingdom_5", -0.3),("kingdom_6", -0.05),("kingdom_7", -0.05),("kingdom_8", -0.05),("kingdom_9", -0.05),("kingdom_10", -0.05),("kingdom_11", -0.05),("kingdom_12", -0.05),("kingdom_13", -0.05),("kingdom_14", -0.05),("kingdom_15", -0.3),("kingdom_16", -0.3),("kingdom_17", -0.3),("kingdom_18", -0.3),("manhunters", -0.6),("forest_bandits", 0.5)], [], 0x888888),
  ("invaders", "Invaders", 0, 0.0, [("outlaws", -0.4),("player_faction", -0.4),("player_supporters_faction", -0.5),("kingdom_1", -0.4),("kingdom_2", -0.4),("kingdom_3", -0.4),("kingdom_4", -0.4),("kingdom_5", -0.4),("kingdom_6", -0.4),("kingdom_7", -0.4),("kingdom_8", -0.4),("kingdom_9", -0.4),("kingdom_10", -0.4),("kingdom_11", -0.4),("kingdom_12", -0.4),("kingdom_13", -0.4),("kingdom_14", -0.4),("kingdom_15", -0.4),("kingdom_16", -0.4),("kingdom_17", -0.5),("kingdom_18", -0.5),("invaders", 0.5),("chaos_invaders", -0.4)], [], 0xFF4500),
  ("chaos_invaders", "Invaders", 0, 0.0, [("outlaws", -0.4),("player_faction", -0.4),("player_supporters_faction", -0.5),("kingdom_1", -0.4),("kingdom_2", -0.4),("kingdom_3", -0.4),("kingdom_4", -0.4),("kingdom_5", 1),("kingdom_6", -0.4),("kingdom_7", -0.4),("kingdom_8", -0.4),("kingdom_9", -0.4),("kingdom_10", -0.4),("kingdom_11", -0.4),("kingdom_12", -0.4),("kingdom_13", -0.4),("kingdom_14", -0.4),("kingdom_15", -0.4),("kingdom_16", -0.4),("kingdom_17", -0.5),("kingdom_18", -0.5),("invaders", -0.4),("chaos_invaders", 0.5)], [], 0xFF4500),
  ("undeads", "{!}Undeads", max_player_rating(-30), 0.0, [("commoners", -0.7),("player_faction", -0.5),("undeads", 0.5)], []),
  ("slavers", "{!}Slavers", 0, 0.0, [("slavers", 0.1)], []),
  ("peasant_rebels", "{!}Peasant_Rebels", 0, 0.0, [("player_faction", -0.4),("player_supporters_faction", -0.1),("kingdom_1", -0.1),("kingdom_2", -0.1),("kingdom_3", -0.1),("kingdom_4", -0.1),("kingdom_5", -0.1),("kingdom_6", -0.1),("kingdom_7", -0.1),("kingdom_8", -0.1),("kingdom_9", -0.1),("kingdom_10", -0.1),("kingdom_11", -0.1),("kingdom_12", -0.1),("kingdom_13", -0.1),("kingdom_14", -0.1),("kingdom_15", -0.1),("kingdom_16", -0.1),("kingdom_17", -0.1),("kingdom_18", -0.1),("peasant_rebels", 1),("noble_refugees", -1)], []),
  ("noble_refugees", "{!}Noble_Refugees", 0, 0.0, [("peasant_rebels", -1),("noble_refugees", 0.5)], []),
]