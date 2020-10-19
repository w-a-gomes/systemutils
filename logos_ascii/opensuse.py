#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    green = color["green"]
    white_bold = color["white-bold"]
    clean = color["clean"]
    
    logo = """
{}             'lkKNWMMWNKkl'             
{}         'oONMWKOxdoodxOKNMNOo'         
{}      .xNMXd;.            .;dKMNx.      
{}    ,0MXl {}..                  {}.lXM0,    
{}  .kMMK{},. kMMNK0kdl::.           {}cNMk.  
{} .XMM{}MMMMWWMMMMMMMMMMMWKko;.      {}.OMX. 
{}.NMM{}MMMMMMMMMMMMMMMWx:{},,,,{}oXXc      {}OMN.
{}xMMK{}MMMMMMMMMMMMMMN.,{}KM0kOo{} kMk     {}.NMx
{}NMM{}MMMMMMMMMMMMMMMk {}KMW..dM'{}'MMx     {}dMN
{}MMM{}MMMMMMMMMWkNMMMW'{}.kWMMX.{}.OMMMc    {}cMM
{}NMM{}MMMMMMMMMMk.':NKWOlpppppNMY:''    {}dMN
{}dMMK{}MMMMMMMMMMWKKx''''''''´,,xxMN   {}.NMd
{}.XMMM{}MMMMMMMMMMMMMMMMMMMMMMMMMMN'   {}0MX.
{} .KMMM{}MMMMMMMMMMMMMMMMMMMMWKkl'   {}.0MK. 
{}   xMMM{}d:;:ccoddxxxdolc;'.       {}oWMx   
{}    .kWNd'                    'dNWk.    
{}      .oXMNkc'            'ckNMXo.      
{}         .ckXMMN0OkxxkO0XMMXkc.         
{}             .:x0NWMMWN0x:.
{}    """.format(
        white_bold, white_bold, white_bold, 
        white_bold, green, white_bold, 
        white_bold, green, white_bold, 
        white_bold, green, white_bold, 
        white_bold, green, white_bold, green, white_bold,
        white_bold, green, white_bold, green, white_bold,
        white_bold, green, white_bold, green, white_bold,
        white_bold, green, white_bold, green, white_bold,
        white_bold, green, white_bold,
        white_bold, green, white_bold,
        white_bold, green, white_bold,
        white_bold, green, white_bold,
        white_bold, green, white_bold,
        white_bold, 
        white_bold, 
        white_bold, 
        white_bold, clean) + "\n" + green + clean
    
    return logo
