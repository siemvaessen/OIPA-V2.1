from django.db import models
import base64

class MediumTextField(models.Field):
    def db_type(self, connection):
        return 'mediumtext'

class requested_call(models.Model):
    call = models.CharField(max_length=255, primary_key=True)
    cached = models.BooleanField(default=False)
    response_time = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __unicode__(self,):
        return "%s" % (self.call)

class cached_call(models.Model):
    call = models.CharField(max_length=255, primary_key=True)
    last_fetched = models.DateTimeField(null=True, default=None)
    result = MediumTextField()

    def __unicode__(self,):
        return "%s" % (self.call)





    #result = models.FileField(upload_to='calls', null=True, default=None)
    #_result = models.TextField(db_column='result', blank=True)
    #
    #def set_data(self, data):
    #    self._data = base64.encodestring(data)
    #
    #def get_data(self):
    #    return base64.decodestring(self._data)
    #
    #result = property(get_data, set_data)
    #
