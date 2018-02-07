# dominion-energy
A repository of work that I done at Dominion Energy including python scripts, macros, and a PERL application.


## Applications & Scripts

- 1 - [Pythonssh](https://github.com/VictorCanas/dominion-energy/tree/master/PythonSSH) - This python script SSH a list of hostnames found a hostfile.txt and runs the commands found in commanfile.txt and outputs it as an excel sheet. NOTE: Using Python 2.7, paramiko. xlsxwriter. With this script I was able to SSH roughly 1,700+ devices to have information such as show version which is very valuable.
- 2 - [Firewall script](#) - This python script was made to help the firewall team. This script ask the user for three inputs: 1. Enter ip address 2. Enter range: 3. Enter network:. Then it takes that input and adds a set of statemets so then the user can copy that and use it. I really enjoy writing this script in two days.
- 3 - [BPDUGuard script - SSH](#) - This python script makes use of the interactive shell when you want to SSH to a device. This particulary script was interesting to make. Once one enters a host in enable mode it asks for a password but one can't send just a command that is on a commandfile.txt rather you have to invoke a the shell to run commands. This script takes a list of hosts in hostnames which are split by commas. Some host have another enable mode password so and else if runs if authentication fails with the first enable password it goes to the other one. The ouput is an excel sheet of the hostnames and commands run on it. 
- 4 - [BPDUGuard script - Telnet](#) - This python script works the same but with telnet protocol. 
- 5 - [DNSNOW+ - PERL Application](#) - 
- 6 - [NSLOOKUP script](#) - This simple python script nslookup a list of ipaddress that are in a text file and prints the fully qualify domain of it to a csv file.
