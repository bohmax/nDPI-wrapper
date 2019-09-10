#include <ndpiReader.c>

int ndpi_wrap_idle_scan_budget(){
    return IDLE_SCAN_BUDGET;
}

struct reader_thread* execute(int argc, char** argv, struct ndpi_detection_module_struct * replace, struct timeval time){
	int i = 0;
	startup_time = time;
	ndpi_info_mod = replace;
	memset(ndpi_thread_info, 0, sizeof(ndpi_thread_info));

    parseOptions(argc, argv);

    if((!json_flag) && (!quiet_mode)) {

      printf("Using nDPI (%s) [%d thread(s)]\n", ndpi_revision(), num_threads);
    }

    signal(SIGINT, sigproc);

    for(i=0; i<num_loops; i++)
      test_lib();
    if(results_path)  free(results_path);
    if(results_file)  fclose(results_file);
    if(extcap_dumper) pcap_dump_close(extcap_dumper);

    return ndpi_thread_info;
}

void free_detection_module_struct(struct ndpi_detection_module_struct * replace){
	ndpi_info_mod = replace;
	if(ndpi_info_mod) ndpi_exit_detection_module(ndpi_info_mod);
}