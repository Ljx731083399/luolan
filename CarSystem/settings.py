class Config:
    INSTALLED_APPS = [
        'mongoengine',
    ]
    from mongoengine import disconnect
    disconnect('test')
class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False