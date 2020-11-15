import argparse
import json
import sched
import time
import psutil

from modules.write_information_to_log_files import setup_logger,\
    log_info, log_critical_info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--config", required=True,
                    help="path to config file")

    args = vars(ap.parse_args())
    file = args["config"]

    try:
        with open(file, 'r') as config_file:
            config = json.load(config_file)
    except OSError:
        print(f'You haven\'t {file} file')
        exit(1)

    try:
        critical_ram = config["ram"]
        critical_list_cpu = config["cpu"]
        critical_temp_gpu = config["temp_gpu"]
        critical_mem_gpu = config["mem_gpu"]
        critical_dict_temperature = config["temperature"]
        path_to_logs = config["logs"]
        time_to_wait = config["time_for_logging_information"]
    except KeyError:
        print('KeyError while reading config. Check your configuration file.')
        exit(22)

    logger = setup_logger([path_to_logs + "/Info.log", path_to_logs +
                           "/ExcessIndicators.log"])

    scheduler = sched.scheduler(time.time, time.sleep)

    scheduler.enter(
        time_to_wait, 1, log_info,
        [
            scheduler,
            logger,
            critical_dict_temperature,
            time_to_wait, ])

    count_of_cpu = psutil.cpu_count()

    scheduler.enter(
        1, 1, log_critical_info,
        [
            scheduler,
            logger,
            critical_dict_temperature,
            critical_list_cpu,
            critical_ram,
            critical_temp_gpu,
            critical_mem_gpu,
            count_of_cpu, ])

    scheduler.run()


if __name__ == '__main__':
    main()

