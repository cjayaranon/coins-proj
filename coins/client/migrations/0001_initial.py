# Generated by Django 2.1.2 on 2018-10-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('accessbr_code', models.PositiveSmallIntegerField(blank=True, db_column='AccessBR_CODE', null=True)),
                ('accessid', models.PositiveSmallIntegerField(db_column='AccessID', primary_key=True, serialize=False)),
                ('accessfname', models.CharField(blank=True, db_column='AccessFName', max_length=45, null=True)),
                ('accesslname', models.CharField(blank=True, db_column='AccessLName', max_length=45, null=True)),
                ('accessmname', models.CharField(blank=True, db_column='AccessMName', max_length=45, null=True)),
                ('accesssname', models.CharField(blank=True, db_column='AccessSName', max_length=45, null=True)),
                ('accessusername', models.CharField(db_column='AccessUserName', max_length=255)),
                ('accesspassword', models.TextField(blank=True, db_column='AccessPassword', null=True)),
                ('accesslevel', models.CharField(blank=True, db_column='AccessLevel', max_length=45, null=True)),
                ('accesscurrassign', models.TextField(blank=True, db_column='AccessCurrAssign', null=True)),
                ('accesstellernumber', models.PositiveIntegerField(blank=True, db_column='AccessTellerNumber', null=True)),
                ('accessdisblimit', models.DecimalField(blank=True, db_column='AccessDisbLimit', decimal_places=2, max_digits=15, null=True)),
                ('accessconnid', models.PositiveIntegerField(blank=True, db_column='AccessConnID', null=True)),
                ('accesshost', models.CharField(blank=True, db_column='AccessHost', max_length=100, null=True)),
                ('accessdate', models.DateField(blank=True, db_column='AccessDate', null=True)),
                ('accesstime', models.TimeField(blank=True, db_column='AccessTime', null=True)),
                ('accessisheadcashier', models.PositiveIntegerField(blank=True, db_column='AccessIsHeadCashier', null=True)),
                ('accessstartday', models.PositiveIntegerField(db_column='AccessStartDay')),
                ('accessendday', models.PositiveIntegerField(db_column='AccessEndDay')),
                ('accesstagapproved', models.PositiveIntegerField(blank=True, db_column='AccessTagApproved', null=True)),
                ('accesspriorityobjname', models.CharField(blank=True, db_column='AccessPriorityObjName', max_length=45, null=True)),
                ('accessdisbursementlimit', models.DecimalField(blank=True, db_column='AccessDisbursementLimit', decimal_places=2, max_digits=15, null=True)),
                ('accesscanreverse', models.PositiveIntegerField(blank=True, db_column='AccessCanReverse', null=True)),
                ('accessposlocation', models.PositiveIntegerField(blank=True, db_column='AccessPOSLocation', null=True)),
                ('accesscangrantrebate', models.PositiveIntegerField(blank=True, db_column='AccessCanGrantRebate', null=True)),
                ('accessisdisabled', models.PositiveIntegerField(blank=True, db_column='AccessIsDisabled', null=True)),
                ('accessmaxlogins', models.PositiveSmallIntegerField(blank=True, db_column='AccessMaxLogins', null=True)),
                ('accesscanbatcheditloansetups', models.PositiveIntegerField(blank=True, db_column='AccessCanBatchEditLoanSetups', null=True)),
                ('accesscanaddnewclient', models.PositiveIntegerField(blank=True, db_column='AccessCanAddNewClient', null=True)),
                ('accesscanpostpartialpayment', models.PositiveIntegerField(blank=True, db_column='AccessCanPostPartialPayment', null=True)),
                ('accesscanpostwithhold', models.PositiveIntegerField(blank=True, db_column='AccessCanPostWithHold', null=True)),
                ('accesscaneditclientimages', models.PositiveIntegerField(blank=True, db_column='AccessCanEditClientImages', null=True)),
                ('accesscanviewitemcost', models.PositiveIntegerField(blank=True, db_column='AccessCanViewItemCost', null=True)),
                ('accesscanviewfocashcoci', models.PositiveIntegerField(blank=True, db_column='AccessCanViewFOCashCOCI', null=True)),
                ('accesscanbatchgeneratesoa', models.PositiveIntegerField(blank=True, db_column='AccessCanBatchGenerateSOA', null=True)),
                ('accesscanpostoverpayment', models.PositiveIntegerField(blank=True, db_column='AccessCanPostOverPayment', null=True)),
                ('accessatmterminalid', models.CharField(blank=True, db_column='AccessATMTerminalID', max_length=8, null=True)),
                ('accesscancreateloansetup', models.PositiveIntegerField(blank=True, db_column='AccessCanCreateLoanSetup', null=True)),
                ('accesscanaddloanapplication', models.PositiveIntegerField(blank=True, db_column='AccessCanAddLoanApplication', null=True)),
                ('accesscaneditloanapplication', models.PositiveIntegerField(blank=True, db_column='AccessCanEditLoanApplication', null=True)),
                ('accesscandeleteloanapplication', models.PositiveIntegerField(blank=True, db_column='AccessCanDeleteLoanApplication', null=True)),
                ('accesscanapproveloanapplication', models.PositiveIntegerField(blank=True, db_column='AccessCanApproveLoanApplication', null=True)),
                ('accesscanaccessbackoffice', models.PositiveIntegerField(blank=True, db_column='AccessCanAccessBackOffice', null=True)),
                ('accessexpirydate', models.DateField(blank=True, db_column='AccessExpiryDate', null=True)),
                ('accessexpiresindays', models.PositiveIntegerField(blank=True, db_column='AccessExpiresInDays', null=True)),
                ('accesslastchangepassdate', models.DateField(blank=True, db_column='AccessLastChangePassDate', null=True)),
                ('accesscangenotherforep', models.PositiveIntegerField(blank=True, db_column='AccessCanGenOtherFORep', null=True)),
                ('accesscanopenatmgw', models.PositiveIntegerField(blank=True, db_column='AccessCanOpenATMGW', null=True)),
                ('accesscanterminateuser', models.PositiveIntegerField(blank=True, db_column='AccessCanTerminateUser', null=True)),
                ('accesscanpostuncleared', models.PositiveIntegerField(blank=True, db_column='AccessCanPostUncleared', null=True)),
                ('accesscanbackdatefo', models.PositiveIntegerField(blank=True, db_column='AccessCanBackDateFO', null=True)),
                ('accesscaneditclientname', models.PositiveIntegerField(blank=True, db_column='AccessCanEditClientName', null=True)),
                ('accesscangeneratesoa', models.PositiveIntegerField(blank=True, db_column='AccessCanGenerateSOA', null=True)),
                ('accessdepartment', models.PositiveIntegerField(blank=True, db_column='AccessDepartment', null=True)),
                ('accesscanchoosedepartment', models.PositiveIntegerField(blank=True, db_column='AccessCanChooseDepartment', null=True)),
                ('accesscanaddhold', models.PositiveIntegerField(blank=True, db_column='AccessCanAddHold', null=True)),
                ('accesscandeletehold', models.PositiveIntegerField(blank=True, db_column='AccessCanDeleteHold', null=True)),
                ('accesscanmodifyhold', models.PositiveIntegerField(blank=True, db_column='AccessCanModifyHold', null=True)),
                ('accessmtmpwd', models.TextField(blank=True, db_column='AccessMTMPWD', null=True)),
                ('accessmtmtid', models.CharField(blank=True, db_column='AccessMTMTID', max_length=10, null=True)),
                ('accessrestrik', models.TextField(blank=True, db_column='AccessRestrik', null=True)),
                ('accesscanexportreport', models.PositiveIntegerField(blank=True, db_column='AccessCanExportReport', null=True)),
                ('accesscanviewactvtlogs', models.PositiveIntegerField(blank=True, db_column='AccessCanViewActvtLogs', null=True)),
                ('accesscanencodepdcfo', models.PositiveIntegerField(blank=True, db_column='AccessCanEncodePDCFO', null=True)),
                ('accesscanrunrequestserver', models.PositiveIntegerField(blank=True, db_column='AccessCanRunRequestServer', null=True)),
                ('accessclientid', models.PositiveIntegerField(blank=True, db_column='AccessClientID', null=True)),
                ('accesscangenrepnorestrict', models.PositiveIntegerField(blank=True, db_column='AccessCanGenRepNoRestrict', null=True)),
                ('accesscanviewclosedclients', models.PositiveIntegerField(blank=True, db_column='AccessCanViewClosedClients', null=True)),
                ('accesscaneditclient', models.PositiveIntegerField(blank=True, db_column='AccessCanEditClient', null=True)),
                ('accesscandeleteclient', models.PositiveIntegerField(blank=True, db_column='AccessCanDeleteClient', null=True)),
                ('accesscandodcm', models.PositiveIntegerField(blank=True, db_column='AccessCanDoDCM', null=True)),
                ('accesscanreleaseloan', models.PositiveIntegerField(blank=True, db_column='AccessCanReleaseLoan', null=True)),
                ('accesscaneditclientdept', models.PositiveIntegerField(blank=True, db_column='AccessCanEditClientDept', null=True)),
                ('accessdepballimit', models.DecimalField(blank=True, db_column='AccessDepBalLimit', decimal_places=2, max_digits=15, null=True)),
                ('accesscaneditloansetup', models.PositiveIntegerField(blank=True, db_column='AccessCanEditLoanSetup', null=True)),
                ('accesscantransactclientwarning', models.PositiveIntegerField(blank=True, db_column='AccessCanTransactClientWARNING', null=True)),
                ('accesscanregattendancenofp', models.PositiveIntegerField(blank=True, db_column='AccessCanRegAttendanceNoFP', null=True)),
                ('accesscantransactclosedclient', models.PositiveIntegerField(blank=True, db_column='AccessCanTransactClosedClient', null=True)),
                ('accessconntimeout', models.PositiveIntegerField(blank=True, db_column='AccessConnTimeOut', null=True)),
                ('accesscancloseclient', models.PositiveIntegerField(blank=True, db_column='AccessCanCloseClient', null=True)),
                ('accesscanbackdatebo', models.PositiveIntegerField(blank=True, db_column='AccessCanBackDateBO', null=True)),
                ('accesscanfuturedatebo', models.PositiveIntegerField(blank=True, db_column='AccessCanFutureDateBO', null=True)),
                ('accesscanbatchgeneratesms', models.PositiveIntegerField(blank=True, db_column='AccessCanBatchGenerateSMS', null=True)),
                ('accesscanapprovesms', models.PositiveIntegerField(blank=True, db_column='AccessCanApproveSMS', null=True)),
                ('accesscansendsms', models.PositiveIntegerField(blank=True, db_column='AccessCanSendSMS', null=True)),
                ('accesscaneditpricerr', models.PositiveIntegerField(blank=True, db_column='AccessCanEditPriceRR', null=True)),
                ('accesscanchangeposlocation', models.PositiveIntegerField(blank=True, db_column='AccessCanChangePOSLocation', null=True)),
                ('accessisclientiddefaultprompt', models.PositiveIntegerField(blank=True, db_column='AccessIsClientIDDefaultPrompt', null=True)),
                ('accessrestrictlicensedept', models.PositiveIntegerField(blank=True, db_column='AccessRestrictLicenseDept', null=True)),
            ],
            options={
                'db_table': 'access',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Acctstat',
            fields=[
                ('acctstatid', models.AutoField(db_column='AcctStatID', primary_key=True, serialize=False)),
                ('acctstatdesc', models.CharField(db_column='AcctStatDesc', max_length=45)),
            ],
            options={
                'db_table': 'acctstat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Accttype',
            fields=[
                ('acctypeid', models.AutoField(db_column='AccTypeID', primary_key=True, serialize=False)),
                ('accttypedesc', models.CharField(db_column='AcctTypeDesc', max_length=45)),
            ],
            options={
                'db_table': 'accttype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alertlevel',
            fields=[
                ('alertlevelid', models.AutoField(db_column='AlertLevelID', primary_key=True, serialize=False)),
                ('alertleveldesc', models.CharField(db_column='AlertLevelDesc', max_length=45)),
            ],
            options={
                'db_table': 'alertlevel',
                'managed': False,
            },
        ),
    ]
