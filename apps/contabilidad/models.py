from django.db import models



from django.db import models
from django.utils import timezone


class PresupuestoPeriodo(models.Model):
    id_periodo = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_culminacion = models.DateField(default=timezone.now)
    periodo = models.DateField(verbose_name="Período de Aprobación del Presupuesto", auto_now_add = True)
    class Meta:
        managed =  True
        db_table = 'contab_presupuesto_periodo'
        verbose_name = 'Periodo Contable'
        verbose_name_plural = 'Resumen de Períodos Contables'
    
class Presupuesto(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=40)
    cantidad_aprob = models.DecimalField(max_length=6,decimal_places=2,max_digits=6)
#    moneda = 
    notas = models.TextField(max_length=200,default="Teclee Alguna Observacion sobre el Presupuesto"),
    responsable = models.CharField(max_length=40,default="Teclee el nombre del responsable del Presupuesto ")
    periodo = models.ForeignKey(PresupuestoPeriodo)

    class Meta:
        managed = True
        db_table = 'contab_presupuesto'
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Resumen de Presupuestos'
        
    def __str__(self):
        return self.nombre
        


class Contratos(models.Model):
    numero_contrato = models.CharField(max_length=10,primary_key=True,default="0000000000")
    fecha_inicio = models.DateField(default=timezone.now)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300,default="Por Favor describa le contrato")

    class Meta:
        managed = True
        db_table = 'contab_contrato'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Listado de Contratos'

    def __str__(self):
        return self.nombre    
        
        



from django.db import models
from django.utils import timezone

class Adquisicion(models.Model):
    

    COMPRA =  "CMP" 
    DONACION =  "DNC" 
    CANJE =  "CNJ"       
    EURO =  "EUR"
    PESO_CUBANO = "CUP" 
    PESO_CONVERTIBLE = "CUC" 
    DOLAR = "USD"


    TIPO_ADQUISICION_CHOICES = (
            (COMPRA,"Compra"),
            (DONACION,"Donación"),
            (CANJE,"Canje"),
    )
    
    TIPO_MONEDA_CHOICES = (
            (EURO,"Euro"),
            (PESO_CUBANO,"Peso Cubano"),
            (PESO_CONVERTIBLE,"Peso Cubano Convertible"),
            (DOLAR,"Dolar"),
    )

          
    transaccion = models.IntegerField(primary_key=True),
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_moneda = models.CharField(max_length=3,choices=TIPO_MONEDA_CHOICES,default=PESO_CONVERTIBLE )
    tipo_adquisicion = models.CharField(max_length=3,choices=TIPO_ADQUISICION_CHOICES,default=COMPRA )
    nombre_vendedor = models.ForeignKey('AdqVendedores',on_delete=models.CASCADE)
    fecha_adquisicion = models.DateTimeField(default=timezone.now)
    categoria_adquisicion = models.CharField(max_length=50) ,
    titulo_adquisicion = models.CharField(max_length=50),
    
    class Meta:
        managed = True
        db_table = 'contab_adquisicion'
        verbose_name = "Adquisición"
        verbose_name_plural = "Adquisiciones"
        
        

    def __str__(self):
        return self.titulo_adquisicion


class AdqVendedores (models.Model):
    nombre_vendedor = models.CharField(max_length=50,default="Teclee el nombre del Vendedor")
    direccion_1 = models.TextField(default="Teclee la dirección principal  del vendeddor")
    direccion_2 = models.CharField(max_length=100, null=True, blank=True)
    direccion_3 = models.CharField(max_length=100, null=True, blank=True)
    direccion_4 = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=11,null=True, blank=True)
    otro_proveedor = models.CharField(max_length=50,null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True)
    fax = models.CharField(max_length=11,null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True) 
#    url_proveedor = models.TextField(null=True, blank=True) 
    descuento = models.DecimalField(max_digits=2, decimal_places=1,default=0.00)
    es_institucion = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'contab_adq_vendedor'
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        
    
    
    def __str__(self):
        return self.nombre_vendedor

    
