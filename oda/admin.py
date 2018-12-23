from django.contrib import admin
from .models import Wraptype
from .models import Brand
from .models import Car_model
from .models import Driver
from .models import Pos_data
# Register your models here.
admin.site.register(Wraptype)
admin.site.register(Brand)
admin.site.register(Car_model)
admin.site.register(Driver)
admin.site.register(Pos_data)