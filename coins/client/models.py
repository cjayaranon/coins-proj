# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Access(models.Model):
    accessbr_code = models.PositiveSmallIntegerField(db_column='AccessBR_CODE', blank=True, null=True)  # Field name made lowercase.
    accessid = models.PositiveSmallIntegerField(db_column='AccessID', primary_key=True)  # Field name made lowercase.
    accessfname = models.CharField(db_column='AccessFName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accesslname = models.CharField(db_column='AccessLName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accessmname = models.CharField(db_column='AccessMName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accesssname = models.CharField(db_column='AccessSName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accessusername = models.CharField(db_column='AccessUserName', max_length=255)  # Field name made lowercase.
    accesspassword = models.TextField(db_column='AccessPassword', blank=True, null=True)  # Field name made lowercase.
    accesslevel = models.CharField(db_column='AccessLevel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accesscurrassign = models.TextField(db_column='AccessCurrAssign', blank=True, null=True)  # Field name made lowercase.
    accesstellernumber = models.PositiveIntegerField(db_column='AccessTellerNumber', blank=True, null=True)  # Field name made lowercase.
    accessdisblimit = models.DecimalField(db_column='AccessDisbLimit', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accessconnid = models.PositiveIntegerField(db_column='AccessConnID', blank=True, null=True)  # Field name made lowercase.
    accesshost = models.CharField(db_column='AccessHost', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accessdate = models.DateField(db_column='AccessDate', blank=True, null=True)  # Field name made lowercase.
    accesstime = models.TimeField(db_column='AccessTime', blank=True, null=True)  # Field name made lowercase.
    accessisheadcashier = models.PositiveIntegerField(db_column='AccessIsHeadCashier', blank=True, null=True)  # Field name made lowercase.
    accessstartday = models.PositiveIntegerField(db_column='AccessStartDay')  # Field name made lowercase.
    accessendday = models.PositiveIntegerField(db_column='AccessEndDay')  # Field name made lowercase.
    accesstagapproved = models.PositiveIntegerField(db_column='AccessTagApproved', blank=True, null=True)  # Field name made lowercase.
    accesspriorityobjname = models.CharField(db_column='AccessPriorityObjName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accessdisbursementlimit = models.DecimalField(db_column='AccessDisbursementLimit', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accesscanreverse = models.PositiveIntegerField(db_column='AccessCanReverse', blank=True, null=True)  # Field name made lowercase.
    accessposlocation = models.PositiveIntegerField(db_column='AccessPOSLocation', blank=True, null=True)  # Field name made lowercase.
    accesscangrantrebate = models.PositiveIntegerField(db_column='AccessCanGrantRebate', blank=True, null=True)  # Field name made lowercase.
    accessisdisabled = models.PositiveIntegerField(db_column='AccessIsDisabled', blank=True, null=True)  # Field name made lowercase.
    accessmaxlogins = models.PositiveSmallIntegerField(db_column='AccessMaxLogins', blank=True, null=True)  # Field name made lowercase.
    accesscanbatcheditloansetups = models.PositiveIntegerField(db_column='AccessCanBatchEditLoanSetups', blank=True, null=True)  # Field name made lowercase.
    accesscanaddnewclient = models.PositiveIntegerField(db_column='AccessCanAddNewClient', blank=True, null=True)  # Field name made lowercase.
    accesscanpostpartialpayment = models.PositiveIntegerField(db_column='AccessCanPostPartialPayment', blank=True, null=True)  # Field name made lowercase.
    accesscanpostwithhold = models.PositiveIntegerField(db_column='AccessCanPostWithHold', blank=True, null=True)  # Field name made lowercase.
    accesscaneditclientimages = models.PositiveIntegerField(db_column='AccessCanEditClientImages', blank=True, null=True)  # Field name made lowercase.
    accesscanviewitemcost = models.PositiveIntegerField(db_column='AccessCanViewItemCost', blank=True, null=True)  # Field name made lowercase.
    accesscanviewfocashcoci = models.PositiveIntegerField(db_column='AccessCanViewFOCashCOCI', blank=True, null=True)  # Field name made lowercase.
    accesscanbatchgeneratesoa = models.PositiveIntegerField(db_column='AccessCanBatchGenerateSOA', blank=True, null=True)  # Field name made lowercase.
    accesscanpostoverpayment = models.PositiveIntegerField(db_column='AccessCanPostOverPayment', blank=True, null=True)  # Field name made lowercase.
    accessatmterminalid = models.CharField(db_column='AccessATMTerminalID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    accesscancreateloansetup = models.PositiveIntegerField(db_column='AccessCanCreateLoanSetup', blank=True, null=True)  # Field name made lowercase.
    accesscanaddloanapplication = models.PositiveIntegerField(db_column='AccessCanAddLoanApplication', blank=True, null=True)  # Field name made lowercase.
    accesscaneditloanapplication = models.PositiveIntegerField(db_column='AccessCanEditLoanApplication', blank=True, null=True)  # Field name made lowercase.
    accesscandeleteloanapplication = models.PositiveIntegerField(db_column='AccessCanDeleteLoanApplication', blank=True, null=True)  # Field name made lowercase.
    accesscanapproveloanapplication = models.PositiveIntegerField(db_column='AccessCanApproveLoanApplication', blank=True, null=True)  # Field name made lowercase.
    accesscanaccessbackoffice = models.PositiveIntegerField(db_column='AccessCanAccessBackOffice', blank=True, null=True)  # Field name made lowercase.
    accessexpirydate = models.DateField(db_column='AccessExpiryDate', blank=True, null=True)  # Field name made lowercase.
    accessexpiresindays = models.PositiveIntegerField(db_column='AccessExpiresInDays', blank=True, null=True)  # Field name made lowercase.
    accesslastchangepassdate = models.DateField(db_column='AccessLastChangePassDate', blank=True, null=True)  # Field name made lowercase.
    accesscangenotherforep = models.PositiveIntegerField(db_column='AccessCanGenOtherFORep', blank=True, null=True)  # Field name made lowercase.
    accesscanopenatmgw = models.PositiveIntegerField(db_column='AccessCanOpenATMGW', blank=True, null=True)  # Field name made lowercase.
    accesscanterminateuser = models.PositiveIntegerField(db_column='AccessCanTerminateUser', blank=True, null=True)  # Field name made lowercase.
    accesscanpostuncleared = models.PositiveIntegerField(db_column='AccessCanPostUncleared', blank=True, null=True)  # Field name made lowercase.
    accesscanbackdatefo = models.PositiveIntegerField(db_column='AccessCanBackDateFO', blank=True, null=True)  # Field name made lowercase.
    accesscaneditclientname = models.PositiveIntegerField(db_column='AccessCanEditClientName', blank=True, null=True)  # Field name made lowercase.
    accesscangeneratesoa = models.PositiveIntegerField(db_column='AccessCanGenerateSOA', blank=True, null=True)  # Field name made lowercase.
    accessdepartment = models.PositiveIntegerField(db_column='AccessDepartment', blank=True, null=True)  # Field name made lowercase.
    accesscanchoosedepartment = models.PositiveIntegerField(db_column='AccessCanChooseDepartment', blank=True, null=True)  # Field name made lowercase.
    accesscanaddhold = models.PositiveIntegerField(db_column='AccessCanAddHold', blank=True, null=True)  # Field name made lowercase.
    accesscandeletehold = models.PositiveIntegerField(db_column='AccessCanDeleteHold', blank=True, null=True)  # Field name made lowercase.
    accesscanmodifyhold = models.PositiveIntegerField(db_column='AccessCanModifyHold', blank=True, null=True)  # Field name made lowercase.
    accessmtmpwd = models.TextField(db_column='AccessMTMPWD', blank=True, null=True)  # Field name made lowercase.
    accessmtmtid = models.CharField(db_column='AccessMTMTID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accessrestrik = models.TextField(db_column='AccessRestrik', blank=True, null=True)  # Field name made lowercase.
    accesscanexportreport = models.PositiveIntegerField(db_column='AccessCanExportReport', blank=True, null=True)  # Field name made lowercase.
    accesscanviewactvtlogs = models.PositiveIntegerField(db_column='AccessCanViewActvtLogs', blank=True, null=True)  # Field name made lowercase.
    accesscanencodepdcfo = models.PositiveIntegerField(db_column='AccessCanEncodePDCFO', blank=True, null=True)  # Field name made lowercase.
    accesscanrunrequestserver = models.PositiveIntegerField(db_column='AccessCanRunRequestServer', blank=True, null=True)  # Field name made lowercase.
    accessclientid = models.PositiveIntegerField(db_column='AccessClientID', blank=True, null=True)  # Field name made lowercase.
    accesscangenrepnorestrict = models.PositiveIntegerField(db_column='AccessCanGenRepNoRestrict', blank=True, null=True)  # Field name made lowercase.
    accesscanviewclosedclients = models.PositiveIntegerField(db_column='AccessCanViewClosedClients', blank=True, null=True)  # Field name made lowercase.
    accesscaneditclient = models.PositiveIntegerField(db_column='AccessCanEditClient', blank=True, null=True)  # Field name made lowercase.
    accesscandeleteclient = models.PositiveIntegerField(db_column='AccessCanDeleteClient', blank=True, null=True)  # Field name made lowercase.
    accesscandodcm = models.PositiveIntegerField(db_column='AccessCanDoDCM', blank=True, null=True)  # Field name made lowercase.
    accesscanreleaseloan = models.PositiveIntegerField(db_column='AccessCanReleaseLoan', blank=True, null=True)  # Field name made lowercase.
    accesscaneditclientdept = models.PositiveIntegerField(db_column='AccessCanEditClientDept', blank=True, null=True)  # Field name made lowercase.
    accessdepballimit = models.DecimalField(db_column='AccessDepBalLimit', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accesscaneditloansetup = models.PositiveIntegerField(db_column='AccessCanEditLoanSetup', blank=True, null=True)  # Field name made lowercase.
    accesscantransactclientwarning = models.PositiveIntegerField(db_column='AccessCanTransactClientWARNING', blank=True, null=True)  # Field name made lowercase.
    accesscanregattendancenofp = models.PositiveIntegerField(db_column='AccessCanRegAttendanceNoFP', blank=True, null=True)  # Field name made lowercase.
    accesscantransactclosedclient = models.PositiveIntegerField(db_column='AccessCanTransactClosedClient', blank=True, null=True)  # Field name made lowercase.
    accessconntimeout = models.PositiveIntegerField(db_column='AccessConnTimeOut', blank=True, null=True)  # Field name made lowercase.
    accesscancloseclient = models.PositiveIntegerField(db_column='AccessCanCloseClient', blank=True, null=True)  # Field name made lowercase.
    accesscanbackdatebo = models.PositiveIntegerField(db_column='AccessCanBackDateBO', blank=True, null=True)  # Field name made lowercase.
    accesscanfuturedatebo = models.PositiveIntegerField(db_column='AccessCanFutureDateBO', blank=True, null=True)  # Field name made lowercase.
    accesscanbatchgeneratesms = models.PositiveIntegerField(db_column='AccessCanBatchGenerateSMS', blank=True, null=True)  # Field name made lowercase.
    accesscanapprovesms = models.PositiveIntegerField(db_column='AccessCanApproveSMS', blank=True, null=True)  # Field name made lowercase.
    accesscansendsms = models.PositiveIntegerField(db_column='AccessCanSendSMS', blank=True, null=True)  # Field name made lowercase.
    accesscaneditpricerr = models.PositiveIntegerField(db_column='AccessCanEditPriceRR', blank=True, null=True)  # Field name made lowercase.
    accesscanchangeposlocation = models.PositiveIntegerField(db_column='AccessCanChangePOSLocation', blank=True, null=True)  # Field name made lowercase.
    accessisclientiddefaultprompt = models.PositiveIntegerField(db_column='AccessIsClientIDDefaultPrompt', blank=True, null=True)  # Field name made lowercase.
    accessrestrictlicensedept = models.PositiveIntegerField(db_column='AccessRestrictLicenseDept', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return u"%s %s" % (self.accessfname, self.accesslname)

    class Meta:
        managed = False
        db_table = 'access'


class Acctstat(models.Model):
    acctstatid = models.AutoField(db_column='AcctStatID', primary_key=True)  # Field name made lowercase.
    acctstatdesc = models.CharField(db_column='AcctStatDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.acctstatdesc

    class Meta:
        managed = False
        db_table = 'acctstat'


class Accttype(models.Model):
    acctypeid = models.AutoField(db_column='AccTypeID', primary_key=True)  # Field name made lowercase.
    accttypedesc = models.CharField(db_column='AcctTypeDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.accttypedesc

    class Meta:
        managed = False
        db_table = 'accttype'


class Alertlevel(models.Model):
    alertlevelid = models.AutoField(db_column='AlertLevelID', primary_key=True)  # Field name made lowercase.
    alertleveldesc = models.CharField(db_column='AlertLevelDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.alertleveldesc

    class Meta:
        managed = False
        db_table = 'alertlevel'


class Branches(models.Model):
    branchesid = models.PositiveIntegerField(db_column='BranchesID', primary_key=True)  # Field name made lowercase. FOREIGN KEY TO COA
    branchesdesc = models.CharField(db_column='BranchesDesc', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=200)  # Field name made lowercase.
    po_contactname = models.CharField(db_column='PO_ContactName', max_length=200)  # Field name made lowercase.
    contactnumbers = models.CharField(db_column='ContactNumbers', max_length=200)  # Field name made lowercase.
    tin = models.CharField(db_column='TIN', max_length=200)  # Field name made lowercase.
    pos_serialnumber = models.CharField(db_column='POS_SerialNumber', max_length=100)  # Field name made lowercase.
    pos_min = models.CharField(db_column='POS_MIN', max_length=100)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=100)  # Field name made lowercase.
    pos_permitnumber = models.CharField(db_column='POS_PermitNumber', max_length=200)  # Field name made lowercase.
    isenablerebates = models.PositiveIntegerField(db_column='IsEnableRebates', blank=True, null=True)  # Field name made lowercase.
    reb_slc_code = models.PositiveIntegerField(db_column='REB_SLC_CODE', blank=True, null=True)  # Field name made lowercase. Foreign key to Sltype
    reb_slt_code = models.PositiveIntegerField(db_column='REB_SLT_CODE', blank=True, null=True)  # Field name made lowercase. Foreign key to Sltype
    reb_expacct = models.PositiveIntegerField(db_column='REB_EXPACCT', blank=True, null=True)  # Field name made lowercase. Foreign key to COA
    isconsolidaterebateentries = models.PositiveIntegerField(db_column='IsConsolidateRebateEntries', blank=True, null=True)  # Field name made lowercase.
    cdaregnum = models.CharField(db_column='CDAREGNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acronym = models.CharField(db_column='ACRONYM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pn_location = models.CharField(db_column='PN_LOCATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pn_ss_at = models.CharField(db_column='PN_SS_AT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    td_expacct = models.PositiveIntegerField(db_column='TD_EXPACCT', blank=True, null=True)  # Field name made lowercase. Foreign key to Coa
    scdiscount = models.DecimalField(db_column='SCDISCOUNT', max_digits=15, decimal_places=2)  # Field name made lowercase.
    sccoaid = models.PositiveIntegerField(db_column='SCCOAID', blank=True, null=True)  # Field name made lowercase. Foreign key to Coa
    pwddiscount = models.DecimalField(db_column='PWDDISCOUNT', max_digits=15, decimal_places=2)  # Field name made lowercase.
    pwdcoaid = models.PositiveIntegerField(db_column='PWDCOAID', blank=True, null=True)  # Field name made lowercase. Foreign key to Coa
    sms_ip = models.CharField(db_column='SMS_IP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sms_port = models.CharField(db_column='SMS_PORT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sms_user = models.CharField(db_column='SMS_USER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sms_pwd = models.TextField(db_column='SMS_PWD', blank=True, null=True)  # Field name made lowercase.
    iwp_url = models.TextField(db_column='IWP_URL', blank=True, null=True)  # Field name made lowercase.
    maxclients = models.TextField(db_column='MAXCLIENTS', blank=True, null=True)  # Field name made lowercase.
    srvfeecoaid = models.CharField(db_column='SRVFEECOAID', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.branchesdesc

    class Meta:
        managed = False
        db_table = 'branches'


class Buslevel(models.Model):
    buslevelid = models.AutoField(db_column='BusLevelID', primary_key=True)  # Field name made lowercase.
    busleveldesc = models.CharField(db_column='BusLevelDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.busleveldesc

    class Meta:
        managed = False
        db_table = 'buslevel'


class Busstatus(models.Model):
    busstatusid = models.AutoField(db_column='BusStatusID', primary_key=True)  # Field name made lowercase.
    busstatusdesc = models.CharField(db_column='BusStatusDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.busstatusdesc

    class Meta:
        managed = False
        db_table = 'busstatus'


class Civilstat(models.Model):
    civilstatid = models.AutoField(db_column='CivilStatID', primary_key=True)  # Field name made lowercase.
    civilstatdesc = models.CharField(db_column='CivilStatDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.civilstatdesc

    class Meta:
        managed = False
        db_table = 'civilstat'


class Clienttype(models.Model):
    clienttypeid = models.AutoField(db_column='ClientTypeID', primary_key=True)  # Field name made lowercase.
    clienttypedesc = models.CharField(db_column='ClientTypeDesc', max_length=45)  # Field name made lowercase.
    clienttypeistaxable = models.PositiveIntegerField(db_column='ClientTypeIsTaxable')  # Field name made lowercase.

    def __str__(self):
        return self.clienttypedesc

    class Meta:
        managed = False
        db_table = 'clienttype'


class Jnttype(models.Model):
    jnttypeid = models.AutoField(db_column='JntTypeID', primary_key=True)  # Field name made lowercase.
    jnttypedesc = models.CharField(db_column='JntTypeDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.jnttypedesc

    class Meta:
        managed = False
        db_table = 'jnttype'


class Gender(models.Model):
    genderid = models.AutoField(db_column='GenderID', primary_key=True)  # Field name made lowercase.
    genderdesc = models.CharField(db_column='GenderDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.genderdesc

    class Meta:
        managed = False
        db_table = 'gender'


class Educattained(models.Model):
    educattainedid = models.AutoField(db_column='EducAttainedID', primary_key=True)  # Field name made lowercase.
    educattaineddesc = models.CharField(db_column='EducAttainedDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.educattaineddesc

    class Meta:
        managed = False
        db_table = 'educattained'


class Sector(models.Model):
    sectorid = models.PositiveIntegerField(db_column='SectorID', primary_key=True)  # Field name made lowercase.
    sectordesc = models.CharField(db_column='SectorDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.sectordesc

    class Meta:
        managed = False
        db_table = 'sector'


class Occu(models.Model):
    occuid = models.PositiveSmallIntegerField(db_column='OccuID', primary_key=True)  # Field name made lowercase.
    occudesc = models.CharField(db_column='OccuDesc', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.occudesc

    class Meta:
        managed = False
        db_table = 'occu'


class Geo(models.Model):
    geoid = models.PositiveSmallIntegerField(db_column='GeoID', primary_key=True)  # Field name made lowercase.
    geodesc = models.CharField(db_column='GeoDesc', max_length=45)  # Field name made lowercase.
    geobr_code = models.ForeignKey(Branches, models.DO_NOTHING, db_column='GeoBR_CODE')  # Field name made lowercase.
    geoupduser = models.ForeignKey(Access, models.DO_NOTHING, db_column='GeoUpdUser', blank=True, null=True)  # Field name made lowercase.
    geoupddatetime = models.DateTimeField(db_column='GeoUpdDateTime', blank=True, null=True)  # Field name made lowercase.
    geocollchartid = models.PositiveIntegerField(db_column='GeoCollChartID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.geodesc

    class Meta:
        managed = False
        db_table = 'geo'
        unique_together = (('geobr_code', 'geoid'),)


class Mailingaddress(models.Model):
    mailingaddressid = models.AutoField(db_column='MailingAddressID', primary_key=True)  # Field name made lowercase.
    mailingaddressdesc = models.CharField(db_column='MailingAddressDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.mailingaddressdesc

    class Meta:
        managed = False
        db_table = 'mailingaddress'


class Restype(models.Model):
    restypeid = models.AutoField(db_column='ResTypeID', primary_key=True)  # Field name made lowercase.
    restypedesc = models.CharField(db_column='ResTypeDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.restypedesc

    class Meta:
        managed = False
        db_table = 'restype'


class Indu(models.Model):
    induid = models.PositiveSmallIntegerField(db_column='InduID', primary_key=True)  # Field name made lowercase.
    indudesc = models.CharField(db_column='InduDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ciccode = models.CharField(db_column='CICCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.indudesc

    class Meta:
        managed = False
        db_table = 'indu'


class Industry(models.Model):
    industryid = models.PositiveSmallIntegerField(db_column='IndustryID', primary_key=True)  # Field name made lowercase.
    industrydesc = models.CharField(db_column='IndustryDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indugrp = models.CharField(db_column='InduGrp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ciccode = models.CharField(db_column='CICCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.industrydesc

    class Meta:
        managed = False
        db_table = 'industry'


class Closedreason(models.Model):
    closedreasonid = models.AutoField(db_column='ClosedReasonID', primary_key=True)  # Field name made lowercase.
    closedreasondesc = models.CharField(db_column='ClosedReasonDesc', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.closedreasondesc

    class Meta:
        managed = False
        db_table = 'closedreason'


class Rating(models.Model):
    ratingid = models.AutoField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    ratingdesc = models.CharField(db_column='RatingDesc', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.ratingdesc

    class Meta:
        managed = False
        db_table = 'rating'


class Dosritag(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    desc1 = models.CharField(db_column='DESC1', max_length=45)  # Field name made lowercase.
    desc2 = models.CharField(db_column='DESC2', max_length=200, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.desc1

    class Meta:
        managed = False
        db_table = 'dosritag'


class Empcode(models.Model):
    empcodeid = models.PositiveIntegerField(db_column='EmpCodeID', primary_key=True)  # Field name made lowercase.
    empcodedesc = models.CharField(db_column='EmpCodeDesc', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.empcodedesc

    class Meta:
        managed = False
        db_table = 'empcode'


class Dept(models.Model):
    deptid = models.AutoField(db_column='DeptID', primary_key=True)  # Field name made lowercase.
    deptdesc = models.CharField(db_column='DeptDesc', max_length=30)  # Field name made lowercase.
    deptparentid = models.ForeignKey('self', models.DO_NOTHING, db_column='DeptParentID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.deptdesc

    class Meta:
        managed = False
        db_table = 'dept'


class Restrik(models.Model):
    restrikid = models.PositiveIntegerField(db_column='RestrikID', primary_key=True)  # Field name made lowercase.
    restrikdesc = models.CharField(db_column='RestrikDesc', max_length=200)  # Field name made lowercase.

    def __str__(self):
        return self.restrikdesc

    class Meta:
        managed = False
        db_table = 'restrik'


class School(models.Model):
    schoolid = models.PositiveSmallIntegerField(db_column='SchoolID', primary_key=True)  # Field name made lowercase.
    schooldesc = models.CharField(db_column='SchoolDesc', max_length=200)  # Field name made lowercase.

    def __str__(self):
        return self.schooldesc

    class Meta:
        managed = False
        db_table = 'school'


class Section(models.Model):
    sectionid = models.PositiveSmallIntegerField(db_column='SectionID', primary_key=True)  # Field name made lowercase.
    sectiondesc = models.CharField(db_column='SectionDesc', max_length=200)  # Field name made lowercase.

    def __str__(self):
        return self.sectiondesc

    class Meta:
        managed = False
        db_table = 'section'


class Grouping(models.Model):
    br_code = models.ForeignKey('self', models.DO_NOTHING, db_column='BR_CODE', related_name='branches')  # Field name made lowercase.
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    desc1 = models.CharField(db_column='DESC1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENT', blank=True, null=True)  # Field name made lowercase.
    clientid = models.PositiveIntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase. Foreign Key Client

    def __str__(self):
        return self.desc1

    class Meta:
        managed = False
        db_table = 'grouping'
        unique_together = (('br_code', 'id'),)


class Client(models.Model):
    clientidbrcode = models.ForeignKey(Branches, models.DO_NOTHING, db_column='ClientIDBrCode')  # Field name made lowercase.
    clientid = models.PositiveIntegerField(db_column='ClientID', primary_key=True)  # Field name made lowercase.
    clientidchkdgt = models.PositiveIntegerField(db_column='ClientIDChkDgt')  # Field name made lowercase.
    oldclientid = models.CharField(db_column='OldClientID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oldpsbn = models.CharField(db_column='OldPSBN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', max_length=5, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collector = models.PositiveIntegerField(db_column='Collector', blank=True, null=True)  # Field name made lowercase. Foreign key to Collchart
    dateopened = models.DateTimeField(db_column='DateOpened', blank=True, null=True)  # Field name made lowercase.
    accounttype = models.ForeignKey(Accttype, models.DO_NOTHING, db_column='AccountType', blank=True, null=True)  # Field name made lowercase.
    clienttype = models.ForeignKey(Clienttype, models.DO_NOTHING, db_column='ClientType', blank=True, null=True)  # Field name made lowercase.
    accountstatus = models.ForeignKey(Acctstat, models.DO_NOTHING, db_column='AccountStatus', blank=True, null=True)  # Field name made lowercase.
    alertlevel = models.ForeignKey(Alertlevel, models.DO_NOTHING, db_column='AlertLevel', blank=True, null=True)  # Field name made lowercase.
    jointtype = models.ForeignKey(Jnttype, models.DO_NOTHING, db_column='JointType', blank=True, null=True)  # Field name made lowercase.
    oldclientname = models.CharField(db_column='OldClientName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    gender = models.ForeignKey(Gender, models.DO_NOTHING, db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    civilstatus = models.ForeignKey(Civilstat, models.DO_NOTHING, db_column='CivilStatus', blank=True, null=True)  # Field name made lowercase.
    educattained = models.ForeignKey(Educattained, models.DO_NOTHING, db_column='EducAttained', blank=True, null=True)  # Field name made lowercase.
    tinnum = models.CharField(db_column='TINNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctcnumber = models.CharField(db_column='CTCNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sssgsisnum = models.CharField(db_column='SSSGSISNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    philhealthnum = models.CharField(db_column='PhilHealthNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pagibignum = models.CharField(db_column='PagibigNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    atmbank = models.CharField(db_column='ATMBank', max_length=30, blank=True, null=True)  # Field name made lowercase.
    atmnum = models.CharField(db_column='ATMNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    schoollastattended = models.CharField(db_column='SchoolLastAttended', max_length=30, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sectoral = models.ForeignKey(Sector, models.DO_NOTHING, db_column='Sectoral', blank=True, null=True)  # Field name made lowercase.
    occupational = models.ForeignKey(Occu, models.DO_NOTHING, db_column='Occupational', blank=True, null=True)  # Field name made lowercase.
    geographical = models.ForeignKey(Geo, models.DO_NOTHING, db_column='Geographical', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    restelnum = models.CharField(db_column='ResTelNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    provtelnum = models.CharField(db_column='ProvTelNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cellnum = models.CharField(db_column='CellNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empbustelnum = models.CharField(db_column='EmpBusTelNum', max_length=40, blank=True, null=True)  # Field name made lowercase.
    othercontactnum = models.CharField(db_column='OtherContactNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    spcellnum = models.CharField(db_column='SpCellNum', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mailingaddress = models.ForeignKey(Mailingaddress, models.DO_NOTHING, db_column='MailingAddress', blank=True, null=True)  # Field name made lowercase.
    resaddstreet = models.CharField(db_column='ResAddStreet', max_length=62, blank=True, null=True)  # Field name made lowercase.
    resaddbarangay = models.CharField(db_column='ResAddBarangay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resaddcity = models.CharField(db_column='ResAddCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resaddprovince = models.CharField(db_column='ResAddProvince', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resaddzipcode = models.CharField(db_column='ResAddZipCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ressince = models.PositiveSmallIntegerField(db_column='ResSince', blank=True, null=True)  # Field name made lowercase.
    restype = models.ForeignKey(Restype, models.DO_NOTHING, db_column='ResType', blank=True, null=True, related_name='restype')  # Field name made lowercase.
    provaddstreet = models.CharField(db_column='ProvAddStreet', max_length=40, blank=True, null=True)  # Field name made lowercase.
    provaddbarangay = models.CharField(db_column='ProvAddBarangay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provaddcity = models.CharField(db_column='ProvAddCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provaddprovince = models.CharField(db_column='ProvAddProvince', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provaddzipcode = models.CharField(db_column='ProvAddZipCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    provsince = models.PositiveSmallIntegerField(db_column='ProvSince', blank=True, null=True)  # Field name made lowercase.
    provtype = models.ForeignKey(Restype, models.DO_NOTHING, db_column='ProvType', blank=True, null=True)  # Field name made lowercase.
    busaddstreet = models.CharField(db_column='BusAddStreet', max_length=62, blank=True, null=True)  # Field name made lowercase.
    busaddbarangay = models.CharField(db_column='BusAddBarangay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    busaddcity = models.CharField(db_column='BusAddCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    busaddprovince = models.CharField(db_column='BusAddProvince', max_length=20, blank=True, null=True)  # Field name made lowercase.
    busaddzipcode = models.CharField(db_column='BusAddZipCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    spbusaddstreet = models.CharField(db_column='SpBusAddStreet', max_length=40, blank=True, null=True)  # Field name made lowercase.
    spbusaddbarangay = models.CharField(db_column='SpBusAddBarangay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spbusaddcity = models.CharField(db_column='SpBusAddCity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spbusaddprovince = models.CharField(db_column='SpBusAddProvince', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spbusaddzipcode = models.CharField(db_column='SpBusAddZipCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    busname = models.CharField(db_column='BusName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    busnature = models.CharField(db_column='BusNature', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bussince = models.PositiveSmallIntegerField(db_column='BusSince', blank=True, null=True)  # Field name made lowercase.
    busnumemployees = models.PositiveSmallIntegerField(db_column='BusNumEmployees', blank=True, null=True)  # Field name made lowercase.
    busjobtitle = models.CharField(db_column='BusJobTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    busstatus = models.ForeignKey(Busstatus, models.DO_NOTHING, db_column='BusStatus', blank=True, null=True)  # Field name made lowercase.
    busdatehired = models.DateField(db_column='BusDateHired', blank=True, null=True)  # Field name made lowercase.
    buslevel = models.ForeignKey(Buslevel, models.DO_NOTHING, db_column='BusLevel', blank=True, null=True)  # Field name made lowercase.
    busothersourceofincome = models.CharField(db_column='BusOtherSourceOfIncome', max_length=30, blank=True, null=True)  # Field name made lowercase.
    busprofessioncode = models.PositiveIntegerField(db_column='BusProfessionCode', blank=True, null=True)  # Field name made lowercase.
    busprofession = models.CharField(db_column='BusProfession', max_length=45, blank=True, null=True)  # Field name made lowercase.
    busoccupationcode = models.PositiveIntegerField(db_column='BusOccupationCode', blank=True, null=True)  # Field name made lowercase.
    busoccupation = models.CharField(db_column='BusOccupation', max_length=45, blank=True, null=True)  # Field name made lowercase.
    busindustrial = models.ForeignKey(Indu, models.DO_NOTHING, db_column='BusIndustrial', blank=True, null=True)  # Field name made lowercase.
    busindustrycode = models.ForeignKey(Industry, models.DO_NOTHING, db_column='BusIndustryCode', blank=True, null=True)  # Field name made lowercase.
    spfname = models.CharField(db_column='SpFName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spmname = models.CharField(db_column='SpMName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    splname = models.CharField(db_column='SpLName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spsname = models.CharField(db_column='SpSName', max_length=5, blank=True, null=True)  # Field name made lowercase.
    spgender = models.ForeignKey(Gender, models.DO_NOTHING, db_column='SpGender', blank=True, null=True, related_name='gender')  # Field name made lowercase.
    spdateofbirth = models.DateField(db_column='SpDateofBirth', blank=True, null=True)  # Field name made lowercase.
    spoccupational = models.ForeignKey(Occu, models.DO_NOTHING, db_column='SpOccupational', blank=True, null=True, related_name='occu')  # Field name made lowercase.
    spbusname = models.CharField(db_column='SpBusName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    spbusjobtitle = models.CharField(db_column='SpBusJobTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    spbusstatus = models.ForeignKey(Busstatus, models.DO_NOTHING, db_column='SpBusStatus', blank=True, null=True, related_name='busstatus')  # Field name made lowercase.
    spbussince = models.PositiveSmallIntegerField(db_column='SpBusSince', blank=True, null=True)  # Field name made lowercase.
    spbusdatehired = models.DateField(db_column='SpBusDateHired', blank=True, null=True)  # Field name made lowercase.
    spbuslevel = models.ForeignKey(Buslevel, models.DO_NOTHING, db_column='SpBusLevel', blank=True, null=True, related_name='buslevel')  # Field name made lowercase.
    spbusnature = models.CharField(db_column='SpBusNature', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spbusnumemployees = models.PositiveSmallIntegerField(db_column='SpBusNumEmployees', blank=True, null=True)  # Field name made lowercase.
    spothersourceofincome = models.CharField(db_column='SpOtherSourceOfIncome', max_length=200, blank=True, null=True)  # Field name made lowercase.
    closeddate = models.DateTimeField(db_column='ClosedDate', blank=True, null=True)  # Field name made lowercase.
    closedreason = models.ForeignKey(Closedreason, models.DO_NOTHING, db_column='ClosedReason', blank=True, null=True)  # Field name made lowercase.
    datetransferred = models.DateTimeField(db_column='DateTransferred', blank=True, null=True)  # Field name made lowercase.
    closeddestbranch = models.PositiveSmallIntegerField(db_column='ClosedDestBranch', blank=True, null=True)  # Field name made lowercase.
    originbranch = models.PositiveSmallIntegerField(db_column='OriginBranch', blank=True, null=True)  # Field name made lowercase.
    upduser = models.ForeignKey(Access, models.DO_NOTHING, db_column='UpdUser', blank=True, null=True, related_name='access')  # Field name made lowercase.
    upddatetime = models.DateTimeField(db_column='UpdDateTime', blank=True, null=True)  # Field name made lowercase.
    driverlicensenum = models.CharField(db_column='DriverLicenseNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datedeceased = models.DateField(db_column='DateDeceased', blank=True, null=True)  # Field name made lowercase.
    encdby = models.ForeignKey(Access, models.DO_NOTHING, db_column='EncdBy', blank=True, null=True)  # Field name made lowercase.
    encddatetime = models.DateTimeField(db_column='EncdDateTime', blank=True, null=True)  # Field name made lowercase.
    rating = models.ForeignKey(Rating, models.DO_NOTHING, db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    busempid = models.CharField(db_column='BusEmpID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sspexcluded = models.PositiveIntegerField(db_column='SSPExcluded', blank=True, null=True)  # Field name made lowercase.
    dosritag = models.ForeignKey(Dosritag, models.DO_NOTHING, db_column='DOSRITag', blank=True, null=True)  # Field name made lowercase.
    dosrirelatedto = models.CharField(db_column='DOSRIRelatedTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    speducattained = models.CharField(db_column='SpEducAttained', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spdegreecourse = models.CharField(db_column='SpDegreeCourse', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spoccupation = models.CharField(db_column='SpOccupation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spmonthlyincome = models.CharField(db_column='SpMonthlyIncome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scpledge = models.DecimalField(db_column='SCPledge', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sdpledge = models.DecimalField(db_column='SDPledge', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isshowtotalpoints = models.PositiveIntegerField(db_column='IsShowTotalPoints', blank=True, null=True)  # Field name made lowercase.
    recruiterid = models.ForeignKey('self', models.DO_NOTHING, db_column='RecruiterID', blank=True, null=True)  # Field name made lowercase.
    gsisnum = models.CharField(db_column='GSISNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nsonum = models.CharField(db_column='NSONum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    votersid = models.CharField(db_column='VotersID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pmesbatchnum = models.CharField(db_column='PMESBatchNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    otheridnum = models.CharField(db_column='OtherIDNum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pmesdate = models.DateField(db_column='PMESDate', blank=True, null=True)  # Field name made lowercase.
    empcode = models.ForeignKey(Empcode, models.DO_NOTHING, db_column='EmpCode', blank=True, null=True)  # Field name made lowercase.
    businessincome = models.CharField(db_column='BusinessIncome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mealallowance = models.DecimalField(db_column='MealAllowance', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clientdept = models.ForeignKey(Dept, models.DO_NOTHING, db_column='ClientDEPT', blank=True, null=True)  # Field name made lowercase.
    smsnumber = models.CharField(db_column='SMSNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    schoolid = models.ForeignKey(School, models.DO_NOTHING, db_column='SchoolID', blank=True, null=True)  # Field name made lowercase.
    sectionid = models.ForeignKey(Section, models.DO_NOTHING, db_column='SectionID', blank=True, null=True)  # Field name made lowercase.
    restrikid = models.ForeignKey(Restrik, models.DO_NOTHING, db_column='RestrikID', blank=True, null=True)  # Field name made lowercase.
    isincludehealthcare = models.PositiveIntegerField(db_column='IsIncludeHealthCare')  # Field name made lowercase.
    grouping = models.ForeignKey(Grouping, models.DO_NOTHING, db_column='Grouping', blank=True, null=True)  # Field name made lowercase.
    salescreditlimit = models.DecimalField(db_column='SalesCreditLimit', max_digits=15, decimal_places=2)  # Field name made lowercase.
    salescreditlimitadditional = models.DecimalField(db_column='SalesCreditLimitAdditional', max_digits=15, decimal_places=2)  # Field name made lowercase.
    salescreditlimitadditionalexpiry = models.DateField(db_column='SalesCreditLimitAdditionalExpiry', blank=True, null=True)  # Field name made lowercase.
    deductionlimit = models.DecimalField(db_column='DeductionLimit', max_digits=15, decimal_places=2)  # Field name made lowercase.

    def __str__(self):
        return u"%s %s" % (self.fname, self.lname)

    class Meta:
        managed = False
        db_table = 'client'
        unique_together = (('clientidbrcode', 'clientid'),)


class Collchart(models.Model):
    collchartid = models.AutoField(db_column='CollChartID', primary_key=True)  # Field name made lowercase.
    collchartdesc = models.CharField(db_column='CollChartDesc', max_length=45)  # Field name made lowercase.
    collchartbr_code = models.ForeignKey(Branches, models.DO_NOTHING, db_column='CollChartBR_CODE')  # Field name made lowercase.
    collchartremarks = models.TextField(db_column='CollChartRemarks', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.collchartdesc

    class Meta:
        managed = False
        db_table = 'collchart'





