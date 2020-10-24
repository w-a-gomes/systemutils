#!/usr/bin/env python3

"""
As logos estão separadas em arquivos únicos para evitar que o interpretador primeiro verifique
centenas de caracteres em dezenas de logos-ascii em busca de erro de sintaxe, otimizando assim
a execução do programa.
"""
# Sem 'import's em laço
def logo_design(logo="linux_kernel"):
    if logo == "linux-kernel":
        import config.logos_ascii.linux_kernel
        logo = config.logos_ascii.linux_kernel.logo()

    elif logo == "arch-linux":
        import config.logos_ascii.arch_linux
        logo = config.logos_ascii.arch_linux.logo()
    
    elif logo == "ubuntu-budgie":
        import config.logos_ascii.ubuntu_budgie
        logo = config.logos_ascii.ubuntu_budgie.logo()
        
    elif logo == "deepin":
        import config.logos_ascii.deepin
        logo = config.logos_ascii.deepin.logo()
        
    elif logo == "debian":
        import config.logos_ascii.debian
        logo = config.logos_ascii.debian.logo()
        
    elif logo == "elementary-os":
        import config.logos_ascii.elementary_os
        logo = config.logos_ascii.elementary_os.logo()

    elif logo == "endless":
        import config.logos_ascii.endless
        logo = config.logos_ascii.endless.logo()
    
    elif logo == "fedora":
        import config.logos_ascii.fedora
        logo = config.logos_ascii.fedora.logo()
        
    elif logo == "kde-neon":
        import config.logos_ascii.kde_neon
        logo = config.logos_ascii.kde_neon.logo()

    elif logo == "linux-mint":
        import config.logos_ascii.linux_mint
        logo = config.logos_ascii.linux_mint.logo()

    elif logo == "lubuntu":
        import config.logos_ascii.lubuntu
        logo = config.logos_ascii.lubuntu.logo()

    elif logo == "mageia":
        import config.logos_ascii.mageia
        logo = config.logos_ascii.mageia.logo()
        
    elif logo == "manjaro":
        import config.logos_ascii.manjaro
        logo = config.logos_ascii.manjaro.logo()

    elif logo == "mx":
        import config.logos_ascii.mx
        logo = config.logos_ascii.mx.logo()
        
    elif logo == "opensuse":
        import config.logos_ascii.opensuse
        logo = config.logos_ascii.opensuse.logo()

    elif logo == "solus":
        import config.logos_ascii.solus
        logo = config.logos_ascii.solus.logo()
        
    elif logo == "ubuntu":
        import config.logos_ascii.ubuntu
        logo = config.logos_ascii.ubuntu.logo()

    elif logo == "xubuntu":
        import config.logos_ascii.xubuntu
        logo = config.logos_ascii.xubuntu.logo()
    
    else:
        import config.logos_ascii.linux_kernel
        logo = config.logos_ascii.linux_kernel.logo()
    
    logo_lines = logo.split("\n")

    if logo_lines[0] == "":
        del(logo_lines[0])
    
    return logo_lines

def registered_logos():
    return {
        "arch-linux": 'Arch Linux', "deepin": 'Deepin', "debian": 'Debian', "elementary-os": 'Elementary OS', \
        "endless": 'Endless', "fedora": 'Fedora', "kde-neon": 'KDE neon', "linux-kernel": 'Linux kernel', \
        "linux-mint": 'Linux Mint', "lubuntu": 'Lubuntu', "mageia": "Mageia", "manjaro": 'Manjaro', "mx": 'MX', "opensuse": 'openSUSE', \
        "solus": 'Solus', "ubuntu": 'Ubuntu', "ubuntu-budgie": 'ubuntu Budgie', "xubuntu": 'Xubuntu', \
        }

# Identify some known distributions that do not configure version information as they should
def customized_logos():
    return {
        "lubuntu": {"custom-name": "Lubuntu", "cmd": "ls /usr/share/lubuntu/", "cmd-return": "openbox", \
            "name-to-replace": "Ubuntu"},

        "ubuntu-budgie": {"custom-name": "ubuntu Budgie", "cmd": "ubuntu-budgie-welcome.budgie-welcome --version", \
            "cmd-return": "Budgie Welcome", "name-to-replace": "Ubuntu"},

        "xubuntu": {"custom-name":     "Xubuntu", "cmd": "ls /usr/share/xubuntu/", "cmd-return": "applications", \
            "name-to-replace": "Ubuntu"},
        }