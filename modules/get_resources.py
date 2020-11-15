import psutil
import GPUtil as GPU


def get_gpu():
    gpu = None
    gpu_temp = None
    gpu_memory = None

    GPUs = GPU.getGPUs()
    if GPUs:
        gpu = GPUs[0]
        gpu_memory = gpu.memoryUtil
        gpu_temp = gpu.temperature
    return gpu, gpu_temp, gpu_memory


def get_resources(critical_dict_temperature, logger):

    temperatures_list = psutil.sensors_temperatures()["coretemp"]
    temperatures = [(temp[0], temp[1]) for temp in temperatures_list
                    if temp[0] in critical_dict_temperature.keys()]

    cpu_list = psutil.cpu_percent(interval=None, percpu=True)

    # psutil.virtual_memory()[3] == ram is used
    ram_used = psutil.virtual_memory()[3]
    try:
        # psutil.virtual_memory()[4] == free ram
        ram = ram_used / (ram_used + psutil.virtual_memory()[4])
    except ZeroDivisionError:
        logger.critical("CRITICAL! Exception: Amount of RAM == 0")
        exit(1)

    return temperatures, cpu_list, ram

