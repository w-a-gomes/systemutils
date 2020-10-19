#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    blue_bold = color["blue-bold"]
    blue_dark = color["blue-dark"]
    clean = color["clean"]
    
    logo = """
{}            .                           
{}            ''............              
{}        ....{}dX{}:...............          
{}      .....:{}WMMx{}'................       
{}    ......;{}NMMMMX{};.................     
{}  .......,{}XMMMMMMW{}o.................    
{} .......,{}XMMMMMMMMM{};'{}c{}'..............   
{} ......;{}XMMMMMMMMMMl{}.{}lNx{},.............  
{}......:{}NMMMMMMMMMMMd.{}.{}OMWk{};;{}lxdc{},...... 
{}.....l{}WMMMMMMMMMMMMk.{}.{}cMMMWk{},'{}lKMN0d{}:'. 
{}...'{}xMMMMMMMMMMMMMMK.{}.,{}MMMMMWo{}..{}oWMMMN;{}.
{}..'{}0MMMMMMMMMMMMMMMN.{}.;{}MMMMMMM0{},.{}xMWO:{}. 
{}.'{}xKNWMMMMMMMMMMMMMM{},.{}oMMMMMMMMX{},{}'{}ol{}kx  
{}  ....',;{}:ccloddxkOO{};'{};;;;;''{}oll{}dkko{},   
{}   'lcc:::;;;;;;;;:::{}clodxxxxxdc{},',.    
{}    ':llooodddddddoollc:;{},',,,,,,.      
{}       ,,,,,,,,,,,,,,,,,,,,,,,,,        
{}          ,,,,,,,,,,,,,,,,,,,           
{}               ,,,,,,,,,
{}               """.format(
        blue_dark, 
        blue_dark, 
        blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, white, blue_dark, 
        blue_dark, white, blue_dark, white, blue_dark, white, blue_dark, white, 
        blue_dark, white, blue_dark, white, blue_dark, white, blue_bold, 
        blue_dark, white, blue_bold, 
        white, blue_bold, 
        blue_bold, 
        blue_bold, 
        blue_bold, 
        clean) + "\n" + blue + clean
    
    return logo
