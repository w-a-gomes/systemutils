#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    green = color["green"]
    green_back = color["green-background"]
    clean = color["clean"]
    
    logo = """
                                        
   {} ......................{}  {}.......... {} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMo{}              {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}dkkkkkkkko{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {} ......... {}  {}..........{}  {} ......... {} 

    """.format(
        green_back, clean, green_back, clean,
        green_back, clean, green_back, clean,
        green_back, clean, green_back, clean,
        green_back, clean, green_back, clean,
        green_back, clean, green_back, clean,
        green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean,
        green_back, clean, green_back, clean, green_back, clean
    ) + "\n" + green + clean
    
    return logo
