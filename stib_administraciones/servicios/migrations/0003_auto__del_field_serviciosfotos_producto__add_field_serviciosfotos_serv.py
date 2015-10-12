# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ServiciosFotos.producto'
        db.delete_column(u'servicios_serviciosfotos', 'producto_id')

        # Adding field 'ServiciosFotos.servicio'
        db.add_column(u'servicios_serviciosfotos', 'servicio',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['servicios.Servicios']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ServiciosFotos.producto'
        db.add_column(u'servicios_serviciosfotos', 'producto',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['servicios.Servicios']),
                      keep_default=False)

        # Deleting field 'ServiciosFotos.servicio'
        db.delete_column(u'servicios_serviciosfotos', 'servicio_id')


    models = {
        u'servicios.servicios': {
            'Meta': {'object_name': 'Servicios'},
            'condicion_iva': ('django.db.models.fields.IntegerField', [], {}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'validez_oferta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'servicios.serviciosfotos': {
            'Meta': {'object_name': 'ServiciosFotos'},
            'comentario': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'path': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.Servicios']"})
        }
    }

    complete_apps = ['servicios']