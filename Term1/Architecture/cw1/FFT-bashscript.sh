#!/bin/bash

export SSFLAGS="-ruu:size 16 -lsq:size 16 -cache:dl1 dl1:8:32:2:l -cache:il1 il1:32:32:4:f -res:ialu 2 -res:fpalu 1 -bpred:btb 2048 4"
./run-wattch 2>&1 | awk '/sim_IPC/ {printf("sim_IPC, %s\n",$2)};\
/ruu_full/ {printf("ruu_full, %s\n", $2)};\
/lsq_full/ {printf("lsq_full, %s\n", $2)};\
/avg_sim_slip/ {printf("avg_sim_slip, %s\n", $2)};\
/sim_exec_BW/ {printf("sim_exec_BW, %s\n", $2)};\
/il1.miss_rate/ {printf("il1.miss_rate, %s\n", $2)};\
/dl1.miss_rate/ {printf("dl1.miss_rate, %s\n", $2)};\
/ul2.miss_rate/ {printf("ul2.miss_rate, %s\n", $2)};\
/bpred_addr_rate/ {printf("bpred_addr_rate, %s\n", $2)};\
/bpred_dir_rate/ {printf("bpred_dir_rate, %s\n", $2)};\
/avg_rename_power_cc1/ {printf("avg_ruu_power, %s\n", $2)};\
/avg_bpred_power_cc1/ {printf("avg_bpred_power, %s\n", $2)};\
/avg_lsq_power_cc1/ {printf("avg_lsq_power, %s\n", $2)};\
/avg_icache_power_cc1/ {printf("avg_icache_power, %s\n", $2)};\
/avg_dcache_power_cc1/ {printf("avg_dcache_power, %s\n", $2)};\
/avg_dcache2_power_cc1/ {printf("avg_dcache2_power, %15s\n", $2)};\
/avg_alu_power_cc1/ {printf("avg_alu_power, %s\n", $2)};\
/^total_power_cycle_cc1/ {printf("total_power, %15s\n", $2)};\
/avg_total_power_cycle_cc1/ {printf("avg_total_power, %15s\n", $2)};
'
