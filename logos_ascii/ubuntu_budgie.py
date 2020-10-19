#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}             .:d0XWMMWX0d:.             
{}         .lkXMMMMMMMMMMWXKXKkc.         
{}      .oXMMMMMMMMMMMKc.      'o0o.      
{}    'OMMMMMMMMMMMMMc            ;XO'    
{}   xMMMMNXXNMMMMMM0               KMx   
{} .XMXo'     lKMMMMN.              'MMX. 
{} XN:       OMMMMMMMNc             .MMMX 
{}oN.        ;WMMMMMMMMMXOxkO0Od'   kMMMMo
{}Nc          .OMMMMMMMMMMMMMMMMM',0MMMMMN
{}M;            KMMMMMMMMMMMMMMMWNMMMMMMMM
{}N0            0MMMMMMMMMMMMMMMMMMMMMMMMX
{}oMK'         dMMMMMMMMNo'.  .,dWMMMMMMMo
{} XMMXxc,,,ckWMMMMMMMMx         .KMMMMMX 
{} .KMMMMMMMMMMMMWMMMMx           'MMMMK. 
{}   dMMMMMMMMMMM,:l:.            ;MMMd   
{}    .kMMMMMMMMM0.              'NMk.    
{}      .lXMMMMMMMWo.          ,kXl.      
{}         .cxXMMMMMMNOdolloxxxc.         
{}              ;dOXWMMWXOd;
{}    """.format(blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, 
        blue, blue, blue, blue, blue, blue, clean) + "\n" + blue + clean
    
    return logo
