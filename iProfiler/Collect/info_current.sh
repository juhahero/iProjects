#!/bin/sh
while true
do 
	#power_wakelock
	date >> /sdcard/power_wakelock.log
	dumpsys power >> /sdcard/power_wakelock.log
	
	#cpuinfo
	date >> /sdcard/cpuinfo.log
	dumpsys cpuinfo >> /sdcard/cpuinfo.log
	
	#cpustat
	date >> /sdcard/cpustat.log
	cat /proc/stat >> /sdcard/cpustat.log
	
	#cpufreq
	date >> /sdcard/cpufreq.log
	cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq >> /sdcard/cpufreq.log
	
	#gpustat
	date >> /sdcard/gpustat.log
	cat /sys/class/kgsl/kgsl-3d0/gpubusy >> /sdcard/gpustat.log
	
	#procrank
	date >> /sdcard/procrank.log
	procrank >> proc_rank.log
	
	sleep 30
done