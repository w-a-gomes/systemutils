#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    red = color["red"]
    clean = color["clean"]
    
    logo = """
{}              ;d0XWMMWX0d;              
{}         .ck0K0{}kxddddddxk{}0K0kc.         
{}      .oK0k{}ollllllllllllllllo{}x0Ko.      
{}    .OX{}xolllllllllllllll{}k0KOd{}llo{}xXO.    
{}   dN{}xlllllllll{}idkkOOk{}xx{}MMMMX{}lllll{}xNd   
{} .KK{}olllllll{}dOx{}k{}iMMMMMMOONNi{}dllllllo{}KK. 
{} KK{}ollllll{}o0MMMl{}x{}OkxxkOKWWNW0o{}llllllo{}KK 
{}oW{}ollllll{}dNMMWO{}ollllllllo{}OWMMNd{}llllllo{}Wo
{}X0{}lllx{}KXK{}k{}KMM{}xllllllllllllx{}MMMK{}lllllll{}0X
{}MO{}llo{}MMMMM{}o{}WN{}llllllllllllllkOOklllllll{}OM
{}X0{}lll{}x0K0{}k{}XMM{}xllllllllllll{}xMMMK{}lllllll{}0X
{}lW{}ollllll{}oNMMMOo{}llllllllo{}0MMMN{}ollllllo{}Wl
{} KK{}ollllll{}o0WMW{}x{}x0OkkO0XWNNW0{}ollllllo{}KK 
{}  KK{}olllllll{}ok{}dk{}MMMMMMMOOXXP{}dllllllo{}KK  
{}   dNx{}lllllllll{}odxkkkkd{}x{}MMMMX{}lllll{}xNd   
{}    .OXk{}olllllllllllllll{}x0KOo{}llo{}kXO.    
{}      .oKKk{}ollllllllllllllllo{}kKKo.      
{}         .:x0K0k{}xxddddxx{}k0K0x:.         
{}              ,oOXWMMWXOo,
{}    """.format(
        white, 
        white, red, white,
        white, red, white,
        white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white, red, white,
        white, red, white, red, white,
        white, red, white,
        white, red, white,
        white,
        clean
        ) + "\n" + red + clean
    
    return logo
