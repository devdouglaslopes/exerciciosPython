h = float(input('Altura da parede(m):'))
l = float(input('Largura da parede(m):'))
area = h*l
calc = area/2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e a sua área é {:.3f}m²'.format(h,l,area))
print('Para pintar essa parede você precisará de {}l de tinta.'.format(calc))