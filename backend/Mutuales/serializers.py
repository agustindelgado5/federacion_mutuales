from rest_framework import serializers
from Mutuales.models import mutuales, servicios, planes,beneficiosDelPlan#,servicio_mutual

class ServiciosSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = servicios
        fields = (
            'id_servicio',
            'servicio',
        )
        read_only_fields = ['id_servicio','created ','updated']


class MutualesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = mutuales
        fields = (
            'id_mutual',
            'nombre',
            'direccion',
            'localidad',
            'sucursal',
            'matricula',
            'cuit',
            'servicios_mutual',
            'email',
            'telefono',
            'representante',
            'fecha_inicio',
            'fecha_ingreso',
        )
        read_only_fields = ['id_mutual','created ','updated']


# class ServiciosMutualSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = servicio_mutual
#         fields = (
#             'id_serv_mut',
#             'id_mutual',
#             'id_servicio',
#         )
#         #read_only_fields = ['id_mutual','id_servicio']
        
class BeneficiosSerializer(serializers.HyperlinkedModelSerializer):
    #idS = serializers.ReadOnlyField(source='servicio.id_servicio')
    # servicio = serializers.ReadOnlyField(source='servicio.servicio')
    #plan = serializers.ReadOnlyField(source='plan.url')
    class Meta:
        model = beneficiosDelPlan
        #fields = '__all__'
        fields = ('id','tipo','cantidad','servicio','plan')
        #exclude=('url','cantidad')
        read_only_fields = ['plan']
    #    depth = 1
       
class PlanesSerializer(serializers.HyperlinkedModelSerializer):
    beneficios=BeneficiosSerializer(source="beneficiosdelplan_set",many=True)
    class Meta:
        model = planes
        fields = ['id_plan','nombre','precio','beneficios']
        #fields = '__all__'
        #exclude= ['servicio']
        depth = 1
        read_only_fields = ['id_plan','created ','updated']
    def create(self, validated_data):
        beneficios_data = validated_data.pop('beneficiosdelplan_set')
        plan = planes.objects.create(**validated_data)
        for b in beneficios_data:
            beneficiosDelPlan.objects.create(plan=plan, **b)
        return plan
    def update(self, instance, validated_data):
        beneficios = self.get_initial().get("beneficios")

        actualizar=[x for x in beneficios if 'id' in x.keys()]
        crear=[x for x in beneficios if 'id' not in x.keys()]
        original=instance.beneficiosdelplan_set.all()
        borrar=[x for x in original if x.id not in [z.get("id") for z in beneficios if 'id' in z.keys()]]
        
        for b in crear:
            s=servicios.objects.get(id_servicio=b.pop("servicio").split('/')[4])
            beneficiosDelPlan.objects.create(plan=instance,servicio=s, **b)
        for b in actualizar:
            bm=instance.beneficiosdelplan_set.get(id=b.get("id"))
            bm.tipo=b.get('tipo', bm.tipo)
            bm.cantidad=b.get('cantidad', bm.cantidad)
            s=servicios.objects.get(id_servicio=b.get("servicio").split('/')[4])
            bm.servicio=s
            bm.save()
        for b in borrar:
            beneficiosDelPlan.objects.filter(id=b.id).delete()

        return instance


