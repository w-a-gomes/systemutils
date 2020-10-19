#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    red = color["red"]
    clean = color["clean"]
    
    logo = """
{}                .:c'....                
{}            .ckXMMMMWMMMNOol:.          
{}         .dXMMMW0o:;,,,:lxKMMMNo.       
{}        xMMMKc.            .lNMMWd      
{}      .XMXc.                  xMMNO     
{}     cMW:          .:;,'.      dMK,     
{}    ,MMc         ,o'            WM;     
{}    xMx         :l              NMd     
{}    xM;         K.              WX.     
{}    xM'         dk            .0X.      
{}    oMo         .ok'   .    .l0l        
{}    .MN           .d0olclodko'          
{}     oMNd            ....               
{}      oMW:                              
{}       ,NW;                             
{}         oWO.                           
{}           cKK:                         
{}             .cddc.                     
{}                 .;;.
{}  """.format(red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, red, 
        red, red, clean) + "\n" + red + clean
    
    return logo
