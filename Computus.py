#!/usr/bin/python3

import sys, argparse
from datetime import date, timedelta

def computus(self, year):
    #Returns Easter as a date object.
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return date(year, month, day)

parser = argparse.ArgumentParser(prog='computus', description='Computus algorithm: Returns Easter time and the holidays that are related to it.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0. (CC) 2019 Rodrigo Vegas Sánchez-Ferrero.')
parser.add_argument('-c', '--carnival', action='store_true', help='Carnival time')
parser.add_argument('-a', '--ash', action='store_true', help='Ash Wednesday')
parser.add_argument('-p', '--palm', action='store_true', help='Palm Sunday')
parser.add_argument('-e', '--easter', action='store_true', help='Easter')
parser.add_argument('-w', '--holyweek', action='store_true', help='Holy Week')
parser.add_argument('year', type=int, nargs='?', help='Any year number from 1583')

args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

if args.year: year = args.year
else: year = date.today().year

easter = computus([], year)

if args.carnival:
    for i in [50, 49, 48]:
        print((easter - timedelta(days=i)).strftime("%d/%m/%Y, Carnival %A."))
    print((easter - timedelta(days=i-1)).strftime("%d/%m/%Y, Carnival %A or Mardi Gras."))

if args.ash: print((easter - timedelta(days=46)).strftime("%d/%m/%Y, Ash %A. First day of Lent."))

if args.palm: print((easter - timedelta(days=7)).strftime("%d/%m/%Y, Palm %A."))

if args.holyweek:
    for key, value in {'Maundy': 3, 'Good': 2, 'Holy': 1}.items():
        print((easter - timedelta(days=value)).strftime("%d/%m/%Y,"),key,(easter - timedelta(days=value)).strftime("%A."))
    args.easter = 'e'

if args.easter:
    if year >= 1583: print(easter.strftime("%d/%m/%Y, Easter. %A."))
    else: print("Error: The year must be an integer greater than 1583.")
