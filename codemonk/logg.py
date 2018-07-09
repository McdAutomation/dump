import logging
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
print(numeric_level)
logging.basicConfig(level=numeric_level)
