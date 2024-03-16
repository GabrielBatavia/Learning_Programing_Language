import multiprocessing # import library multiprocessing
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

if __name__ == "__main__":
	# creating thread
	p1 = multiprocessing.Process(target=print_with_dynamic_sleep, args=(5,))
	p2 = multiprocessing.Process(target=print_with_static_sleep, args=(5,))

	# memulai process pertama
	p1.start()
	# memulai process kedua
	p2.start()

	# tunggu sampai process 1 selesai dilaksanakan
	p1.join()
	# tunggu sampai process 2 selesai dilaksanakan
	p2.join()

	# both threads completely executed
	print("Selesai!")
    print("Bagus hasilnya")
 