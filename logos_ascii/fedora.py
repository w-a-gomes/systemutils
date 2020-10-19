#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    blue_bold = color["blue-bold"]
    clean = color["clean"]
    
    logo = """
{}                ........                
{}           ...''''''''''''...           
{}        .'''''''''''''{},clool:,{}'.        
{}     .'''''''''''''{}cONMMMMMMMX{}:;,{}'.     
{}    '''''''''''''{};KMMMMWK0000x{}ccc;{}''    
{}  .'''''''''''''{};NMMMXl{},''''',{}:ccc:{}''.  
{} .''''''''''''''{}dMMMW{};'''''''''{}:ccc,{}''. 
{} '''''''''''''''{}xMMMW{}'''''''''{},:ccc,{}''' 
{}.'''''''''''''''{}xMMMW{},,,,'''{},;:ccc;{}''''.
{}.'''''{},;:c{}dNMMMMMMMMMMMMMW0{}ccccc:,{}'''''.
{}.''{},;:cccc{}dXWWWWMMMMMWWWWWO{}cc:;,{}'''''''.
{}.'{},:ccc:;{},''''''{}xMMMW{}'''''''''''''''''' 
{}.'{}:ccc:{}'''''''''{}xMMMW{}'''''''''''''''''  
{}.'{}:ccc:{}'''''''''{}OMMMN{}''''''''''''''''   
{}.'{};cccc;{},'''''{}:kMMMMd{}''''''''''''''.    
{}.''{},:cc{}lOK00KNMMMMNo{}'''''''''''''.      
{}.''''{},:{}dMMMMMMMW0o{},'''''''''''..        
{} .''''''{};clooc;{}''''''''''...            
{}    ''''''''''''''''''''
{}  """.format(
        blue,
        blue,
        blue, white,     blue,
        blue, white,     blue_bold, blue,
        blue, white,     blue_bold, blue,
        blue, white,     blue,      blue_bold, blue,
        blue, white,     blue,      blue_bold, blue,
        blue, white,     blue,      blue_bold, blue,
        blue, white,     blue,      blue_bold, blue,
        blue, blue_bold, white,     blue_bold, blue,   
        blue, blue_bold, white,     blue_bold, blue,
        blue, blue_bold, blue,      white,     blue,
        blue, blue_bold, blue,      white,     blue,
        blue, blue_bold, blue,      white,     blue,
        blue, blue_bold, blue,      white,     blue,
        blue, blue_bold, white,     blue,
        blue, blue_bold, white,     blue,
        blue, white,     blue,
        blue,
        clean
    ) + "\n" + blue + clean
    
    return logo
