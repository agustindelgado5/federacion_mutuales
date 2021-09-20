# from django.http import HttpResponse
# from io import BytesIO
# from django.template.loader import get_template
# from xhtml2pdf import pisa
from datetime import datetime

# #Funcion para convertir a pdf
# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')

#     return None

# Funcion para calcular la edad de una persona
def calcular_edad(fecha_nac):
    fecha_actual = datetime.now()

    if fecha_actual.year > fecha_nac.year:
        if fecha_actual.month > fecha_nac.month:
            edad = fecha_actual.year - fecha_nac.year
        elif fecha_actual.month < fecha_nac.month:
            edad = (fecha_actual.year - fecha_nac.year) - 1
        elif fecha_actual.day >= fecha_nac.day:
            edad = fecha_actual.year - fecha_nac.year
        else:
            edad = (fecha_actual.year - fecha_nac.year) - 1
    elif fecha_actual.year == fecha_nac.year:
        edad = 0
    else:
        edad = -1
    return edad
