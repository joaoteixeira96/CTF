# Redeemer

##  nmap -p- -sV 10.129.37.89
Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-07 05:54 EDT
Nmap scan report for 10.129.37.89
Host is up (0.060s latency).
Not shown: 65534 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.7

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 78.14 seconds

##  redis-cli -h 10.129.37.89

##  10.129.37.89:6379>INFO
Server
redis_version:5.0.7
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:66bd629f924ac924
redis_mode:standalone
os:Linux 5.4.0-77-generic x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:atomic-builtin
gcc_version:9.3.0
process_id:753
run_id:bbe9deb8a62871d85ea1d46b5cade1662c0c6347
tcp_port:6379
uptime_in_seconds:1839
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:10429885
executable:/usr/bin/redis-server
config_file:/etc/redis/redis.conf
Clients
connected_clients:1
client_recent_max_input_buffer:2
client_recent_max_output_buffer:0
blocked_clients:0

Memory
used_memory:859624
used_memory_human:839.48K
used_memory_rss:5988352
used_memory_rss_human:5.71M
used_memory_peak:859624
used_memory_peak_human:839.48K
used_memory_peak_perc:100.00%
used_memory_overhead:847166
used_memory_startup:797248
used_memory_dataset:12458
used_memory_dataset_perc:19.97%
allocator_allocated:1584120
allocator_active:1937408
allocator_resident:9158656
total_system_memory:2084024320
total_system_memory_human:1.94G
used_memory_lua:41984
used_memory_lua_human:41.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.22
allocator_frag_bytes:353288
allocator_rss_ratio:4.73
allocator_rss_bytes:7221248
rss_overhead_ratio:0.65
rss_overhead_bytes:-3170304
mem_fragmentation_ratio:7.32
mem_fragmentation_bytes:5170736
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:49694
mem_aof_buffer:0
mem_allocator:jemalloc-5.2.1
active_defrag_running:0
lazyfree_pending_objects:0

Persistence
loading:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1654596116
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:413696
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0

Stats
total_connections_received:6
total_commands_processed:6
instantaneous_ops_per_sec:0
total_net_input_bytes:317
total_net_output_bytes:14888
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:341
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0

Replication
role:master
connected_slaves:0
master_replid:32e0ff528849efe3a34aae105d499cfca6e27265
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

CPU
used_cpu_sys:1.680515
used_cpu_user:1.817142
used_cpu_sys_children:0.001502
used_cpu_user_children:0.000000

Cluster
cluster_enabled:0

Keyspace
db0:keys=4,expires=0,avg_ttl=0

##  10.129.37.89:6379>DBSIZE

##  10.129.37.89:6379>KEYS *

## 03e1d2b376c37ab3f5319922053953eb
