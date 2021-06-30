import ubidots


ubidots_client = ubidots.ApiClient(token='BBFF-i8XWP7su6Zg9oq7PGcJsXC4hUQxmxN')
flagged_vehicles = ubidots_client.get_variable('608420c81d84727ad63e7dd8')


def report(vehicle):
    flagged_vehicles.save_value({'value': vehicle.id})
