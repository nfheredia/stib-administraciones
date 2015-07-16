# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoRelaciones'
        db.create_table(u'relaciones_tiporelaciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('comentario', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'relaciones', ['TipoRelaciones'])

        # Adding model 'RelacionesUsuariosProductos'
        db.create_table(u'relaciones_relacionesusuariosproductos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('leido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enviado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail_recibido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('tipo_relacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relaciones.TipoRelaciones'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Productos'])),
        ))
        db.send_create_signal(u'relaciones', ['RelacionesUsuariosProductos'])

        # Adding model 'RelacionesUsuariosServicios'
        db.create_table(u'relaciones_relacionesusuariosservicios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('leido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enviado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail_recibido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('tipo_relacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relaciones.TipoRelaciones'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.Servicios'])),
        ))
        db.send_create_signal(u'relaciones', ['RelacionesUsuariosServicios'])

        # Adding model 'RelacionesEdificiosProductos'
        db.create_table(u'relaciones_relacionesedificiosproductos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('leido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enviado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail_recibido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('tipo_relacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relaciones.TipoRelaciones'])),
            ('edificio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edificios.Edificios'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Productos'])),
        ))
        db.send_create_signal(u'relaciones', ['RelacionesEdificiosProductos'])

        # Adding model 'RelacionesEdificiosServicios'
        db.create_table(u'relaciones_relacionesedificiosservicios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('leido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enviado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail_recibido', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estado', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('tipo_relacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['relaciones.TipoRelaciones'])),
            ('edificio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edificios.Edificios'])),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.Servicios'])),
        ))
        db.send_create_signal(u'relaciones', ['RelacionesEdificiosServicios'])


    def backwards(self, orm):
        # Deleting model 'TipoRelaciones'
        db.delete_table(u'relaciones_tiporelaciones')

        # Deleting model 'RelacionesUsuariosProductos'
        db.delete_table(u'relaciones_relacionesusuariosproductos')

        # Deleting model 'RelacionesUsuariosServicios'
        db.delete_table(u'relaciones_relacionesusuariosservicios')

        # Deleting model 'RelacionesEdificiosProductos'
        db.delete_table(u'relaciones_relacionesedificiosproductos')

        # Deleting model 'RelacionesEdificiosServicios'
        db.delete_table(u'relaciones_relacionesedificiosservicios')


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
        u'relaciones.relacionesedificiosproductos': {
            'Meta': {'object_name': 'RelacionesEdificiosProductos'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'edificio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edificios.Edificios']"}),
            'enviado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mail_recibido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Productos']"}),
            'tipo_relacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relaciones.TipoRelaciones']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'relaciones.relacionesedificiosservicios': {
            'Meta': {'object_name': 'RelacionesEdificiosServicios'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'edificio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edificios.Edificios']"}),
            'enviado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mail_recibido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.Servicios']"}),
            'tipo_relacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relaciones.TipoRelaciones']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'relaciones.relacionesusuariosproductos': {
            'Meta': {'object_name': 'RelacionesUsuariosProductos'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enviado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mail_recibido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Productos']"}),
            'tipo_relacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relaciones.TipoRelaciones']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'relaciones.relacionesusuariosservicios': {
            'Meta': {'object_name': 'RelacionesUsuariosServicios'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enviado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mail_recibido': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['servicios.Servicios']"}),
            'tipo_relacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['relaciones.TipoRelaciones']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'relaciones.tiporelaciones': {
            'Meta': {'object_name': 'TipoRelaciones'},
            'comentario': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'servicios.servicios': {
            'Meta': {'object_name': 'Servicios'},
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

    complete_apps = ['relaciones']