services_to_register = [
    {
        "name": "rewards-svc",
        "version": "0.1.0",
        "owner": "engagement@aeropay.io",
        "environment": "staging",
        "status": "healthy",
        "health_url": "/health/rewards",
        "dependencies": ["notification-svc"],
    },
    {
        "name": "audit-trail-svc",
        "version": "1.0.0",
        "owner": "compliance@aeropay.io",
        "environment": "production",
        "status": "healthy",
        "health_url": "/health/audit-trail",
        "dependencies": [],
    },
    {
        "name": "rate-limiter",
        "version": "0.9.0",
        "owner": "platform@aeropay.io",
        "environment": "production",
        "status": "healthy",
        "health_url": "/health/rate-limiter",
        "dependencies": ["api-gateway", "auth-svc"],
    },
]