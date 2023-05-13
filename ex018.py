from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ang))
print('O Ângulo de {}° tem o SENO de {:.2f}'.format(ang, seno))
coss = cos(radians(ang))
print('O Ângulo de {}° tem o COSSENO de {:.2f}'.format(ang, coss))
tang = tan(radians(ang))
print('O Ângulo de {}° tem o TANGENTE de {:.2f}'.format(ang, tang))
