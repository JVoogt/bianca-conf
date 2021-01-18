d = { 'D1F80A':['GarageDoor1','ON','true'],
      'D1F80E':['GarageDoor1','OFF','true'],
      'D1660A':['GarageDoor2','ON','true'],
      'D1660E':['GarageDoor2','OFF','true'],
      'D08D0A':['GarageDoor3','ON','true'],
      'D08D0E':['GarageDoor3','OFF','true']
    }

p = data.get('payload')

if p is not None:
  if p in d.keys():
    service_data = {'topic':'433/{}'.format(d[p][0]), 'payload':'{}'.format(d[p][1]), 'qos':2, 'retain':'{}'.format(d[p][2])}
  else:
    service_data = {'topic':'433/unknown', 'payload':'{}'.format(p), 'qos':0, 'retain':'false'}
    logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(p))
  hass.services.call('mqtt', 'publish', service_data, False)