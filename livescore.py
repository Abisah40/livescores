import requests
api_key = 'iwp8UztDScZGeiWu'
secret = 'Rmx9jwvmwdNZsLkKiKTcjnQczPSN7PiY'


def livescore(live):
    url = f'http://livescore-api.com/api-client/matches/live.json?key={api_key}&secret={secret}&lang=ar'
    if game == 'today':

        response = requests.get(url)
        #print(response)

        if response.status_code == 200:
            data = response.json()
            #print(data)
            data_1 = data.get('data')
            data_2 = data_1.get('match')
            #print(data_2)
            for data_3 in data_2:
                #print(data_3)
                home = data_3.get('home', [])
                away = data_3.get('away', [])

                if data_3:
                    print(f'{data_3['competition']['name']}')
                    print(f'HOME : {home.get('name')}') 
                    print(f'AWAY : {away.get('name')}') 
                    print(f'status : {data_3.get('status')}') 
                    print(f'schedule : {data_3.get('scheduled')}')
                    print(f'score : {data_3['scores']['score']}')  
                    print(f'time : {data_3.get('time')}')

    elif game == 'live':
        response = requests.get(url)
        if response.status_code == 200:

            data = response.json()
            data_1 = data.get('data')
            data_2 = data_1.get('match')
            # print(data_2)
            for data_3 in data_2:
            # print(i)
                home = data_3.get('home', [])
                away = data_3.get('away', [])

                if data_3['status'] == 'IN PLAY':
                    print(f'{data_3['competition']['name']}')
                    print(f'HOME : {home.get('name')}') 
                    print(f'AWAY : {away.get('name')}') 
                    print(f'status : {data_3.get('status')}') 
                    print(f'schedule : {data_3.get('scheduled')}')
                    print(f'score : {data_3['scores']['score']}')  
                    print(f'time : {data_3.get('time')}')
                 
                # print('no available live match')
        else:
            print('could not connect to the server...')
    else:
        url = f'https://livescore-api.com/api-client/teams/matches.json?number=30&team_id={game}&key={api_key}&secret={secret}'

        params = {
            'away_name':'home_name',
            'competition.name':'competition.name',
            'date':'date'
        }
        response = requests.get(url,params = params)
        #print(response)
        if response.status_code == 200:
            data = response.json()
            #print(data)
            if data['success'] == True:
                data_1 = data.get('data')
                #print(data_1)
                for data_2 in data_1:
                    if data_2:
                        print(f'{data_2.get('date')}')
                        print(f'{data_2.get('home_name')}')
                        print(f'{data_2.get('away_name')}')
                        print(f'{data_2.get('score')}')
                        print(f'{data_2.get('time')}')
                        print(f'{data_2.get('status')}')
                        print(f'{data_2['competition']['name']}')
                    else:

                        print('sorry')
game = input(('enter live / today / date(example: 2025-03-28): ').title()).strip()
livescore('live') 





