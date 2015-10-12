# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contactos'
        db.create_table(u'contactos_contactos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('edificio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edificios.Edificios'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('piso', self.gf('django.db.models.fields.IntegerField')(max_length=2, blank=True)),
            ('departamente', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('comentario', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'contactos', ['Contactos'])

        # Adding model 'HorariosContactos'
        db.create_table(u'contactos_horarioscontactos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('contacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contactos.Contactos'])),
            ('lunes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('martes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('miercoles', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('jueves', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('viernes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sabado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('domingo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hora_desde', self.gf('django.db.models.fields.TimeField')()),
            ('hora_hasta', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'contactos', ['HorariosContactos'])


    def backwards(self, orm):
        # Deleting model 'Contactos'
        db.delete_table(u'contactos_contactos')

        # Deleting model 'HorariosContactos'
        db.delete_table(u'contactos_horarioscontactos')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contactos.contactos': {
            'Meta': {'object_name': 'Contactos'},
            'comentario': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'departamente': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'edificio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edificios.Edificios']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'contactos.horarioscontactos': {
            'Meta': {'object_name': 'HorariosContactos'},
            'contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contactos.Contactos']"}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domingo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hora_desde': ('django.db.models.fields.TimeField', [], {}),
            'hora_hasta': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jueves': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lunes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'martes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'miercoles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'viernes': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'edificios.edificios': {
            'Meta': {'object_name': 'Edificios'},
            'cantidad_pisos': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cantidad_unidades': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'comentario': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'foto_fachada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['contactos']