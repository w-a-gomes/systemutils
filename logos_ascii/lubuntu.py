#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}             .:d0XWMMWX0d:.             
{}         .ck00{}OxdollllodxO{}00kc.         
{}      .dK0{}dccccccccccccccccccd{}0Kd.      
{}    'OX{}dcccccccccccccc{};i'{}cccccccd{}KO'    
{}   xN{}dcccccccccccc{}idOXXd{}ccccccccccd{}Nx   
{} .K0{}cccccccccc{}ik0NMMMMO{}ccccccccccccc{}0K. 
{} XK{}cccccccc{}d0NMMMMMMMMMK{}occcccccccccc{}KX 
{}oW{}lcccc{}ikKWMMMMMMMMMMMMMMk{}ccccccccccc{}lWo
{}X0{}cc{}oOXMMMMMMMMMMMXKNMMMMMO{}ccccccccccc{}0X
{}M0ONWXClkWMMMMMM0{}occc{}l0MMMMk{}cccccccccc{}kM
{}XX{}dlccc{}lKMPlMMX{}occccccco{}XMMW{}occccccccc{}0X
{}oW{}lccc{}dNK{}ok{}MWk{}ccccccccccc{}KMMX{}cccccccc{}lWo
{} KK{}c{}l0X{}ol{}KM0l{}ccccccccccccc{}0MMd{}ccccccc{}KK 
{} .KKK{}xcd{}WNd{}cccccccccccccccc{}0MX{}cccccc{}KK. 
{}   dNdOWO{}ccccccccccccccccccc{}KM{}occc{}dNd   
{}    .OMO{}cccccccccccccccccccc{}lN0{}cx{}XO.    
{}      .oK0xl{}cccccccccccccccc{}lOWKo.      
{}         .cx0KOkddooooddxO00xc.         
{}              ;dOXWMMWXOd;
{}    """.format(
        white,
        white, blue, white,
        white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white, blue, white,
        white, blue, white, blue, white, blue, white, blue, white,
        white, blue, white, blue, white, blue, white, blue, white,
        white, blue, white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white, blue, white,
        white, blue, white,
        white,
        white,
        clean
    ) + "\n" + blue + clean
    
    return logo
