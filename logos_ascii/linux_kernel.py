#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    yellow = color["yellow"]
    blue = color["blue"]
    clean = color["clean"]

    logo = """
{}               .''''''''.               
{}              .'''''''''''              
{}              ,MN{}'''{}NMN:{}''.             
{}              l{}M{}N{}';'{}N{}M{}N{};'''             
{}              :{}xXMMMMXxx{}'''             
{}             .o{}xMMMMMXx'{},''.            
{}             .k{}M{}'xNNK'{}MMd{}'''.           
{}           ..{}dMMMMMMMMMMMl{}''''.         
{}          .,{}OMMMMMMMMMMMMMd{}'''''.       
{}        .'c{}NMMMMMMMMMMMMMMM0{},''''.      
{}       .'o{}MMMMMMMMMMMMMMMMMMK{}''''''.    
{}      '',{}WMMMMMMMMMMMMMMMMMMM{}:''''''    
{}     .::,x{}WMMMMMMMMMMMMMMMMMMc{}'''''.    
{}   .:kKKk{}l,d{}NMMMMMMMMMMMMMWO{}xK{}'''':{}kx   
{}dkkkkkkkkkx{};'c0{}MMMMMMMMMMMW{}kkkkxxxkkk:  
{}kkkkkkkkkkkkd{}:cX{}MMMMMMMMNko{}kkkkkkkkkkkk;
{}kkkkkkkkkkkkkko{}:lodddoc{},''{}okkkkkkkkkk'  
{}.;kkkkkkkkkkkkk{}.'''''':;..{}kkkkkkkkk'    
{}   ''':xkkkkk'           'kkkkx'
{}  """.format(
        blue,
        blue, 
        white,  blue,   white,  blue,
        white,  blue,   white,  blue,   white,  blue,   white,  blue,
        blue,   yellow, blue,
        blue,   yellow, blue,
        blue,   white,  yellow, white,  blue,
        blue,   white,  blue,
        blue,   white,  blue,
        blue,   white,  blue,
        blue,   white,  blue,
        blue,   white,  blue,
        blue,   white,  blue,
        yellow, blue,   white,  yellow,  blue,   yellow,
        yellow, blue,   white,  yellow,
        yellow, blue,   white,  yellow,
        yellow, white,  blue,   yellow,
        yellow, blue,   yellow,
        yellow, 
        clean
        ) + "\n" + yellow + clean
    
    return logo
