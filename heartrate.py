
#/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import time
import csv

ANALOG_IN = 'P9_40'
SAMPLE_RATE = 10                #Hertz (~100 samples every second)
data_list = []                  # Making two lists to throw all analog readings into, one for time and one for Volt
time_list = []
header = ["time", "volt"]       # assigning each column a title for the CSV file; Time and Volt

start_time = time.time()

def write_csv_from_lists(data_list, header, rawDataCSV):
        rawDataCSV = open('rawDataCSV.csv', 'w')
        with rawDataCSV:
                writer = csv.writer(rawDataCSV)
                writer.writerow(header)
                def read_adc(adc_pin):
                        ADC.read("P9_40")
                        return ADC.read("P9_40")

                #Configure ADC
                ADC.setup()

        # execute until keyboard interrupt
                try:
                        while True:
                                value = read_adc("P9_40")
                                data_list.append(value * 1.8)
                                time_list.append(time.time() - start_time)
                                print("time: ", time.time() - start_time,  "Volt: ",  (value * 1.8))    # Displays time of reading in millisec from start of loop, assigned with the Volt at the time of reading
                                time.sleep(1/SAMPLE_RATE)

                except KeyboardInterrupt:
                        pass

                writer.writerows(zip(time_list, data_list))
write_csv_from_lists(data_list, header, "rawDataCSV.csv")





