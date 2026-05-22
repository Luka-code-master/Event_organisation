from rest_framework.throttling import ScopedRateThrottle


class RegistrationThrottle(ScopedRateThrottle):
    scope = 'registration_burst' 