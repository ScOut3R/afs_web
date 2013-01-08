# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table('network_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('policy', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('network', ['Group'])

        # Adding M2M table for field hosts on 'Group'
        db.create_table('network_group_hosts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['network.group'], null=False)),
            ('host', models.ForeignKey(orm['network.host'], null=False))
        ))
        db.create_unique('network_group_hosts', ['group_id', 'host_id'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table('network_group')

        # Removing M2M table for field hosts on 'Group'
        db.delete_table('network_group_hosts')


    models = {
        'network.group': {
            'Meta': {'object_name': 'Group'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'grouphosts'", 'symmetrical': 'False', 'to': "orm['network.Host']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'policy': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
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