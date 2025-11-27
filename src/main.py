from src.car_park import CarPark
from src.display import Display
from src.sensor import EntrySensor, ExitSensor


def main():
    # create car park and save config
    car_park = CarPark("Moondalup", 5)
    car_park.write_config()

    # load from config
    car_park = CarPark.from_config()

    # display
    main_display = Display(1)
    car_park.register(main_display)

    # entry and exit sensors
    entry_sensor = EntrySensor(1, True, car_park)
    exit_sensor = ExitSensor(2, True, car_park)
    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    # cars entering
    for _ in range(3):
        entry_sensor.detect_vehicle()

    # cars leaving
    for _ in range(2):
        exit_sensor.detect_vehicle()

    print(main_display.message)


if __name__ == "__main__":
    main()
