from django.contrib import admin
from .models import StudentRecord, Issuer, StudentReturn, SchoolLogo, LibraryShelve, BorrowerImage, TeachersRecord,\
                    TeachersReturn, TeacherImage


# Register your models here.
admin.site.register(StudentRecord)
admin.site.register(Issuer)
admin.site.register(StudentReturn)

admin.site.register(SchoolLogo)
admin.site.register(LibraryShelve)
admin.site.register(BorrowerImage)
admin.site.register(TeachersRecord)
admin.site.register(TeachersReturn)
admin.site.register(TeacherImage)

