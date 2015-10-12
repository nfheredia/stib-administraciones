# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Productos'
        db.create_table(u'productos_productos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('forma_pago', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('validez_oferta', self.gf('django.db.models.fields.IntegerField')()),
            ('condicion_iva', self.gf('django.db.models.fields.IntegerField')()),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'productos', ['Productos'])


    def backwards(self, orm):
        # Deleting model 'Productos'
        db.delete_table(u'productos_productos')


    models = {
        u'productos.productos': {
            'Meta': {'object_name': 'Productos'},
            'condicion_iva': ('django.db.models.fields.IntegerField', [], {}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'forma_pago': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'validez_oferta': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['productos']