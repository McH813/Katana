# @name:    Katana-DorkScanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana
# @author:  Adnane tebbaa (AXT)
# Main-file V1.0
"""
MIT License

Copyright (c) 2020 adnane tebbaa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import argparse
from os import system, name 
def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


print ("")
A = """             
                    |
  ,_._._._._._._._._T__________________________________________________________
  |G|o|o|g|l|e|_|_|_O_________________________________________________________/
                    R                                                           V1.5
                    |
                    
    Katana Dork Scanner (Katana-DS) coded by adnane tebbaa 
    please use -h to see help
    """
print ("")
print(A)

parser = argparse.ArgumentParser("katana-ds.py",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g","--google", help="google mode", action='store_true' )
parser.add_argument("-s","--scada", help="scada mode ", action='store_true' )
parser.add_argument("-t","--tor", help="Tor mode ", action='store_true' )
parser.add_argument("-p","--proxy", help="Proxy mode ", action='store_true' )
parser.add_argument("-b","--bitly", help="bit.ly mode ", action='store_true' )

args = parser.parse_args()

if args.google :
 clear() 
 from Modes import Gmode
 
if args.scada :
 clear ()
 from Modes import Scada
 
if args.tor :
 clear ()
 from Modes import Tor
  
if args.proxy :
 clear ()
 from Modes import Proxy

if args.bitly :
 clear ()
 from Modes import Bitly