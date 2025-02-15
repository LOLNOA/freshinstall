
"""
Personal fresh install script
"""
import os


def blackarch_installer():
    os.system("curl -O https://blackarch.org/strap.sh")
    os.system("sudo bash strap.sh")

def package_installer(list):
    finallist = []
    with open(list) as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespace
            if line and '#' not in line:  # Check if the line is not empty and not a comment
                finallist.append(line)

    install_packages = " ".join(finallist)  # Join the list into a space-separated string

    # Run the pacman command
    if list == 'pacman_packages.txt':
        package_command = "sudo pacman -S "
    if list == 'aur_packages.txt':
        package_command = "yay -S "
    os.system(package_command + install_packages)
blackarch_installer()
package_installer('pacman_packages.txt')#