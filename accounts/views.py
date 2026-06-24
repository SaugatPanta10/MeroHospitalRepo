from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class DynamicRoleLoginView(LoginView):
    template_name = 'login.html' # Points to our upcoming universal login card template
    
    def get_success_url(self):
        user = self.request.user
        
        # Interrogate the logged-in user profile's internal database role
        if user.role == user.Role.ADMIN:
            return reverse_lazy('accounts:admin_dashboard')
        elif user.role == user.Role.DOCTOR:
            return reverse_lazy('doctors:doctor_dashboard')
        elif user.role == user.Role.PATIENT:
            return reverse_lazy('patients:patient_dashboard')
            
        # Standard safety net fallback
        return reverse_lazy('home_page')