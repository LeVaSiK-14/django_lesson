from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    SchoolView, ClasView,
    StudentView,
)

router = DR()

router.register('school', SchoolView)
router.register('clas', ClasView)
router.register('student', StudentView)


urlpatterns = []

urlpatterns += router.urls


# get list      http://127.0.0.1:8000/school/
# get retrieve  http://127.0.0.1:8000/school/1
# post          http://127.0.0.1:8000/school/
# put           http://127.0.0.1:8000/school/1
# patch         http://127.0.0.1:8000/school/1
# delete        http://127.0.0.1:8000/school/1


# {
#     'id': 1,
#     'name': 'matematicheskaya 1',
#     'number': 61,
#     'address': 'maldybaeva 61'
# }


# {
#     'name': 'matematicheskaya 1',
# }



# CRUD

# Create
# Read
# Update
# Delete