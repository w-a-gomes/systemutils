#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}                   ..                   
{}                   O0                   
{}                  xMMO                  
{}                 oMMMMO                 
{}                lMMMMMMk                
{}               :MMMMMMMM0               
{}              lcckMMMMMMMK              
{}             xMMMN0NMMMMMMK.            
{}            kMMMMMMMMMMMMMMX.           
{}          .KMMMMMMMMMMMMMMMMW,          
{}         .XMMMMMMMMMMMMMMMMMMMc         
{}        ,WMMMMMMWo.  .cNMMMMMMMo        
{}       cMMMMMMMM'      .NMMMMMMMk       
{}      xMMMMMMMMO        oMMMMMNKNK.     
{}    .KMMMMMMMMMk        lMMMMMMli:.     
{}   'NMMMMMMWKko;        'lx0NMMMMMMO,   
{}  :WMMNkl,.                   'ckXMMMo  
{} xXx:.                            .;dKk 
{}''                                    .'
{}  """.format(blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, 
        blue, blue, blue, blue, blue, clean) + "\n" + blue + clean
    
    return logo
