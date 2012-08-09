# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Host'
        db.create_table('network_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('mac', self.gf('network.models.MACAddressField')(unique=True, max_length=17)),
            ('wifi', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('network', ['Host'])


    def backwards(self, orm):
        # Deleting model 'Host'
        db.delete_table('network_host')


    models = {
        'network.host': {
            'Meta': {'object_name': 'Host'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'entry': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'mac': ('network.models.MACAddressField', [], {'unique': 'True', 'max_length': '17'}),
            'wifi': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['network']