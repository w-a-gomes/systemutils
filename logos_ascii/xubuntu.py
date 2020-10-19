#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}              ..',,,,,,'..              
{}          ..,;;;;;;;;;;;;;;,..          
{}       .,;;;;;;;;;;;;;;;;;;;;;;,.       
{}     .;;;;;;;;;;;;;;;;;;;;{}c{};;;;;;;'     
{}   .;;;;;;;;;;:{}loc{};;;;;;;{}cW{}c;;:{}xl{};;;.   
{}  ';;;;;;{}oxo{};;{}XMMWo{};;;;;;{}xW{}:;l{}N0{}:;;;;'  
{} ';;;;;;{}xMMM0{}:{}XMMM0{};;;;;;{}K0{};x{}WO{};;;;;;;' 
{}.;;;;;;;{}oMMMMKkMMMXlc{}:;;;{}0{}co{}Wd{};;;;;;;;;.
{}';;;;;;;:{}WMMMMMMMMMMMMWNK0kxl{};;;;;;;;;;'
{},;;;;;;;{}0MMMMMMMMMMMMMMMMMMMMNOl{};;;;;;;,
{}';;;;;;{}lMMMMMMMMMMMMMMMMMMMMMMMWl{};;;;;;'
{}.;;;;;;{}kMMMMMMMMMMMMMMMMMMMMMMM0{}:;;;;;;.
{} ';;;;;{}kMMMMMMMMMMMMMMMMMMMWKxc{};;;;;;;' 
{}  ';;;;{}cWMMMMMMMMMMMMMMN0kl{}:;;;;;;;;;'  
{}   .;;;;{}cOXWMMMMWNKOxoc{};;;;;;;;;;;;;.   
{}     .;;;;;;{}ccc{}:;;;;;;;;;;;;;;;;;;.     
{}       .';;;;;;;;;;;;;;;;;;;;;;'.       
{}          ..';;;;;;;;;;;;;;'..          
{}               ..',,,,'..
{}    """.format(
        blue,
        blue,
        blue,
        blue, white, blue,
        blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue,
        blue,
        blue,
        clean
    ) + "\n" + blue + clean
    
    return logo
