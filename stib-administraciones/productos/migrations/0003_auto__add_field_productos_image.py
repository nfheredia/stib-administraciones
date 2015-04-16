# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Productos.image'
        db.add_column(u'productos_productos', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Productos.image'
        db.delete_column(u'productos_productos', 'image')


    models = {
        u'productos.productos': {
            'Meta': {'object_name': 'Productos'},
            'condicion_iva': ('django.db.models.fields.IntegerField', [], {}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'validez_oferta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'productos.productosfotos': {
            'Meta': {'object_name': 'ProductosFotos'},
            'comentario': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'path': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Productos']"})
        }
    }

    complete_apps = ['productos']