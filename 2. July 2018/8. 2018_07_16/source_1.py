from geopy import Nominatim


if __name__ == '__main__':
    geo = Nominatim()
    x = geo.geocode('Москва, Кирпичная 33')
    print(x)