#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    red_bold = color["red-bold"]
    clean = color["clean"]
    
    logo = """
                                        
                                        
                                        
                                        
                                        
{}                         ,o'            
{}  ,clc:;..           .cOWNd.            
{};WWxodxOXWWKxc'   ,dXMKo.         ...   
{}WM,       .,lKMMNMMNc      'cx0NMNXXWWk.
{}0Md     .;okXMXxco0WMKxlxXMXkl,.     lMX
{} dNWXXWWX0dc'     .:NMMXMMKo;.       'MW
{}    ..         .oKMKo,   .:d0NMX0kxdkNWc
{}            .xNWO:.            .,:cc:'  
{}            .l,                         
{}                                        
                                        
                                        
                                        
                     
    """.format(red_bold, red_bold, red_bold, red_bold, red_bold, red_bold, red_bold, red_bold, 
    	red_bold, clean) + "\n" + red_bold + clean
    
    return logo
