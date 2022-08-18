from rest_framework.throttling import UserRateThrottle

class MyRateThrottle(UserRateThrottle):
    scope = 'MyRate'