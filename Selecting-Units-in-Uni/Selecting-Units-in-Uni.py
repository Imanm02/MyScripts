import requests
import json
import time

site_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
           'Accept': 'application/json',
           'Accept-Language': 'en-US,en;q=0.5',
           'Referer': 'https://my.edu.sharif.edu/courses/marked',
           'Content-Type': 'application/json',
           'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SWQiOiI5OTEwNTU2MSIsImNyZWF0ZWRBdCI6MTYzMDk5MjAxMjI1Niwic3VwZXJVc2VyIjpmYWxzZSwiaWF0IjoxNjMwOTkyMDEyfQ.1EEcP0ndpTwzDOEHMBozEk8F_pxy17dVprA98ytEx6Y',
           'Origin': 'https://my.edu.sharif.edu',
           'Connection': 'keep-alive',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'TE': 'trailers'}
courses = [('40254-1', '3'), ('40124-3', '3')]
while courses:
    for course in courses:
        site_data = '{"action":"add","course":"' + course[0] + '","units":' + course[1] + '}'
        text = requests.post('https://my.edu.sharif.edu/api/reg', headers=site_headers, data=site_data).text
        try:
            response = json.loads(text)
            if response['jobs'][0]['result'] == 'OK':
                print(course[0] + ' registered successfully.')
                courses.remove(course)
            else:
                print('couldn\'t register ' + course[0] + '. ERROR: ' + str(response['jobs'][0]['result']))
        except:
            print(text)
    time.sleep(5)
