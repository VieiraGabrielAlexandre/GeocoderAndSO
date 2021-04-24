from pygeocoder import Geocoder

endereco = "avenida paulista, 100 Sao Paulo"

print(Geocoder("Aqui token").geocode(endereco))
#