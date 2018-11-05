# Generated by Django 2.1.2 on 2018-10-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('branchesid', models.PositiveIntegerField(db_column='BranchesID', primary_key=True, serialize=False)),
                ('branchesdesc', models.CharField(db_column='BranchesDesc', max_length=45)),
                ('address', models.CharField(db_column='Address', max_length=200)),
                ('manager', models.CharField(db_column='Manager', max_length=200)),
                ('po_contactname', models.CharField(db_column='PO_ContactName', max_length=200)),
                ('contactnumbers', models.CharField(db_column='ContactNumbers', max_length=200)),
                ('tin', models.CharField(db_column='TIN', max_length=200)),
                ('pos_serialnumber', models.CharField(db_column='POS_SerialNumber', max_length=100)),
                ('pos_min', models.CharField(db_column='POS_MIN', max_length=100)),
                ('emailaddress', models.CharField(db_column='EmailAddress', max_length=100)),
                ('pos_permitnumber', models.CharField(db_column='POS_PermitNumber', max_length=200)),
                ('isenablerebates', models.PositiveIntegerField(blank=True, db_column='IsEnableRebates', null=True)),
                ('reb_slc_code', models.PositiveIntegerField(blank=True, db_column='REB_SLC_CODE', null=True)),
                ('reb_slt_code', models.PositiveIntegerField(blank=True, db_column='REB_SLT_CODE', null=True)),
                ('reb_expacct', models.PositiveIntegerField(blank=True, db_column='REB_EXPACCT', null=True)),
                ('isconsolidaterebateentries', models.PositiveIntegerField(blank=True, db_column='IsConsolidateRebateEntries', null=True)),
                ('cdaregnum', models.CharField(blank=True, db_column='CDAREGNUM', max_length=100, null=True)),
                ('acronym', models.CharField(blank=True, db_column='ACRONYM', max_length=45, null=True)),
                ('pn_location', models.CharField(blank=True, db_column='PN_LOCATION', max_length=200, null=True)),
                ('pn_ss_at', models.CharField(blank=True, db_column='PN_SS_AT', max_length=200, null=True)),
                ('td_expacct', models.PositiveIntegerField(blank=True, db_column='TD_EXPACCT', null=True)),
                ('scdiscount', models.DecimalField(db_column='SCDISCOUNT', decimal_places=2, max_digits=15)),
                ('sccoaid', models.PositiveIntegerField(blank=True, db_column='SCCOAID', null=True)),
                ('pwddiscount', models.DecimalField(db_column='PWDDISCOUNT', decimal_places=2, max_digits=15)),
                ('pwdcoaid', models.PositiveIntegerField(blank=True, db_column='PWDCOAID', null=True)),
                ('sms_ip', models.CharField(blank=True, db_column='SMS_IP', max_length=45, null=True)),
                ('sms_port', models.CharField(blank=True, db_column='SMS_PORT', max_length=10, null=True)),
                ('sms_user', models.CharField(blank=True, db_column='SMS_USER', max_length=45, null=True)),
                ('sms_pwd', models.TextField(blank=True, db_column='SMS_PWD', null=True)),
                ('iwp_url', models.TextField(blank=True, db_column='IWP_URL', null=True)),
                ('maxclients', models.TextField(blank=True, db_column='MAXCLIENTS', null=True)),
                ('srvfeecoaid', models.CharField(db_column='SRVFEECOAID', max_length=10)),
            ],
            options={
                'db_table': 'branches',
                'managed': False,
            },
        ),
    ]
