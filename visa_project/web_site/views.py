from django.shortcuts import render, HttpResponse
import folium
import geocoder
# Create your views here.

def home(request):
    return render(request, "home.html")

def acessibilidade(request):
    return render(request, "acessibilidade.html")

def map(request):

    location = geocoder.osm('recife')
    lat = location.lat
    lng = location.lng
    country = location.country

    #creating Map Object with Folium
    m = folium.Map(location=[-14.537928336797815, -40.95286772588722], zoom_start=3.5, width='100%', height='100%')

    #folium.Marker([-12.988416362561837, -38.50353491104314]).add_to(m)
    #dá pra usar essa linha de baixo pra por os pontos turisticos com o marker + infos do nome do lugar
    folium.Marker([-12.988416362561837, -38.50353491104314], tooltip='Salvador').add_to(m)
    folium.Marker([-22.90279798439243, -43.17928929265192], tooltip='Rio de Janeiro').add_to(m)

    # aqui vamo usar o form
    #folium.CircleMarker([lat, lng], tooltip=country).add_to(m)

    #Representação do mapa para o html
    m = m._repr_html_()

    context = {
        'm': m,
    }
    return render(request, 'map.html', context)
    