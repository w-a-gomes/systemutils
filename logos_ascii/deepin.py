#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}               .';::::;'.               
{}          .,:looo{}xXXXXXK0O{}o:'.          
{}       .:loooooo{}kMMMMMMMX{}kooool;.       
{}     'loooooooo{}OMMMMMW{}0doooooooool'     
{}   .l{}x{}llllllll{}xMMMMW{}Ooo{}xO0XNNWWWMWO{}l.   
{}  ,d{}NW{}olllllll{}XMMM0{}x{}OxkMKNNWMMMMMMMX{}o'  
{} ,o{}WMMK{}llllllo{}MMM{}kl{}NN{}ld{}MO{}O{}N{}dk{}WMMMMMMN{}o' 
{}.l{}XMMMMO{}llllll{}MMK{}l{}0W{}dl{}0M{}dx{}MX{}lo{}NMMMMMMK{}l 
{}'d{}MMMMMM0{}lcccc{}KM{}0{}00{}ol{}kMX{}lk{}MM{}dlx{}MMMMMMM{}o'
{},x{}MMMMMMMN{}xccc{}lKW0{}x{}OXMN{}ol{}NMM{}ocl{}WMMMMMM{}d,
{}'o{}MMMMMMMMMXk{}lcc{}d0XNKk{}lo{}XMM0{}ccc{}WMMMMMM{}l.
{} c{}KMMMMMMMMMMMX{}Okdoddk{}KMMWk{}cccx{}MMMMMM0{}c 
{} 'l{}NMMMMMMMMMMMMMMMMMMWKk{}ccccl{}NMMMMMX{}c. 
{}  .cod{}xO0KKXXXXXXK0Oxoc{}:::::l{}XMMMMMK{}c.  
{}   .;:::::::::::::::::::::c{}kWMMMMW{}x;.   
{}     .;:::::::::::::::::l{}kNMMMMX{}x;.     
{}       .';::::::::::co{}OXMMMWK{}kc'.       
{}           .',;;:l{}dO00Okx{}o:'.           
{}                ...''...
{}  """.format(
        blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue, white, blue,
        blue, white, blue, white, blue,
        blue, white, blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue, white, blue,
        blue,
        clean
        ) + "\n" + blue + clean
    
    return logo
