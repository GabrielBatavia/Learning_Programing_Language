import threading # import library threading
import time # import library time

def print_with_dynamic_sleep(total_iteration):
    """
    fungsi berikut akan melakukan print command
    dengan interval yang berbeda-beda
    """
    for x in range(total_iteration):
        print("Hello from dynamic-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(x) # fungsi akan berhenti selama x second, akan berubah2 secara dinamis

def print_with_static_sleep(total_iteration):
    """
	fungsi berikut akan melakukan print command
	dengan interval yang statis/sama
    """
    for x in range(total_iteration):
        print("Hello from static-sleep interval, pengulangan ke-{}".format(x))
        time.sleep(2) # fungsi akan berhenti selama 2 second