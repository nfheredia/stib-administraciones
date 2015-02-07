# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Personales'
        db.create_table(u'personales_personales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('comentario', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'personales', ['Personales'])


    def backwards(self, orm):
        # Deleting model 'Personales'
        db.delete_table(u'personales_personales')


    models = {
        u'personales.personales': {
            'Meta': {'object_name': 'Personales'},
            'comentario': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        }
    }

    complete_apps = ['personales']