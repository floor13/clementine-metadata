import dbus
session_bus = dbus.SessionBus()
player = session_bus.get_object('org.mpris.clementine', '/Player')
iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')
metadata = iface.GetMetadata()

#protocol = metadata['location'] + '\n'

print(metadata['title'] + ' - ' + metadata['artist'])
