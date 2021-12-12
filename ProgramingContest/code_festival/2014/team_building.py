n = int(input())

team_row =(n-1)//20+1
team_column = n%20 if n%20 !=0 else 20
if team_row%2 ==0:
    print(20-team_column+1)
else:
    print(team_column)