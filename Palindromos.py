_autor_ = 'Enrique Bello'
#palabras palindromos

palindromos = [
    'enrique bello bello enrique',
    'anita lava la tina',
    'eva usaba rimel y le miraba suave',
    986755,
    'yo hago yoga hoy',
    'a mercedes ese de crema',
    'mani inam',
    7337
]

def es_palindromo(p):
    estandar = str(p).lower().replace(' ', '')
    return estandar == estandar[::-1]

if __name__== '__main__':
  for p in palindromos:
    resultado = es_palindromo(p)
    print(resultado)