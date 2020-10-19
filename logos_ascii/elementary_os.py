#!/usr/bin/env python3

import config.colors

def logo():
    color = config.colors.colors()

    white = color["white"]
    blue = color["blue"]
    clean = color["clean"]
    
    logo = """
{}              .',::ccc:,'.              
{}          .,:ccc{}looooool{}ccc:,.          
{}       ':ll{}ok0KKK0{}OOOO{}0KKK0ko{}ll:'       
{}     ,cl{}d0X0{}xoll{}dkOOOOkd{}llok{}KXOo{}lc;.    
{}   'cl{}dXX{}xlll{}d0Kk{}olllld{}0Nk{}llllk{}XKo{}lc,   
{}  ;ll{}0Nd{}lll{}dXXd{}lllllllll{}dMk{}lllll{}xNO{}ll:  
{} :ll{}XX{}llll{}OM0{}llllllllllll{}N0{}llllllo{}N0{}ll: 
{}'ll{}0W{}llll{}OM0{}llllllllllll{}xMd{}lllllllx{}Mk{}ll'
{}:ll{}WO{}llll{}WW{}llllllllllll{}kWx{}lllllll{}dNNN{}llc
{}clo{}Mx{}lllo{}MN{}llllllllll{}xX0o{}llllllo{}0N{}x{}OW{}llc
{}:ll{}WO{}llll{}XM{}dlllllll{}kX0o{}llllllo{}OWO{}ll{}KX{}llc
{}'ll{}OW{}olllo{}NWx{}ll{}okKKk{}llllllld{}KNO{}olld{}Mk{}ll'
{} :ll{}XX{}lllo{}xNMNWNko{}lllll{}ok0NKk{}llllo{}N0{}ll: 
{}  ;ll{}0WNNXKO{}xx{}0NWNNXNNNKOx{}llllll{}kNO{}ll:  
{}   'cld{}XXx{}llllllllllllllllllll{}kXK{}olc,   
{}     ,clo{}0XKk{}olllllllllllld{}kKXO{}olc;     
{}       ':llo{}k0KKKo{}0OO0{}oKKK0x{}oll:'       
{}          .,:cll{}XkookK{}lllc:,.           
{}              .';:cccc:;'.
{}""".format(
    blue, 
    blue, white, blue, 
    blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, white, blue, 
    blue, white, blue, white, blue, 
    blue, white, blue, white, blue, 
    blue, white, blue, white, blue, 
    blue, white, blue, 
    blue, 
    clean) + "\n" + blue + clean
    
    return logo
