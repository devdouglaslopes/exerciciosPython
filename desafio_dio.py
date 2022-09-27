entrada = str(input())
T = len(entrada)

if T <= 140:
  print('TWEET')
elif T > 140:
  print('MUTE')