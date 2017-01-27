from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	#custom permission to allow only owners of an object to modify it
	def has_object_permission(self, request, view, obj):
		#for any request -- > read permissions
		if request.method in permissions.SAFE_METHODS:
			return True
		#owners -> write permissions
		return obj.owner == request.user