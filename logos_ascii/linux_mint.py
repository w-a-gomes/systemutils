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
                                        
{}dddddddddddddddddddddddddddol:'.        
{}MMMWWWWWWWWWWWWWWWWWWNNNNNNWWMMMNk;     
{}MMM{}XXXXXKKKKK000000OOOOkkkkkxxk0{}XWMWd   
{}MMM{}KKKKKKK{}XWNX{}000OOOOkkkkkkxxxxxdd{}0WMN, 
{}MMMWWNX{}Okk{}KMMN{}kkkkk{}OKKKKO{}k{}k{}0KK0O{}dddd{}NMM,
{}llllkMMX{}kk{}0MMN{}xxx{}kNMMMMMMMMMMMMMMK{}dox{}MMX
{}    ,MMN{}xx{}0MMX{}xxx{}NMMX{}xdk{}WMMX{}xdx{}NMM0{}oo{}MMM
{}    ,MMX{}dd{}0MMX{}ddd{}WMMO{}ddd{}XMM0{}doo{}KMMK{}lo{}MMM
{}    ,MMX{}dd{}OMMX{}oo{}o{}WMMO{}ooo{}XMM0{}ooo{}KMMK{}oo{}MMM
{}    ,MMX{}oo{}OMMX{}o{}oo{}NMMO{}lll{}XMM0{}ool{}0MMK{}oo{}MMM
{}    ,MMX{}oo{}kMMX{}lllooollllooollll{}k00k{}lo{}MMM
{}    .WMW{}ol{}dWMMO{}lcccccccccccccox{}O00d{}lo{}MMM
{}     lMMK{}lco{}KMMMNNNN000000000000Od{}llo{}MMM
{}      lWMN{}xcclx{}O0000k00000000do{}lllllo{}MMM
{}       .kMMW0{}xl::::::::::::::cccccco0{}MMM
{}         .ckNMMMWNNXXXNNNNNNNNNNNNNMMMMM
{}             .';cloooooooooooooooooooooo
{}                                        
    """.format(
        white,
        white,
        white, green, white,
        white, green, white, green, white,
        white, green, white, green, white, green, cyan,  white, cyan,  white,
        white, green, white, green, white, cyan,  white,
        white, green, white, green, white, cyan,  white, cyan,  white, cyan,  white,
        white, green, white, green, white, cyan,  white, cyan,  white, cyan,  white,
        white, green, white, green, cyan,  white, cyan,  white, cyan,  white, cyan,  white,
        white, green, white, green, cyan,  white, cyan,  white, cyan,  white, cyan,  white,
        white, green, white, cyan,  white, cyan,  white,
        white, green, white, cyan,  white, cyan,  white,
        white, green, white, cyan,  white,
        white, cyan,  white, cyan,  white,
        white, cyan,  white,
        white,
        white,
        clean
        ) + "\n" + green + clean
    
    return logo
