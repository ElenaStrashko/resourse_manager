import logging

from modules.get_resources import get_resources, get_gpu


def setup_logger(log_file):
    logger = logging.getLogger('resource_manager')
    logger.setLevel(logging.INFO)

    info_log = logging.FileHandler(log_file[0])
    info_log.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    info_log.setLevel(logging.INFO)

    critical_log = logging.FileHandler(log_file[1])
    critical_log.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    critical_log.setLevel(logging.CRITICAL)

    logger.addHandler(info_log)
    logger.addHandler(critical_log)

    return logger


def log_info(scheduler, logger, critical_dict_temperature, time_to_wait):

    temperatures, cpu_list, ram = get_resources(critical_dict_temperature,
                                                logger)
    gpu, gpu_temp, gpu_memory = get_gpu()

    for name, temp in temperatures:
        logger.info(f'INFO: For {name} temperature is {temp}')
    for i in range(len(cpu_list)):
        logger.info(f'INFO: Processor core utilization percentage'

                    f' {i} is {cpu_list[i]}')

    logger.info(f'INFO: Percentage of occupied RAM is {ram}')

    if gpu is not None:
        logger.info(f'INFO: The percentage of used GPU memory {gpu_memory}')
        logger.info(f'INFO: Temperature of GPU is {gpu_temp}')

    scheduler.enter(time_to_wait, 1, log_info,
                    [
                        scheduler,
                        logger,
                        critical_dict_temperature,
                        time_to_wait, ])


def log_critical_info(scheduler, logger, critical_dict_temperature,
                      critical_list_cpu, critical_ram, critical_temp_gpu,
                      critical_mem_gpu, count_of_cpu):

    temperatures, cpu_list, ram = get_resources(critical_dict_temperature,
                                                logger)
    gpu, gpu_temp, gpu_memory = get_gpu()

    for name, temp in temperatures:
        if temp >= critical_dict_temperature[name]:
            logger.critical(f'CRITICAL TEMPERATURE! For'
                            f' {name} temperature is {temp}')

    for index in range(len(critical_list_cpu)):
        if count_of_cpu <= index:
            print(f'You write a lof of cores in config in cpu.'
                  f' Your computer has only {count_of_cpu} cores')
        else:
            if cpu_list[index] >= critical_list_cpu[index]:
                logger.critical(f'CRITICAL PROCESSOR CORE UTILIZATION PERCENTAGE!'
                                f'For core {index} is {cpu_list[index]}')

    if ram >= critical_ram:
        logger.critical(f'CRITICAL PERCENTAGE OF OCCUPIED'
                        f' RAM! It is {ram}')

    if gpu is not None:
        if gpu_temp >= critical_temp_gpu:
            logger.critical(f'CRITICAL TEMPERATURE OF'
                            f' GPU! It is {gpu_temp}')

        if gpu_memory >= critical_mem_gpu:
            logger.critical(f'CRITICAL PERCENTAGE OF'
                            f' USED GPU MEMORY! It is {gpu_memory}')

    scheduler.enter(1, 1, log_critical_info,
                    [
                        scheduler,
                        logger,
                        critical_dict_temperature,
                        critical_list_cpu,
                        critical_ram,
                        critical_temp_gpu,
                        critical_mem_gpu,
                        count_of_cpu, ])

