from tkinter import *
from tkinter import font
import platform, psutil

from CPUBench import CPU_Benchmark
from DiskBench import Disk_Benchmark
from MemoryBench import MemoryBench

sys =      f"System :  {platform.system()}"
proc =     f"Processor :  {platform.processor()}"
machine =  f"Machine :  {platform.machine()}"
ver =      f"Version :  {platform.version()}"
ram =      f"Ram :  {round(psutil.virtual_memory().total / (1024.0 ** 3))} GB"
cpu_core = f"CPU Core :  {psutil.cpu_count()} core"

def cpu():
    time_cpu = CPU_Benchmark()
    time_memory = MemoryBench()
    time_disk = Disk_Benchmark()
    
    cpu_time.set(time_cpu)
    mem_time.set(time_memory)
    disk_time.set(time_disk)
    total = time_cpu + time_memory + time_disk
    total_time.set(total)

def exit():
    root.destroy()

# ------------------------------------------------------------------------------------------ #

root = Tk()
root.geometry("880x450")
root.resizable(False, False)
root.title("Benchmark")
title_label = Label(root, text = "Benchmark", font = ("Arial Bold", 24)).place(x = 368, y = 15)

sys_label = Label(root, text = sys, font = ("Arial", 15)).place(x = 20, y = 50)
proc_label = Label(root, text = proc, font = ("Arial", 15)).place(x = 20, y = 75)
machine_label = Label(root, text = machine, font = ("Arial", 15)).place(x = 20, y = 100)
ver_label = Label(root, text = ver, font = ("Arial", 15)).place(x = 20, y = 125)
ram_label = Label(root, text = ram, font = ("Arial", 15)).place(x = 20, y = 150)
core_label = Label(root, text = cpu_core, font = ("Arial", 15)).place(x = 20, y = 175)

# CPU_Bench
cpu_label = Label(root, text = "CPU score : ", font = ("Arial", 16)).place(x = 20, y = 235)

cpu_time = StringVar()
cpu_score = Label(root, textvariable = cpu_time ,font = ("Arial", 16), fg = "red")
cpu_score.place(x = 150, y = 235)

# Memory_Bench
mem_label = Label(root, text = "Memory score : ", font = ("Arial", 16)).place(x = 20, y = 260)

mem_time = StringVar()
mem_score = Label(root, textvariable = mem_time, font=("Arial", 16), fg="red")
mem_score.place(x=150, y=260)

# Disk_Bench
disk_label = Label(root, text = "Disk score : ", font = ("Arial", 16)).place(x = 20, y = 285)

disk_time = StringVar()
disk_score = Label(root, textvariable = disk_time,font = ("Arial", 16), fg = "red")
disk_score.place(x = 150, y = 285)

total_time = StringVar()
total_label = Label(root, text = "Total score : ", font = ("Arial", 16)).place(x = 20, y = 310)
total_score = Label(root, textvariable = total_time, font= ("Arial", 16), fg="red").place(x = 150, y = 310)

start_button = Button(root, text = "Start", command = cpu).place(x = 411 , y = 360)
exit_button = Button(root, text = "Exit", fg = "red", command = exit).place(x = 415 , y = 390)


root.mainloop()