#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    cyan = color["cyan"]
    green = color["green"]
    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}              .,:cllllc:,.              
{}         ..;cllllo{}dkkd{}ollllc;..         
{}       'cll{}okkkkkkkkkkkkkkkko{}llc'       
{}    .:l{}xxOOko{}llllll{}xx{}llllll{}okOOxx{}l:.    
{}   ;l{}l{}dX{}x{}O{}ll{}ll{}xkkk0OO0kkkx{}ll{}ll{}O{}x{}Xd{}ll;   
{}  c{}ll{}O0o{}l{}llx{}OOd{}lll{}lll{}lll{}l{}dOO{}xl{}ll{}o0O{}l{}lc  
{} c{}ll{}0k{}ll{}l{}o0k{}ll{}lll{}lll{}lll{}lll{}ll{}k0o{}l{}ll{}k0{}llc 
{},l{}l{}k0{}l{}ll{}oXo{}ll{}l{}lll{}oxkkxo{}ll{}l{}lll{}oXo{}lll{}0k{}l{}l,
{}cl{}oXo{}lll{}Kx{}llllll{}0WMMMMW0{}llllll{}xK{}lll{}oXo{}lc
{}ll{}K{}k{}K{}lll{}No{}lllll{}dMMMMMMMMd{}lllll{}oN{}lll{}K{}k{}K{}ll
{}cl{}lXo{}lll{}0x{}llllll{}0WMMMMW0{}llllll{}x0{}lll{}oXl{}lc
{},l{}l{}k0{}l{}ll{}oXo{}ll{}l{}lll{}oxkkxo{}l{}ll{}lll{}oXo{}lll{}0k{}ll,
{} c{}ll{}0k{}ll{}l{}o0k{}ll{}llll{}ll{}lll{}lll{}ll{}k0o{}l{}ll{}k0{}llc 
{}  c{}ll{}O0o{}l{}ll{}dOOd{}lll{}lll{}lll{}l{}dOOd{}l{}ll{}o0O{}l{}lc  
{}   ,ll{}dX{}x{}O{}llll{}xkkk0OO0kkkd{}llll{}O{}x{}Xd{}ll,   
{}    .;l{}xxOOkd{}llllll{}xx{}llllll{}dkOOxx{}l;.    
{}       'cll{}oxkkkkkkkkkkkkkkxo{}llc'       
{}          .,clllll{}dkkd{}lllllc,.          
{}              .,:cllllc:,.
{}    """.format(
        green,
        green, white, green,
        green, white, green,
        green, white, green, white, green, white, green,
        cyan,  green, white, green, white, cyan,  green, white, green, cyan,  white, green, white, cyan,
        green, cyan,  white, green, cyan,  white, cyan,  green, cyan,  green, white, cyan,  green, white, cyan,  green,
        cyan,  green, white, cyan,  green, white, cyan,  green, cyan,  green, cyan,  green, white, cyan,  green, white, cyan,
        cyan,  green, white, cyan,  green, white, cyan,  green, cyan,  white, cyan,  green, cyan,  white, cyan,  white, green, cyan,
        cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,
        cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,
        cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,
        blue,  cyan,  white, cyan,  blue,  white, cyan,  blue,  cyan,  white, cyan,  blue,  cyan,  white, cyan,  white, blue,
        cyan,  blue,  white, cyan,  blue,  white, cyan,  blue,  cyan,  blue,  cyan,  blue,  white, cyan,  blue,  white, cyan,
        cyan,  cyan,  white, blue,  cyan,  white, cyan,  blue,  cyan,  blue,  white, cyan,  blue,  white, cyan,  blue,
        blue,  white, blue,  white, blue,  white, blue,  white, blue,  white, blue,
        blue,  white, blue,  white, blue,  white, blue,
        blue,  white, blue,
        blue,  white, blue,
        blue,
        clean
    ) + "\n" + cyan + clean
    
    return logo
