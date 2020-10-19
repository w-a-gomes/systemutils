#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white_bold = color["white-bold"]
    cyan = color["cyan"]
    clean = color["clean"]
    
    logo = """
{}   ,xolllllllllllllllllllllllllllllllox'
{}   M                                  .W
{}   M                                  .W
{}   M        :KMx.            oWN'     .W
{}   M       'KMMMMd.        lWMO.      .W
{}   M         ,KMMMWo     cNM0'        .W
{}   M           ;XMMMWl :NMK,          .W
{}   M             :NMMMMMX;            .W
{}   M           cO' OMMMMN:            .W
{}   M         :XMMMNMNxWMMMX;          .W
{}   M       ,KMMMMMMMO. dWMMMK,:,      .W
{}   M     '0MMMMMMMMMMMd..xMMMMMM0.    .W
{}   M   .OMMMMMMMMMMMMMMWo :MMMMMMMk.  .W
{}   M .xMMMMMMMMMMMMMMMMMMWMMMMMMMMMMx..W
{}   M .'''''''''''''''''''''''''''''''..W
{}   M                                  .W
{}   M                                  .W
{}   ,dlcccccccccccccccccccccccccccccccld'
{}                                        
{}
{}""".format(white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, 
        white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, clean) + "\n" + cyan + clean
    
    return logo
