
"""
Personal fresh install setup script
"""
import os
def blackarch_installer():
    os.system("curl -O https://blackarch.org/strap.sh")
    os.system("sudo bash strap.sh")

def package_installer(list):
    finallist = []
    with open(list) as f:
        for line in f:
            line = line.strip()  
            if line and '#' not in line:  
                finallist.append(line)
    install_packages = " ".join(finallist) 
    if list == 'pacman_packages.txt' or 'blackarch_packages.txt':
        package_command = "sudo pacman -S "
    if list == 'aur_packages.txt':
        package_command = "yay -S "
    if list == 'settings.txt':
        package_command = install_packages
    
    if not finallist:
        print("PACKAGE LIST EMPTY!")
    if package_command == install_packages:
        os.system(package_command)
    else:
        os.system(package_command + install_packages)
print("""
##################################
      INSTALLING BLACKARCH KEYRING
##################################
      """)
blackarch_installer()
print(""""
######################################
           INSTALLING PACMAN PAACKAGES
######################################
""")
package_installer('pacman_packages.txt')
print("""
#############################
      INSTALLING AUR PACKAGES
#############################
""")
package_installer('aur_packages.txt')
print("""
###################################
      INSTALLING BLACKARCH PACKAGES
###################################
""")
package_installer('blackarch_packages.txt')
print("""
########################
APPPLYING OTHER COMMANDS 
########################
""")
package_installer('settings.txt')