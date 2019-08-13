def suma_complejos(c1,c2):
    return ((c1[0]+c2[0]),(c1[1]+c2[1]))
def resta_complejos(c1,c2):
    return ((c1[0]-c2[0]),(c1[1]-c2[1]))
def producto_complejos(c1,c2):
    real=(c1[0]*c2[0])-(c1[1]*c2[1])
    ima=(c1[0]*c2[1])+(c1[1]*c2[0])
    return ((real,ima))
def division_complejos(c1,c2):
    deno=producto_complejos(c2,(c2[0],(c2[1]*-1)))
    num=producto_complejos(c1,(c2[0],(c2[1]*-1)))
    return ((num[0]/deno[0]),num[1]/deno[1])
def modulo_complejos(c1):
    return ((c1[0]**2)+(c1[1]**2))**.5
def conjugado_complejos(c1,c2):
    return 0
def conversion_polar_cartesiano(c1,c2):
    return 0
def fase_complejo(c1,c2):
    return 0
