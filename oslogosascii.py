#!/usr/bin/env python3
# https://github.com/w-a-gomes/osutility

clean = "\033[0m"

red = "\033[0m\033[0;31m"
red_bold = "\033[0m\033[1;31m"
red_dark = "\033[0m\033[2;31m"
red_background = "\033[0m\033[0;31;41m"

green = "\033[0m\033[0;32m"
green_bold = "\033[0m\033[1;32m"
green_dark = "\033[0m\033[2;32m"
green_background = "\033[0m\033[0;32;42m"

yellow = "\033[0m\033[0;33m"
yellow_bold = "\033[0m\033[1;33m"
yellow_dark = "\033[0m\033[2;33m"
yellow_background = "\033[0m\033[0;33;43m"

blue = "\033[0m\033[0;34m"
blue_bold = "\033[0m\033[1;34m"
blue_dark = "\033[0m\033[2;34m"
blue_background = "\033[0m\033[0;34;44m"

purple = "\033[0m\033[0;35m"
purple_bold = "\033[0m\033[1;35m"
purple_dark = "\033[0m\033[2;35m"
purple_background = "\033[0m\033[0;35;45m"

cyan = "\033[0m\033[0;36m"
cyan_bold = "\033[0m\033[1;36m"
cyan_dark = "\033[0m\033[2;36m"
cyan_background = "\033[0m\033[0;36;46m"

white = "\033[0m\033[0;37m"
white_bold = "\033[0m\033[1;37m"
white_dark = "\033[0m\033[2;37m"
white_background = "\033[0m\033[0;37;47m"


class LogosASCII(object):
    def __init__(self, os_name):
        self.os_name = os_name
        self.logos = {
            'arch-linux': """
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
{}  """.format(blue, blue, blue, blue, blue, blue, blue,
               blue, blue, blue, blue, blue, blue, blue,
               blue, blue, blue, blue, blue,
               clean) + "\n" + blue + clean,
            'debian': """
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
{}  """.format(red, red, red, red, red, red, red,
               red, red, red, red, red, red, red,
               red, red, red, red, red,
               clean) + "\n" + red + clean,
            'deepin': """
{}               .';::::;'.               
{}          .,:looo{}xXXXXXK0O{}o:'.          
{}       .:loooooo{}kMMMMMMMX{}kooool;.       
{}     'loooooooo{}OMMMMMW{}0doooooooool'     
{}   .l{}x{}llllllll{}xMMMMW{}Ooo{}xO0XNNWWWMWO{}l.   
{}  ,d{}NW{}olllllll{}XMMM0{}x{}OxkMKNNWMMMMMMMX{}o'  
{} ,o{}WMMK{}llllllo{}MMM{}kl{}NN{}ld{}MO{}O{}N{}dk{}WMMMMMMN{}o' 
{}.l{}XMMMMO{}llllll{}MMK{}l{}0W{}dl{}0M{}dx{}MX{}lo{}NMMMMMMK{}l 
{}'d{}MMMMMM0{}lcccc{}KM{}0{}00{}ol{}kMX{}lk{}MM{}dlx{}MMMMMMM{}o'
{},x{}MMMMMMMN{}xccc{}lKW0{}x{}OXMN{}ol{}NMM{}ocl{}WMMMMMM{}d,
{}'o{}MMMMMMMMMXk{}lcc{}d0XNKk{}lo{}XMM0{}ccc{}WMMMMMM{}l.
{} c{}KMMMMMMMMMMMX{}Okdoddk{}KMMWk{}cccx{}MMMMMM0{}c 
{} 'l{}NMMMMMMMMMMMMMMMMMMWKk{}ccccl{}NMMMMMX{}c. 
{}  .cod{}xO0KKXXXXXXK0Oxoc{}:::::l{}XMMMMMK{}c.  
{}   .;:::::::::::::::::::::c{}kWMMMMW{}x;.   
{}     .;:::::::::::::::::l{}kNMMMMX{}x;.     
{}       .';::::::::::co{}OXMMMWK{}kc'.       
{}           .',;;:l{}dO00Okx{}o:'.           
{}                ...''...
{}  """.format(
                blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue,
                clean
            ) + "\n" + blue + clean,
        }

    def get_logo_as_unique_string(self) -> str:
        return self.logos[self.os_name]

    def get_logo_as_list_of_lines(self) -> list:
        return self.logos[self.os_name].split('\n')


if __name__ == '__main__':
    logos_ascii = LogosASCII('deepin')

    # Print como uma string
    print(logos_ascii.get_logo_as_unique_string())

    # Print como uma lista
    for item in logos_ascii.get_logo_as_list_of_lines():
        print(item)
