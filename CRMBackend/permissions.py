from rest_framework import permissions


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):


    edit_methods = ( "POST")

    def has_permission(self, request, view):
        if request.method  in  self.edit_methods  and  request.user.role == 'responsable':
               
            return True
  
    # def has_object_permission(self, request, view, obj):
    #     if request.user.is_superuser:
    #         return True
    #     if request.method in permissions.SAFE_METHODS:
    #             return True
       
        