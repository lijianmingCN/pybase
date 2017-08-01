# -*- coding: utf-8 -*-
import psutil

def printCPUInfo():
    cpu_times = psutil.cpu_times()
    print '用户的CPU时间比:'+str(cpu_times.user)
    print '执行用户进程的CPU时间比:'+str(cpu_times.user)
    print '执行内核进程和中断的时间百分比:'+str(cpu_times.system)
    print 'CPU处于Idle状态的时间百分比:'+str(cpu_times.idle)

def printPerCPUInfo():
    cpu_times = psutil.cpu_times(percpu = True)
    for cpu in cpu_times:
        print '--------------------'
        print '用户的CPU时间比:'+str(cpu.user)
        print '执行用户进程的CPU时间比:'+str(cpu.user)
        print '执行内核进程和中断的时间百分比:'+str(cpu.system)
        print 'CPU处于Idle状态的时间百分比:'+str(cpu.idle)
        print '--------------------'

def printCPUCount():
    print '逻辑CPU个数:'+str(psutil.cpu_count())
    print '物理CPU个数:'+str(psutil.cpu_count(logical=False))


def printVirtualMemory():
    virtualMemory = psutil.virtual_memory()
    print '内存总数:'+str(virtualMemory.total)
    print '可用内存:'+str(virtualMemory.available)
    print '内存使用率:'+str(virtualMemory.percent)
    print '正在使用使用:'+str(virtualMemory.used)
    print '空闲内存:'+str(virtualMemory.free)
    
def printSwapMemory():
    swapMemory = psutil.swap_memory()
    print swapMemory.total
    print swapMemory.used
    print swapMemory.free
    print swapMemory.percent
    print swapMemory.sin
    print swapMemory.sout
    
def printDiskIOCounter():
    ioCounter = psutil.disk_io_counters()
    print ioCounter.read_count
    print ioCounter.write_count
    print ioCounter.read_bytes
    print ioCounter.write_bytes
    print ioCounter.read_time
    print ioCounter.write_time

def printPerDiskIOCounter():
    ioCounters = psutil.disk_io_counters(perdisk=True)
    for io in ioCounters:
        print '--------------------'
        print io
        print ioCounters[io].read_count
        print ioCounters[io].write_count
        print ioCounters[io].read_bytes
        print ioCounters[io].write_bytes
        print ioCounters[io].read_time
        print ioCounters[io].write_time
        print '--------------------'
    
def printDiskUsage():
    diskUsage = psutil.disk_usage('/')
    print diskUsage.total
    print diskUsage.used
    print diskUsage.free
    print diskUsage.percent

def printDiskPartitions():
    diskPartitions = psutil.disk_partitions()
    for part in diskPartitions:
        print part

def printNetIOCointers():
    ioCounters = psutil.net_io_counters()
    print ioCounters.bytes_sent
    print ioCounters.bytes_recv
    print ioCounters.packets_sent
    print ioCounters.packets_recv
    print ioCounters.errin
    print ioCounters.errout
    print ioCounters.dropin
    print ioCounters.dropout
    
def printPerNetIOCointers():
    netioCounters = psutil.net_io_counters(pernic=True)
    for net in netioCounters:
        print '--------------------'
        print net
        print netioCounters[net].bytes_sent
        print netioCounters[net].bytes_recv
        print netioCounters[net].packets_sent
        print netioCounters[net].packets_recv
        print netioCounters[net].errin
        print netioCounters[net].errout
        print netioCounters[net].dropin
        print netioCounters[net].dropout
        print '--------------------'
#todo
def printNetConnections():
    netConnections = psutil.net_connections()
    print netConnections


def printUsers():
    users = psutil.users()
    for user in users:
        print '--------------------'
        print user.name
        print user.terminal
        print user.host
        print user.started
        print '--------------------'
    
def printBootTime():
    print psutil.boot_time()

def printProcess():
    print psutil.get_pid_list()

def doProcess(pid):
    p = psutil.Process(pid)
    print '进程路径'+str(p.exe())
    print '进程名'+str(p.name())
    print '进程绝对路径'+str(p.getcwd())
    print p.cmdline()
    print '进程状态'+p.status()
    print p.username()
    print '进程创建时间'+str(p.create_time())
    print p.memory_info_ex()
    #print p.uids()
    #print p.gids()
    print p.get_cpu_times()
    print p.get_cpu_percent(interval=1.0)
    print p.get_cpu_affinity()
    print p.set_cpu_affinity([0])
    print p.get_memory_percent()
    print p.get_memory_info()
    print p.get_ext_memory_info()
    print p.get_io_counters()
    print p.get_open_files()
    print p.get_connections()
    print p.get_num_threads()
    #print p.get_num_fds()
    print p.get_num_ctx_switches()
    print p.get_threads()
    print p.get_nice()
    #print p.set_nice(10)
    print p.suspend()
    #print p.wait(timeout=3)
    print psutil.test()
    print p.get_memory_maps()
    #p.terminate

def printPopen():
    p = psutil.Popen(['/usr/bin/python','-c','print("hello")'],stdout=PIPE)
    print p.name()
    print p.username()
    print p.communicate()
    print p.cpu_times()
    
if __name__ == '__main__':
    printCPUInfo()
    #printPerCPUInfo()
    #printCPUCount()
    #printVirtualMemory()
    #printSwapMemory()
    #printDiskIoCounter()
    #printPerDiskIOCounter()
    #printDiskUsage()
    #printDiskPartitions()
    #printPerNetIOCointers()
    #printNetIOCointers()
    #printNetConnections()
    #printUsers()
    #printBootTime()
    #printProcess()
    #doProcess(15936)
