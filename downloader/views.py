from django.shortcuts import render
from pytube import YouTube
import os
from django.http import FileResponse
import re

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'home.html',{
        })
    else:
        try:
            URL = request.POST.get('url')

            download_video(URL)

            #Obtener el nombre del archivo
            titulo = YouTube(URL).title
            video_id = re.sub(r'[<>:"/\\|?*]', '', titulo)
            video_filename = f'{video_id}.mp4'

            #Construir la ruta al archivo descargado
            directorio_destino= 'videos'
            ruta_del_video = os.path.join(directorio_destino,video_filename)

            #Devolver el archivo como respuesta de archivo
            response = FileResponse(open(ruta_del_video, 'rb'), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{video_filename}"'
            return response

        except Exception as e:
            return render(request, 'home.html', {
                'error': f"Ocurrio un error porfavor vuelva a intentar {str(e)}"
            })
    

def download_video(URL):
    try:
        yt = YouTube(URL)
        yt_stream = yt.streams.get_highest_resolution()

        directorio_destino = 'videos'
        
        if not yt_stream:
            raise Exception("No se encontraron streams disponibles para la resolución más alta.")

        yt_stream.download(directorio_destino)
    except Exception as e:
        raise Exception(f"Error al descargar el video: {str(e)}")