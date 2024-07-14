"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        items = soup.find_all('tbody')
        for item in items:
            target = item.text
            s = ''
            male_number = 0
            female_number = 0
            d_number = {}
            for i in range(len(target)):
                if target[i].isdigit() or target[i] is ' ' or target[i] is '\n':  # get the digits
                    s += target[i]
                    ss = s.split('\n')  # transform a list
            for j in range(2, 401, 2):
                sss = ss[j].split(' ')
                d_number[j] = sss  # transform a dict, which value is a list, j:[male number,female number]
            for key, value in d_number.items():
                male_number += int(value[1])
                female_number += int(value[3])
            print(f'Male Number: {male_number}')
            print(f'Female Number: {female_number}')


if __name__ == '__main__':
    main()
