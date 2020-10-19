#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    blue_bold = color["blue-bold"]
    clean = color["clean"]

    logo = """
{}               .°°.                    
{}                °°.°°,                 
{}                  `..´                 
{}                .°°°.                  
{}                '...'                  
{}             .''''..°°°.               
{}             '    ''...'               
{}              ''''                     
{}          ,,,           ,,,            
{}         kMNXMXOdooodkKWWXMX.          
{}       .XMk    '''''''    :WM:         
{}       OMO                 cMW.        
{}       WM;                 .MM;        
{}       0Md                 ;MM.        
{}       .WM;               .XMd         
{}        'NMx.            cWMo          
{}          lNMOc'.    .;xNWk'           
{}            'o0NMMWWMWKx'              
{}                '''''                  
{}  """.format(
        blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, 
        white, white, white, white, white, white, white, white, white, white, white, 
        clean) + "\n" + blue + clean
    
    return logo
